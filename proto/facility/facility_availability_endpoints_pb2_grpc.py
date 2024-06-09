# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto.facility import facility_availability_endpoints_pb2 as v1_dot_facility_dot_facility__availability__endpoints__pb2


class FacilityAvailabilityServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getFacilitiesAvailabilityPercent = channel.unary_unary(
                '/FacilityAvailabilityService/getFacilitiesAvailabilityPercent',
                request_serializer=v1_dot_facility_dot_facility__availability__endpoints__pb2.FacilityAvailabilityRequest.SerializeToString,
                response_deserializer=v1_dot_facility_dot_facility__availability__endpoints__pb2.FacilityAvailabilityResponse.FromString,
                )


class FacilityAvailabilityServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getFacilitiesAvailabilityPercent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FacilityAvailabilityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getFacilitiesAvailabilityPercent': grpc.unary_unary_rpc_method_handler(
                    servicer.getFacilitiesAvailabilityPercent,
                    request_deserializer=v1_dot_facility_dot_facility__availability__endpoints__pb2.FacilityAvailabilityRequest.FromString,
                    response_serializer=v1_dot_facility_dot_facility__availability__endpoints__pb2.FacilityAvailabilityResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FacilityAvailabilityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FacilityAvailabilityService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getFacilitiesAvailabilityPercent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FacilityAvailabilityService/getFacilitiesAvailabilityPercent',
            v1_dot_facility_dot_facility__availability__endpoints__pb2.FacilityAvailabilityRequest.SerializeToString,
            v1_dot_facility_dot_facility__availability__endpoints__pb2.FacilityAvailabilityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
