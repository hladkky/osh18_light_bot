import asyncio

import loguru
from google.protobuf.message import Message
from grpc.aio import UnaryStreamCall, AioRpcError

from constants import HUB_ID, SOCKET_ID
from proto.common.hub.object_type_pb2 import Hub
from proto.hub.hub_endpoints_pb2 import StreamHubChangesRequest
from proto.hub.hub_endpoints_pb2_grpc import HubServiceStub
from proto.hub.main.update_pb2 import Update


def _find_socket_in_source(source: Hub):
    filtered = [
        device.socket for device in source.devices
        if device.WhichOneof("test_oneof") == "socket" and device.socket.common_part.id == SOCKET_ID
    ]
    return filtered[0] if filtered else None


def _find_socket_in_update(update: Update):
    if (
            update.WhichOneof("test_oneof") != "device" or
            update.device.WhichOneof("test_oneof") != "socket" or
            update.device.socket.common_part.id != SOCKET_ID
    ):
        return None
    return update.device.socket


class HubStreamService:
    def __init__(self, client):
        self._client = client
        self._stream: UnaryStreamCall = None
        self._queue = asyncio.Queue()
        self._power_exists = False

    def stop_stream_socket_state(self):
        self._stream.cancel()

    async def start_stream_socket_state(self):
        while True:
            try:
                async for socket in self._stream_hub_changes():
                    loguru.logger.debug(f"Socket message from hub stream: {repr(socket)}")
                    if socket.common_part.HasField("online"):
                        yield socket.common_part.online.value
            except AioRpcError as e:
                loguru.logger.error(e)
                await asyncio.sleep(5)

    async def _stream_hub_changes(self):
        stub = HubServiceStub(self._client.channel)
        print("metadata", self._client.metadata)
        self._stream = stub.streamHubChanges(StreamHubChangesRequest(hub_id=HUB_ID), metadata=self._client.metadata)

        async for changes in self._stream:
            changes: Message
            one_of = changes.WhichOneof("test_oneof")
            socket = None
            if one_of == "source":
                socket = _find_socket_in_source(getattr(changes, one_of))
            if one_of == "update":
                socket = _find_socket_in_update(getattr(changes, one_of))
            if socket:
                yield socket
