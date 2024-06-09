# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/additional/data/endpoint_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/additional/data/endpoint_info.proto',
  package='systems.ajax.a911.grpc.v1.hub.main.additional.data',
  syntax='proto3',
  serialized_options=b'\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/v1/hub/main/additional/data/endpoint_info.proto\x12\x32systems.ajax.a911.grpc.v1.hub.main.additional.data\"\x8e\x05\n\x0c\x45ndpointInfo\x12Y\n\x06target\x18\x01 \x01(\x0e\x32I.systems.ajax.a911.grpc.v1.hub.main.additional.data.EndpointInfo.Endpoint\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x94\x04\n\x08\x45ndpoint\x12\x18\n\x14\x45NDPOINT_UNSPECIFIED\x10\x00\x12\"\n\x1e\x45NDPOINT_LIGHT_SWITCH_BUTTON_1\x10\x01\x12\"\n\x1e\x45NDPOINT_LIGHT_SWITCH_BUTTON_2\x10\x02\x12\x30\n,ENDPOINT_FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_1\x10\x03\x12\x30\n,ENDPOINT_FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_2\x10\x04\x12\x30\n,ENDPOINT_FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_3\x10\x05\x12\x30\n,ENDPOINT_FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_4\x10\x06\x12\x36\n2ENDPOINT_TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_1\x10\x07\x12\x36\n2ENDPOINT_TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_2\x10\x08\x12\x36\n2ENDPOINT_TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_3\x10\t\x12\x36\n2ENDPOINT_TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_4\x10\nB6\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\x01\x62\x06proto3'
)



_ENDPOINTINFO_ENDPOINT = _descriptor.EnumDescriptor(
  name='Endpoint',
  full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.EndpointInfo.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_LIGHT_SWITCH_BUTTON_1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_LIGHT_SWITCH_BUTTON_2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_1', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_2', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_3', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_4', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_1', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_2', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_3', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_4', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=226,
  serialized_end=758,
)
_sym_db.RegisterEnumDescriptor(_ENDPOINTINFO_ENDPOINT)


_ENDPOINTINFO = _descriptor.Descriptor(
  name='EndpointInfo',
  full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.EndpointInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.EndpointInfo.target', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.EndpointInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENDPOINTINFO_ENDPOINT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=758,
)

_ENDPOINTINFO.fields_by_name['target'].enum_type = _ENDPOINTINFO_ENDPOINT
_ENDPOINTINFO_ENDPOINT.containing_type = _ENDPOINTINFO
DESCRIPTOR.message_types_by_name['EndpointInfo'] = _ENDPOINTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EndpointInfo = _reflection.GeneratedProtocolMessageType('EndpointInfo', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTINFO,
  '__module__' : 'v1.hub.main.additional.data.endpoint_info_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.additional.data.EndpointInfo)
  })
_sym_db.RegisterMessage(EndpointInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)