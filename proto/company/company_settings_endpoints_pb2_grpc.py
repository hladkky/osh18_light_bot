# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto.v1.company import company_settings_pb2 as v1_dot_company_dot_company__settings__pb2


class CompanySettingsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getCompanySettings = channel.unary_unary(
                '/CompanySettingsService/getCompanySettings',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
                )
        self.updateCompanyIncidentSettings = channel.unary_unary(
                '/CompanySettingsService/updateCompanyIncidentSettings',
                request_serializer=v1_dot_company_dot_company__settings__pb2.IncidentGenerationSettings.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
                )
        self.updateHubEventGeneratingIncidentSettings = channel.unary_unary(
                '/CompanySettingsService/updateHubEventGeneratingIncidentSettings',
                request_serializer=v1_dot_company_dot_company__settings__pb2.HubEventGeneratingIncidentSettings.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
                )
        self.updateCompanyGlobalFacilityPermissionSettings = channel.unary_unary(
                '/CompanySettingsService/updateCompanyGlobalFacilityPermissionSettings',
                request_serializer=v1_dot_company_dot_company__settings__pb2.GlobalFacilityPermissionSettings.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
                )
        self.updateCompanyQrUsageSettings = channel.unary_unary(
                '/CompanySettingsService/updateCompanyQrUsageSettings',
                request_serializer=v1_dot_company_dot_company__settings__pb2.QrUsageSettings.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
                )
        self.updateCompanyMaintenanceReportSettings = channel.unary_unary(
                '/CompanySettingsService/updateCompanyMaintenanceReportSettings',
                request_serializer=v1_dot_company_dot_company__settings__pb2.MaintenanceReportSettings.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
                )
        self.getCompanySurveillanceMediaSettings = channel.unary_unary(
                '/CompanySettingsService/getCompanySurveillanceMediaSettings',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.SurveillanceMediaSettings.FromString,
                )
        self.updateCompanySurveillanceMediaSettings = channel.unary_unary(
                '/CompanySettingsService/updateCompanySurveillanceMediaSettings',
                request_serializer=v1_dot_company_dot_company__settings__pb2.SurveillanceMediaSettings.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.SurveillanceMediaSettings.FromString,
                )
        self.updateMonitoringSettings = channel.unary_unary(
                '/CompanySettingsService/updateMonitoringSettings',
                request_serializer=v1_dot_company_dot_company__settings__pb2.MonitoringSettings.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
                )
        self.updateAccountNumberSettings = channel.unary_unary(
                '/CompanySettingsService/updateAccountNumberSettings',
                request_serializer=v1_dot_company_dot_company__settings__pb2.AccountNumberSettings.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
                )
        self.updateAccessConfirmationSettings = channel.unary_unary(
                '/CompanySettingsService/updateAccessConfirmationSettings',
                request_serializer=v1_dot_company_dot_company__settings__pb2.AccessConfirmationSettings.SerializeToString,
                response_deserializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
                )


class CompanySettingsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getCompanySettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateCompanyIncidentSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateHubEventGeneratingIncidentSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateCompanyGlobalFacilityPermissionSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateCompanyQrUsageSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateCompanyMaintenanceReportSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCompanySurveillanceMediaSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateCompanySurveillanceMediaSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateMonitoringSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateAccountNumberSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateAccessConfirmationSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CompanySettingsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getCompanySettings': grpc.unary_unary_rpc_method_handler(
                    servicer.getCompanySettings,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.SerializeToString,
            ),
            'updateCompanyIncidentSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.updateCompanyIncidentSettings,
                    request_deserializer=v1_dot_company_dot_company__settings__pb2.IncidentGenerationSettings.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.SerializeToString,
            ),
            'updateHubEventGeneratingIncidentSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.updateHubEventGeneratingIncidentSettings,
                    request_deserializer=v1_dot_company_dot_company__settings__pb2.HubEventGeneratingIncidentSettings.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.SerializeToString,
            ),
            'updateCompanyGlobalFacilityPermissionSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.updateCompanyGlobalFacilityPermissionSettings,
                    request_deserializer=v1_dot_company_dot_company__settings__pb2.GlobalFacilityPermissionSettings.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.SerializeToString,
            ),
            'updateCompanyQrUsageSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.updateCompanyQrUsageSettings,
                    request_deserializer=v1_dot_company_dot_company__settings__pb2.QrUsageSettings.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.SerializeToString,
            ),
            'updateCompanyMaintenanceReportSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.updateCompanyMaintenanceReportSettings,
                    request_deserializer=v1_dot_company_dot_company__settings__pb2.MaintenanceReportSettings.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.SerializeToString,
            ),
            'getCompanySurveillanceMediaSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.getCompanySurveillanceMediaSettings,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.SurveillanceMediaSettings.SerializeToString,
            ),
            'updateCompanySurveillanceMediaSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.updateCompanySurveillanceMediaSettings,
                    request_deserializer=v1_dot_company_dot_company__settings__pb2.SurveillanceMediaSettings.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.SurveillanceMediaSettings.SerializeToString,
            ),
            'updateMonitoringSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.updateMonitoringSettings,
                    request_deserializer=v1_dot_company_dot_company__settings__pb2.MonitoringSettings.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.SerializeToString,
            ),
            'updateAccountNumberSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.updateAccountNumberSettings,
                    request_deserializer=v1_dot_company_dot_company__settings__pb2.AccountNumberSettings.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.SerializeToString,
            ),
            'updateAccessConfirmationSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.updateAccessConfirmationSettings,
                    request_deserializer=v1_dot_company_dot_company__settings__pb2.AccessConfirmationSettings.FromString,
                    response_serializer=v1_dot_company_dot_company__settings__pb2.CompanySettings.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CompanySettingsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CompanySettingsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getCompanySettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/getCompanySettings',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateCompanyIncidentSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/updateCompanyIncidentSettings',
            v1_dot_company_dot_company__settings__pb2.IncidentGenerationSettings.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateHubEventGeneratingIncidentSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/updateHubEventGeneratingIncidentSettings',
            v1_dot_company_dot_company__settings__pb2.HubEventGeneratingIncidentSettings.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateCompanyGlobalFacilityPermissionSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/updateCompanyGlobalFacilityPermissionSettings',
            v1_dot_company_dot_company__settings__pb2.GlobalFacilityPermissionSettings.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateCompanyQrUsageSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/updateCompanyQrUsageSettings',
            v1_dot_company_dot_company__settings__pb2.QrUsageSettings.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateCompanyMaintenanceReportSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/updateCompanyMaintenanceReportSettings',
            v1_dot_company_dot_company__settings__pb2.MaintenanceReportSettings.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getCompanySurveillanceMediaSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/getCompanySurveillanceMediaSettings',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.SurveillanceMediaSettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateCompanySurveillanceMediaSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/updateCompanySurveillanceMediaSettings',
            v1_dot_company_dot_company__settings__pb2.SurveillanceMediaSettings.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.SurveillanceMediaSettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateMonitoringSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/updateMonitoringSettings',
            v1_dot_company_dot_company__settings__pb2.MonitoringSettings.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateAccountNumberSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/updateAccountNumberSettings',
            v1_dot_company_dot_company__settings__pb2.AccountNumberSettings.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateAccessConfirmationSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CompanySettingsService/updateAccessConfirmationSettings',
            v1_dot_company_dot_company__settings__pb2.AccessConfirmationSettings.SerializeToString,
            v1_dot_company_dot_company__settings__pb2.CompanySettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
