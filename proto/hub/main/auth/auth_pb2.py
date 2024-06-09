# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/auth/auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.systems.ajax.logging.proto import log_marker_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2
from proto.systems.ajax.logging.proto import formatting_options_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/auth/auth.proto',
  package='systems.ajax.a911.grpc.v1.hub.main.auth',
  syntax='proto3',
  serialized_options=b'\n#systems.ajax.a911.grpc.v1.main.authP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bv1/hub/main/auth/auth.proto\x12\'systems.ajax.a911.grpc.v1.hub.main.auth\x1a+systems/ajax/logging/proto/log_marker.proto\x1a\x33systems/ajax/logging/proto/formatting_options.proto\"\x7f\n\x0cLoginRequest\x12\x12\n\x05login\x18\x01 \x01(\tB\x03\xf8\x44\x01\x12\x15\n\x08password\x18\x02 \x01(\tB\x03\xf8\x44\x01\x12\x44\n\tuser_role\x18\x03 \x01(\x0e\x32\x31.systems.ajax.a911.grpc.v1.hub.main.auth.UserRole\"\xcb\x01\n\rLoginResponse\x12\x14\n\x07user_id\x18\x01 \x01(\tB\x03\xf0\x44\x06\x12\x44\n\tuser_role\x18\x02 \x01(\x0e\x32\x31.systems.ajax.a911.grpc.v1.hub.main.auth.UserRole\x12\x12\n\x05\x65mail\x18\x03 \x01(\tB\x03\xf8\x44\x01\x12\x17\n\nfirst_name\x18\x04 \x01(\tB\x03\xf8\x44\x01\x12\x16\n\tlast_name\x18\x05 \x01(\tB\x03\xf8\x44\x01\x12\x19\n\x0cphone_number\x18\x06 \x01(\tB\x03\xf8\x44\x01**\n\x08UserRole\x12\x08\n\x04USER\x10\x00\x12\x07\n\x03PRO\x10\x01\x12\x0b\n\x07\x43OMPANY\x10\x02\x42\x31\n#systems.ajax.a911.grpc.v1.main.authP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2.DESCRIPTOR,systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2.DESCRIPTOR,])

_USERROLE = _descriptor.EnumDescriptor(
  name='UserRole',
  full_name='systems.ajax.a911.grpc.v1.hub.main.auth.UserRole',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRO', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPANY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=505,
  serialized_end=547,
)
_sym_db.RegisterEnumDescriptor(_USERROLE)

UserRole = enum_type_wrapper.EnumTypeWrapper(_USERROLE)
USER = 0
PRO = 1
COMPANY = 2



_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginRequest.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_role', full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginRequest.user_role', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=170,
  serialized_end=297,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginResponse.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360D\006', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_role', full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginResponse.user_role', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginResponse.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginResponse.first_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginResponse.last_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='systems.ajax.a911.grpc.v1.hub.main.auth.LoginResponse.phone_number', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=300,
  serialized_end=503,
)

_LOGINREQUEST.fields_by_name['user_role'].enum_type = _USERROLE
_LOGINRESPONSE.fields_by_name['user_role'].enum_type = _USERROLE
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.enum_types_by_name['UserRole'] = _USERROLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'v1.hub.main.auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.auth.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'v1.hub.main.auth.auth_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.auth.LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)


DESCRIPTOR._options = None
_LOGINREQUEST.fields_by_name['login']._options = None
_LOGINREQUEST.fields_by_name['password']._options = None
_LOGINRESPONSE.fields_by_name['user_id']._options = None
_LOGINRESPONSE.fields_by_name['email']._options = None
_LOGINRESPONSE.fields_by_name['first_name']._options = None
_LOGINRESPONSE.fields_by_name['last_name']._options = None
_LOGINRESPONSE.fields_by_name['phone_number']._options = None
# @@protoc_insertion_point(module_scope)