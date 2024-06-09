# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/hub_access_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.systems.ajax.logging.proto import log_marker_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2
from proto.systems.ajax.logging.proto import formatting_options_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/hub_access_response.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\036systems.ajax.a911.grpc.v1.mainP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%v1/hub/main/hub_access_response.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a+systems/ajax/logging/proto/log_marker.proto\x1a\x33systems/ajax/logging/proto/formatting_options.proto\"\xa7\x01\n\x11HubAccessResponse\x12\x18\n\nprofi_mail\x18\xe8\x07 \x01(\tB\x03\xf8\x44\x01\x12\x15\n\x07user_id\x18\xe9\x07 \x01(\tB\x03\xf0\x44\x06\x12\x16\n\x08pro_name\x18\xea\x07 \x01(\tB\x03\xf8\x44\x01\x12\x15\n\x0c\x61\x63\x63\x65ss_level\x18\x93N \x01(\x05\x12\x14\n\x0b\x61\x63\x63\x65ss_time\x18\xec\x07 \x01(\x05\x12\x1c\n\x13is_request_declined\x18\xed\x07 \x01(\x08\x42,\n\x1esystems.ajax.a911.grpc.v1.mainP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2.DESCRIPTOR,systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2.DESCRIPTOR,])




_HUBACCESSRESPONSE = _descriptor.Descriptor(
  name='HubAccessResponse',
  full_name='systems.ajax.a911.grpc.v1.hub.main.HubAccessResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='profi_mail', full_name='systems.ajax.a911.grpc.v1.hub.main.HubAccessResponse.profi_mail', index=0,
      number=1000, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='systems.ajax.a911.grpc.v1.hub.main.HubAccessResponse.user_id', index=1,
      number=1001, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360D\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pro_name', full_name='systems.ajax.a911.grpc.v1.hub.main.HubAccessResponse.pro_name', index=2,
      number=1002, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_level', full_name='systems.ajax.a911.grpc.v1.hub.main.HubAccessResponse.access_level', index=3,
      number=10003, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_time', full_name='systems.ajax.a911.grpc.v1.hub.main.HubAccessResponse.access_time', index=4,
      number=1004, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_request_declined', full_name='systems.ajax.a911.grpc.v1.hub.main.HubAccessResponse.is_request_declined', index=5,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=176,
  serialized_end=343,
)

DESCRIPTOR.message_types_by_name['HubAccessResponse'] = _HUBACCESSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HubAccessResponse = _reflection.GeneratedProtocolMessageType('HubAccessResponse', (_message.Message,), {
  'DESCRIPTOR' : _HUBACCESSRESPONSE,
  '__module__' : 'v1.hub.main.hub_access_response_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.HubAccessResponse)
  })
_sym_db.RegisterMessage(HubAccessResponse)


DESCRIPTOR._options = None
_HUBACCESSRESPONSE.fields_by_name['profi_mail']._options = None
_HUBACCESSRESPONSE.fields_by_name['user_id']._options = None
_HUBACCESSRESPONSE.fields_by_name['pro_name']._options = None
# @@protoc_insertion_point(module_scope)
