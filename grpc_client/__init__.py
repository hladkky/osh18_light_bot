import asyncio
import json
from pathlib import Path

import grpc
import loguru
from grpc.aio import AioRpcError
from rx.subject import Subject

from constants import TARGET, CREDENTIALS_PASSWORD, CREDENTIALS_EMAIL, USER_AGENT, APPLICATION_LABEL, CLIENT_VERSION
from grpc_client.services.hub_stream import HubStreamService
from grpc_client.services.login import LoginService

CACHE_FILE = Path(__file__).parent / "cache.json"


def get_light_exists_from_cache():
    try:
        with open(CACHE_FILE) as f:
            cache = json.loads(f.read())
            return cache.get("light_exists")
    except IOError:
        return None


def set_light_exists_to_cache(value):
    with open(CACHE_FILE, "w") as f:
        f.write(json.dumps({
            "light_exists": value
        }))


class GRPCClient:
    def __init__(self):
        self.channel = None
        self._create_channel()
        self.metadata = (
            ("x-user-agent", USER_AGENT),
            ("client-version-major", CLIENT_VERSION),
            ("application-label", APPLICATION_LABEL),
        )
        self.login_service = LoginService(self)
        self.hub_stream_service = HubStreamService(self)
        self._light_exists = get_light_exists_from_cache()

    async def login(self):
        await self.login_service.login(CREDENTIALS_EMAIL, CREDENTIALS_PASSWORD)

    async def start_power_monitoring(self, subject: Subject):
        while True:
            try:
                await self.login()
                loguru.logger.debug("Successfully logged in.")
                async for state in self.hub_stream_service.start_stream_socket_state():
                    self.update_light_exists(state, subject)
            except AioRpcError as e:
                loguru.logger.error(e)
                await asyncio.sleep(5)

    async def stop_power_monitoring(self):
        self.hub_stream_service.stop_stream_socket_state()

    def update_light_exists(self, value: bool, subject: Subject):
        if self._light_exists is None:
            self._light_exists = value
        elif self._light_exists != value:
            self._light_exists = value
            subject.on_next(value)

        set_light_exists_to_cache(value)

    def _create_channel(self):
        self.channel = grpc.aio.secure_channel(
            target=TARGET,
            credentials=grpc.ssl_channel_credentials()
        )
