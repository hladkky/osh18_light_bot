import hashlib

from google.protobuf.empty_pb2 import Empty

from constants import MACHINE_ID
from proto.auth.auth_endpoints_pb2_grpc import AuthServiceStub
from proto.auth.auth_endpoints_pb2_grpc import AuthServiceStub as NewAuthServiceStub
from proto.auth.auth_pb2 import LoginRequest


class LoginService:
    def __init__(self, client):
        self._client = client

    async def login(self, email: str, password: str):
        # login
        auth = NewAuthServiceStub(self._client.channel)
        password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
        result = await auth.login(
            LoginRequest(
                login=email, password=password, machine_id=MACHINE_ID
            ),
            timeout=13,
            metadata=self._client.metadata,
        )
        metadata = (
            ("x-session-user", str(result.user_id)),
            ("x-session-token", str(result.session_token)),
            *self._client.metadata,
        )

        # login into personal
        stub = AuthServiceStub(self._client.channel)
        result = await stub.loginIntoPersonalAccount(Empty(), metadata=metadata, timeout=10)
        self._client.metadata = (
            ("x-session-user", str(result.user_id)),
            ("x-session-token", str(result.session_token)),
            *self._client.metadata,
        )
        return result
