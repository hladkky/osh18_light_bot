# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/auth/auth-endpoints.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from v1.auth import auth_pb2 as v1_dot_auth_dot_auth__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/auth/auth-endpoints.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\036systems.ajax.a911.grpc.auth.v1\210\001\001\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cv1/auth/auth-endpoints.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x12v1/auth/auth.proto2\xed\x01\n\x0b\x41uthService\x12&\n\x05login\x12\r.LoginRequest\x1a\x0e.LoginResponse\x12\x38\n\x10loginIntoCompany\x12\x14.CompanyLoginRequest\x1a\x0e.LoginResponse\x12\x42\n\x18loginIntoPersonalAccount\x12\x16.google.protobuf.Empty\x1a\x0e.LoginResponse\x12\x38\n\x06logout\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.EmptyB&\n\x1esystems.ajax.a911.grpc.auth.v1\x88\x01\x01\xba\x02\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,v1_dot_auth_dot_auth__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_AUTHSERVICE = _descriptor.ServiceDescriptor(
  name='AuthService',
  full_name='AuthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=82,
  serialized_end=319,
  methods=[
  _descriptor.MethodDescriptor(
    name='login',
    full_name='AuthService.login',
    index=0,
    containing_service=None,
    input_type=v1_dot_auth_dot_auth__pb2._LOGINREQUEST,
    output_type=v1_dot_auth_dot_auth__pb2._LOGINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='loginIntoCompany',
    full_name='AuthService.loginIntoCompany',
    index=1,
    containing_service=None,
    input_type=v1_dot_auth_dot_auth__pb2._COMPANYLOGINREQUEST,
    output_type=v1_dot_auth_dot_auth__pb2._LOGINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='loginIntoPersonalAccount',
    full_name='AuthService.loginIntoPersonalAccount',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=v1_dot_auth_dot_auth__pb2._LOGINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='logout',
    full_name='AuthService.logout',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHSERVICE)

DESCRIPTOR.services_by_name['AuthService'] = _AUTHSERVICE

# @@protoc_insertion_point(module_scope)