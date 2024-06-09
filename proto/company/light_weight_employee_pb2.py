# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/company/light-weight-employee.proto
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
  name='v1/company/light-weight-employee.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n!systems.ajax.a911.grpc.company.v1\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&v1/company/light-weight-employee.proto\x1a+systems/ajax/logging/proto/log_marker.proto\x1a\x33systems/ajax/logging/proto/formatting_options.proto\"t\n\x13LightWeightEmployee\x12\x18\n\x0b\x65mployee_id\x18\x01 \x01(\tB\x03\xf0\x44\x07\x12\x12\n\x05\x65mail\x18\x02 \x01(\tB\x03\xf8\x44\x01\x12\x17\n\nfirst_name\x18\x03 \x01(\tB\x03\xf8\x44\x01\x12\x16\n\tlast_name\x18\x04 \x01(\tB\x03\xf8\x44\x01\x42&\n!systems.ajax.a911.grpc.company.v1\xba\x02\x00\x62\x06proto3'
  ,
  dependencies=[systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2.DESCRIPTOR,systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2.DESCRIPTOR,])




_LIGHTWEIGHTEMPLOYEE = _descriptor.Descriptor(
  name='LightWeightEmployee',
  full_name='LightWeightEmployee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='employee_id', full_name='LightWeightEmployee.employee_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360D\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='LightWeightEmployee.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='LightWeightEmployee.first_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='LightWeightEmployee.last_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=140,
  serialized_end=256,
)

DESCRIPTOR.message_types_by_name['LightWeightEmployee'] = _LIGHTWEIGHTEMPLOYEE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LightWeightEmployee = _reflection.GeneratedProtocolMessageType('LightWeightEmployee', (_message.Message,), {
  'DESCRIPTOR' : _LIGHTWEIGHTEMPLOYEE,
  '__module__' : 'v1.company.light_weight_employee_pb2'
  # @@protoc_insertion_point(class_scope:LightWeightEmployee)
  })
_sym_db.RegisterMessage(LightWeightEmployee)


DESCRIPTOR._options = None
_LIGHTWEIGHTEMPLOYEE.fields_by_name['employee_id']._options = None
_LIGHTWEIGHTEMPLOYEE.fields_by_name['email']._options = None
_LIGHTWEIGHTEMPLOYEE.fields_by_name['first_name']._options = None
_LIGHTWEIGHTEMPLOYEE.fields_by_name['last_name']._options = None
# @@protoc_insertion_point(module_scope)