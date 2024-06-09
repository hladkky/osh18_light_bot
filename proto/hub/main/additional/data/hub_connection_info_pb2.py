# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/additional/data/hub_connection_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/additional/data/hub_connection_info.proto',
  package='systems.ajax.a911.grpc.v1.hub.main.additional.data',
  syntax='proto3',
  serialized_options=b'\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5v1/hub/main/additional/data/hub_connection_info.proto\x12\x32systems.ajax.a911.grpc.v1.hub.main.additional.data\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc9\x02\n\x11HubConnectionInfo\x12\x36\n\x12original_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12x\n\x15hub_connection_status\x18\x02 \x01(\x0e\x32Y.systems.ajax.a911.grpc.v1.hub.main.additional.data.HubConnectionInfo.HubConnectionStatus\"\x81\x01\n\x13HubConnectionStatus\x12%\n!HUB_CONNECTION_STATUS_UNSPECIFIED\x10\x00\x12 \n\x1cHUB_CONNECTION_STATUS_ONLINE\x10\x01\x12!\n\x1dHUB_CONNECTION_STATUS_OFFLINE\x10\x02\x42\x36\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_HUBCONNECTIONINFO_HUBCONNECTIONSTATUS = _descriptor.EnumDescriptor(
  name='HubConnectionStatus',
  full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.HubConnectionInfo.HubConnectionStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HUB_CONNECTION_STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HUB_CONNECTION_STATUS_ONLINE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HUB_CONNECTION_STATUS_OFFLINE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=343,
  serialized_end=472,
)
_sym_db.RegisterEnumDescriptor(_HUBCONNECTIONINFO_HUBCONNECTIONSTATUS)


_HUBCONNECTIONINFO = _descriptor.Descriptor(
  name='HubConnectionInfo',
  full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.HubConnectionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_timestamp', full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.HubConnectionInfo.original_timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hub_connection_status', full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.HubConnectionInfo.hub_connection_status', index=1,
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
    _HUBCONNECTIONINFO_HUBCONNECTIONSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=472,
)

_HUBCONNECTIONINFO.fields_by_name['original_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HUBCONNECTIONINFO.fields_by_name['hub_connection_status'].enum_type = _HUBCONNECTIONINFO_HUBCONNECTIONSTATUS
_HUBCONNECTIONINFO_HUBCONNECTIONSTATUS.containing_type = _HUBCONNECTIONINFO
DESCRIPTOR.message_types_by_name['HubConnectionInfo'] = _HUBCONNECTIONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HubConnectionInfo = _reflection.GeneratedProtocolMessageType('HubConnectionInfo', (_message.Message,), {
  'DESCRIPTOR' : _HUBCONNECTIONINFO,
  '__module__' : 'v1.hub.main.additional.data.hub_connection_info_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.additional.data.HubConnectionInfo)
  })
_sym_db.RegisterMessage(HubConnectionInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
