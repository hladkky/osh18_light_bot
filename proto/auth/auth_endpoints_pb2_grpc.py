# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto.auth import auth_pb2 as v1_dot_auth_dot_auth__pb2


class AuthServiceStub(object):
    """
    Service that provides methods for user authentication.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.login = channel.unary_unary(
                '/AuthService/login',
                request_serializer=v1_dot_auth_dot_auth__pb2.LoginRequest.SerializeToString,
                response_deserializer=v1_dot_auth_dot_auth__pb2.LoginResponse.FromString,
                )
        self.loginIntoCompany = channel.unary_unary(
                '/AuthService/loginIntoCompany',
                request_serializer=v1_dot_auth_dot_auth__pb2.CompanyLoginRequest.SerializeToString,
                response_deserializer=v1_dot_auth_dot_auth__pb2.LoginResponse.FromString,
                )
        self.loginIntoPersonalAccount = channel.unary_unary(
                '/AuthService/loginIntoPersonalAccount',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=v1_dot_auth_dot_auth__pb2.LoginResponse.FromString,
                )
        self.logout = channel.unary_unary(
                '/AuthService/logout',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class AuthServiceServicer(object):
    """
    Service that provides methods for user authentication.
    """

    def login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def loginIntoCompany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def loginIntoPersonalAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def logout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=v1_dot_auth_dot_auth__pb2.LoginRequest.FromString,
                    response_serializer=v1_dot_auth_dot_auth__pb2.LoginResponse.SerializeToString,
            ),
            'loginIntoCompany': grpc.unary_unary_rpc_method_handler(
                    servicer.loginIntoCompany,
                    request_deserializer=v1_dot_auth_dot_auth__pb2.CompanyLoginRequest.FromString,
                    response_serializer=v1_dot_auth_dot_auth__pb2.LoginResponse.SerializeToString,
            ),
            'loginIntoPersonalAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.loginIntoPersonalAccount,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=v1_dot_auth_dot_auth__pb2.LoginResponse.SerializeToString,
            ),
            'logout': grpc.unary_unary_rpc_method_handler(
                    servicer.logout,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """
    Service that provides methods for user authentication.
    """

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService/login',
            v1_dot_auth_dot_auth__pb2.LoginRequest.SerializeToString,
            v1_dot_auth_dot_auth__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def loginIntoCompany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService/loginIntoCompany',
            v1_dot_auth_dot_auth__pb2.CompanyLoginRequest.SerializeToString,
            v1_dot_auth_dot_auth__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def loginIntoPersonalAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService/loginIntoPersonalAccount',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            v1_dot_auth_dot_auth__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService/logout',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)