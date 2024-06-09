# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/facility/light-weight-facility.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.mobile.facility import facility_monitoring_status_pb2 as v1_dot_mobile_dot_facility_dot_facility__monitoring__status__pb2
from proto.systems.ajax.logging.proto import log_marker_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/facility/light-weight-facility.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\"systems.ajax.a911.grpc.facility.v1\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'v1/facility/light-weight-facility.proto\x1a\x33v1/mobile/facility/facility-monitoring-status.proto\x1a+systems/ajax/logging/proto/log_marker.proto\"\xa6\x06\n\x13LightWeightFacility\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x13\n\x0b\x66\x61\x63ility_id\x18\x02 \x01(\t\x12\x18\n\x06hub_id\x18\x03 \x01(\tB\x03\xf0\x44\x05H\x00\x88\x01\x01\x12\x15\n\x08space_id\x18\t \x01(\tB\x03\xf0\x44\x02\x12\x36\n\x0cgeneral_info\x18\x04 \x01(\x0b\x32 .LightWeightFacility.GeneralInfo\x12@\n\x11\x63onnection_status\x18\x05 \x01(\x0e\x32%.LightWeightFacility.ConnectionStatus\x12\x38\n\raccess_rights\x18\x06 \x01(\x0b\x32!.LightWeightFacility.AccessRights\x12/\n\x06status\x18\x07 \x01(\x0e\x32\x1b.LightWeightFacility.StatusB\x02\x18\x01\x12V\n\x11monitoring_status\x18\x08 \x01(\x0e\x32;.systems.ajax.a911.grpc.v1.mobile.facility.MonitoringStatus\x1aI\n\x0bGeneralInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x1b\n\x13registration_number\x18\x03 \x01(\t\x1a\xa2\x01\n\x0c\x41\x63\x63\x65ssRights\x12\x1a\n\x12\x65xpiration_seconds\x18\x01 \x01(\x03\x12\x41\n\x0b\x61\x63\x63\x65ss_type\x18\x02 \x01(\x0e\x32,.LightWeightFacility.AccessRights.AccessType\"3\n\nAccessType\x12\x0b\n\x07\x45XPIRED\x10\x00\x12\r\n\tPERMANENT\x10\x01\x12\t\n\x05VALID\x10\x02\"+\n\x10\x43onnectionStatus\x12\x0b\n\x07OFFLINE\x10\x00\x12\n\n\x06ONLINE\x10\x01\"N\n\x06Status\x12\x17\n\x13MONITORING_APPROVED\x10\x00\x12\x18\n\x14MONITORING_REQUESTED\x10\x01\x12\x11\n\rIN_SLEEP_MODE\x10\x02\x42\t\n\x07_hub_id\"X\n SearchLightWeightFacilityRequest\x12\x15\n\rsearch_phrase\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\r\x12\x0e\n\x06offset\x18\x03 \x01(\x04\"h\n\x1bLightWeightFacilityResponse\x12(\n\nfacilities\x18\x01 \x03(\x0b\x32\x14.LightWeightFacility\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0f\n\x07\x63ounter\x18\x03 \x01(\x04\x42\'\n\"systems.ajax.a911.grpc.facility.v1\xba\x02\x00\x62\x06proto3'
  ,
  dependencies=[v1_dot_mobile_dot_facility_dot_facility__monitoring__status__pb2.DESCRIPTOR,systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2.DESCRIPTOR,])



_LIGHTWEIGHTFACILITY_ACCESSRIGHTS_ACCESSTYPE = _descriptor.EnumDescriptor(
  name='AccessType',
  full_name='LightWeightFacility.AccessRights.AccessType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXPIRED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PERMANENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VALID', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=761,
  serialized_end=812,
)
_sym_db.RegisterEnumDescriptor(_LIGHTWEIGHTFACILITY_ACCESSRIGHTS_ACCESSTYPE)

_LIGHTWEIGHTFACILITY_CONNECTIONSTATUS = _descriptor.EnumDescriptor(
  name='ConnectionStatus',
  full_name='LightWeightFacility.ConnectionStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OFFLINE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONLINE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=814,
  serialized_end=857,
)
_sym_db.RegisterEnumDescriptor(_LIGHTWEIGHTFACILITY_CONNECTIONSTATUS)

_LIGHTWEIGHTFACILITY_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='LightWeightFacility.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MONITORING_APPROVED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MONITORING_REQUESTED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN_SLEEP_MODE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=859,
  serialized_end=937,
)
_sym_db.RegisterEnumDescriptor(_LIGHTWEIGHTFACILITY_STATUS)


_LIGHTWEIGHTFACILITY_GENERALINFO = _descriptor.Descriptor(
  name='GeneralInfo',
  full_name='LightWeightFacility.GeneralInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='LightWeightFacility.GeneralInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='LightWeightFacility.GeneralInfo.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registration_number', full_name='LightWeightFacility.GeneralInfo.registration_number', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=574,
  serialized_end=647,
)

_LIGHTWEIGHTFACILITY_ACCESSRIGHTS = _descriptor.Descriptor(
  name='AccessRights',
  full_name='LightWeightFacility.AccessRights',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='expiration_seconds', full_name='LightWeightFacility.AccessRights.expiration_seconds', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_type', full_name='LightWeightFacility.AccessRights.access_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LIGHTWEIGHTFACILITY_ACCESSRIGHTS_ACCESSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=650,
  serialized_end=812,
)

_LIGHTWEIGHTFACILITY = _descriptor.Descriptor(
  name='LightWeightFacility',
  full_name='LightWeightFacility',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_name', full_name='LightWeightFacility.display_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='facility_id', full_name='LightWeightFacility.facility_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hub_id', full_name='LightWeightFacility.hub_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360D\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='space_id', full_name='LightWeightFacility.space_id', index=3,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360D\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='general_info', full_name='LightWeightFacility.general_info', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_status', full_name='LightWeightFacility.connection_status', index=5,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_rights', full_name='LightWeightFacility.access_rights', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='LightWeightFacility.status', index=7,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monitoring_status', full_name='LightWeightFacility.monitoring_status', index=8,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LIGHTWEIGHTFACILITY_GENERALINFO, _LIGHTWEIGHTFACILITY_ACCESSRIGHTS, ],
  enum_types=[
    _LIGHTWEIGHTFACILITY_CONNECTIONSTATUS,
    _LIGHTWEIGHTFACILITY_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_hub_id', full_name='LightWeightFacility._hub_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=142,
  serialized_end=948,
)


_SEARCHLIGHTWEIGHTFACILITYREQUEST = _descriptor.Descriptor(
  name='SearchLightWeightFacilityRequest',
  full_name='SearchLightWeightFacilityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='search_phrase', full_name='SearchLightWeightFacilityRequest.search_phrase', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='SearchLightWeightFacilityRequest.limit', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='SearchLightWeightFacilityRequest.offset', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=950,
  serialized_end=1038,
)


_LIGHTWEIGHTFACILITYRESPONSE = _descriptor.Descriptor(
  name='LightWeightFacilityResponse',
  full_name='LightWeightFacilityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='facilities', full_name='LightWeightFacilityResponse.facilities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='LightWeightFacilityResponse.offset', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counter', full_name='LightWeightFacilityResponse.counter', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1040,
  serialized_end=1144,
)

_LIGHTWEIGHTFACILITY_GENERALINFO.containing_type = _LIGHTWEIGHTFACILITY
_LIGHTWEIGHTFACILITY_ACCESSRIGHTS.fields_by_name['access_type'].enum_type = _LIGHTWEIGHTFACILITY_ACCESSRIGHTS_ACCESSTYPE
_LIGHTWEIGHTFACILITY_ACCESSRIGHTS.containing_type = _LIGHTWEIGHTFACILITY
_LIGHTWEIGHTFACILITY_ACCESSRIGHTS_ACCESSTYPE.containing_type = _LIGHTWEIGHTFACILITY_ACCESSRIGHTS
_LIGHTWEIGHTFACILITY.fields_by_name['general_info'].message_type = _LIGHTWEIGHTFACILITY_GENERALINFO
_LIGHTWEIGHTFACILITY.fields_by_name['connection_status'].enum_type = _LIGHTWEIGHTFACILITY_CONNECTIONSTATUS
_LIGHTWEIGHTFACILITY.fields_by_name['access_rights'].message_type = _LIGHTWEIGHTFACILITY_ACCESSRIGHTS
_LIGHTWEIGHTFACILITY.fields_by_name['status'].enum_type = _LIGHTWEIGHTFACILITY_STATUS
_LIGHTWEIGHTFACILITY.fields_by_name['monitoring_status'].enum_type = v1_dot_mobile_dot_facility_dot_facility__monitoring__status__pb2._MONITORINGSTATUS
_LIGHTWEIGHTFACILITY_CONNECTIONSTATUS.containing_type = _LIGHTWEIGHTFACILITY
_LIGHTWEIGHTFACILITY_STATUS.containing_type = _LIGHTWEIGHTFACILITY
_LIGHTWEIGHTFACILITY.oneofs_by_name['_hub_id'].fields.append(
  _LIGHTWEIGHTFACILITY.fields_by_name['hub_id'])
_LIGHTWEIGHTFACILITY.fields_by_name['hub_id'].containing_oneof = _LIGHTWEIGHTFACILITY.oneofs_by_name['_hub_id']
_LIGHTWEIGHTFACILITYRESPONSE.fields_by_name['facilities'].message_type = _LIGHTWEIGHTFACILITY
DESCRIPTOR.message_types_by_name['LightWeightFacility'] = _LIGHTWEIGHTFACILITY
DESCRIPTOR.message_types_by_name['SearchLightWeightFacilityRequest'] = _SEARCHLIGHTWEIGHTFACILITYREQUEST
DESCRIPTOR.message_types_by_name['LightWeightFacilityResponse'] = _LIGHTWEIGHTFACILITYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LightWeightFacility = _reflection.GeneratedProtocolMessageType('LightWeightFacility', (_message.Message,), {

  'GeneralInfo' : _reflection.GeneratedProtocolMessageType('GeneralInfo', (_message.Message,), {
    'DESCRIPTOR' : _LIGHTWEIGHTFACILITY_GENERALINFO,
    '__module__' : 'v1.facility.light_weight_facility_pb2'
    # @@protoc_insertion_point(class_scope:LightWeightFacility.GeneralInfo)
    })
  ,

  'AccessRights' : _reflection.GeneratedProtocolMessageType('AccessRights', (_message.Message,), {
    'DESCRIPTOR' : _LIGHTWEIGHTFACILITY_ACCESSRIGHTS,
    '__module__' : 'v1.facility.light_weight_facility_pb2'
    # @@protoc_insertion_point(class_scope:LightWeightFacility.AccessRights)
    })
  ,
  'DESCRIPTOR' : _LIGHTWEIGHTFACILITY,
  '__module__' : 'v1.facility.light_weight_facility_pb2'
  # @@protoc_insertion_point(class_scope:LightWeightFacility)
  })
_sym_db.RegisterMessage(LightWeightFacility)
_sym_db.RegisterMessage(LightWeightFacility.GeneralInfo)
_sym_db.RegisterMessage(LightWeightFacility.AccessRights)

SearchLightWeightFacilityRequest = _reflection.GeneratedProtocolMessageType('SearchLightWeightFacilityRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHLIGHTWEIGHTFACILITYREQUEST,
  '__module__' : 'v1.facility.light_weight_facility_pb2'
  # @@protoc_insertion_point(class_scope:SearchLightWeightFacilityRequest)
  })
_sym_db.RegisterMessage(SearchLightWeightFacilityRequest)

LightWeightFacilityResponse = _reflection.GeneratedProtocolMessageType('LightWeightFacilityResponse', (_message.Message,), {
  'DESCRIPTOR' : _LIGHTWEIGHTFACILITYRESPONSE,
  '__module__' : 'v1.facility.light_weight_facility_pb2'
  # @@protoc_insertion_point(class_scope:LightWeightFacilityResponse)
  })
_sym_db.RegisterMessage(LightWeightFacilityResponse)


DESCRIPTOR._options = None
_LIGHTWEIGHTFACILITY.fields_by_name['hub_id']._options = None
_LIGHTWEIGHTFACILITY.fields_by_name['space_id']._options = None
_LIGHTWEIGHTFACILITY.fields_by_name['status']._options = None
# @@protoc_insertion_point(module_scope)