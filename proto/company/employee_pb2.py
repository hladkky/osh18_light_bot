# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/company/employee.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.systems.ajax.logging.proto import formatting_options_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/company/employee.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n!systems.ajax.a911.grpc.company.v1P\001\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19v1/company/employee.proto\x1a\x33systems/ajax/logging/proto/formatting_options.proto\"\xc1\x05\n\x08\x45mployee\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x04\x12\x12\n\x05\x65mail\x18\x03 \x01(\tB\x03\xf8\x44\x01\x12,\n\rphone_numbers\x18\x04 \x03(\x0b\x32\x15.Employee.PhoneNumber\x12\x17\n\nfirst_name\x18\x05 \x01(\tB\x03\xf8\x44\x01\x12\x16\n\tlast_name\x18\x06 \x01(\tB\x03\xf8\x44\x01\x12\x10\n\x08photo_id\x18\x07 \x01(\t\x12#\n\x04role\x18\x08 \x01(\x0b\x32\x15.Employee.ComplexRole\x12 \n\x06status\x18\t \x01(\x0e\x32\x10.Employee.Status\x12\x0f\n\x07\x64\x65leted\x18\n \x01(\x08\x1an\n\x0bPhoneNumber\x12\x13\n\x06number\x18\x01 \x01(\tB\x03\xf8\x44\x01\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x1a.Employee.PhoneNumber.Type\" \n\x04Type\x12\x08\n\x04MAIN\x10\x00\x12\x0e\n\nADDITIONAL\x10\x01\x1a,\n\x0b\x43omplexRole\x12\x1d\n\x05roles\x18\x01 \x03(\x0e\x32\x0e.Employee.Role\"\xdc\x01\n\x04Role\x12\t\n\x05OWNER\x10\x00\x12\x17\n\x13SENIOR_CMS_ENGINEER\x10\x01\x12\x10\n\x0c\x43MS_ENGINEER\x10\x02\x12\x16\n\x12HEAD_OF_INSTALLERS\x10\x03\x12\r\n\tINSTALLER\x10\x04\x12\x15\n\x11HEAD_OF_OPERATORS\x10\x05\x12\x0c\n\x08OPERATOR\x10\x06\x12\x17\n\x13RAPID_RESPONSE_TEAM\x10\x07\x12\x18\n\x14SUBSCRIPTION_MANAGER\x10\x08\x12\x1f\n\x1bSENIOR_SUBSCRIPTION_MANAGER\x10\t\">\n\x06Status\x12\x0b\n\x07PENDING\x10\x00\x12\r\n\tCANCELLED\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02\x12\n\n\x06\x41\x43TIVE\x10\x03\x42(\n!systems.ajax.a911.grpc.company.v1P\x01\xba\x02\x00\x62\x06proto3'
  ,
  dependencies=[systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2.DESCRIPTOR,])



_EMPLOYEE_PHONENUMBER_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Employee.PhoneNumber.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MAIN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADDITIONAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=423,
  serialized_end=455,
)
_sym_db.RegisterEnumDescriptor(_EMPLOYEE_PHONENUMBER_TYPE)

_EMPLOYEE_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='Employee.Role',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OWNER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENIOR_CMS_ENGINEER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMS_ENGINEER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HEAD_OF_INSTALLERS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSTALLER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HEAD_OF_OPERATORS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RAPID_RESPONSE_TEAM', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIPTION_MANAGER', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENIOR_SUBSCRIPTION_MANAGER', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=504,
  serialized_end=724,
)
_sym_db.RegisterEnumDescriptor(_EMPLOYEE_ROLE)

_EMPLOYEE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Employee.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INACTIVE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=726,
  serialized_end=788,
)
_sym_db.RegisterEnumDescriptor(_EMPLOYEE_STATUS)


_EMPLOYEE_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='Employee.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='Employee.PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Employee.PhoneNumber.type', index=1,
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
    _EMPLOYEE_PHONENUMBER_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=455,
)

_EMPLOYEE_COMPLEXROLE = _descriptor.Descriptor(
  name='ComplexRole',
  full_name='Employee.ComplexRole',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roles', full_name='Employee.ComplexRole.roles', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=457,
  serialized_end=501,
)

_EMPLOYEE = _descriptor.Descriptor(
  name='Employee',
  full_name='Employee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Employee.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='Employee.version', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='Employee.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_numbers', full_name='Employee.phone_numbers', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='Employee.first_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='Employee.last_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='photo_id', full_name='Employee.photo_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='Employee.role', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='Employee.status', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='Employee.deleted', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EMPLOYEE_PHONENUMBER, _EMPLOYEE_COMPLEXROLE, ],
  enum_types=[
    _EMPLOYEE_ROLE,
    _EMPLOYEE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=788,
)

_EMPLOYEE_PHONENUMBER.fields_by_name['type'].enum_type = _EMPLOYEE_PHONENUMBER_TYPE
_EMPLOYEE_PHONENUMBER.containing_type = _EMPLOYEE
_EMPLOYEE_PHONENUMBER_TYPE.containing_type = _EMPLOYEE_PHONENUMBER
_EMPLOYEE_COMPLEXROLE.fields_by_name['roles'].enum_type = _EMPLOYEE_ROLE
_EMPLOYEE_COMPLEXROLE.containing_type = _EMPLOYEE
_EMPLOYEE.fields_by_name['phone_numbers'].message_type = _EMPLOYEE_PHONENUMBER
_EMPLOYEE.fields_by_name['role'].message_type = _EMPLOYEE_COMPLEXROLE
_EMPLOYEE.fields_by_name['status'].enum_type = _EMPLOYEE_STATUS
_EMPLOYEE_ROLE.containing_type = _EMPLOYEE
_EMPLOYEE_STATUS.containing_type = _EMPLOYEE
DESCRIPTOR.message_types_by_name['Employee'] = _EMPLOYEE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Employee = _reflection.GeneratedProtocolMessageType('Employee', (_message.Message,), {

  'PhoneNumber' : _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), {
    'DESCRIPTOR' : _EMPLOYEE_PHONENUMBER,
    '__module__' : 'v1.company.employee_pb2'
    # @@protoc_insertion_point(class_scope:Employee.PhoneNumber)
    })
  ,

  'ComplexRole' : _reflection.GeneratedProtocolMessageType('ComplexRole', (_message.Message,), {
    'DESCRIPTOR' : _EMPLOYEE_COMPLEXROLE,
    '__module__' : 'v1.company.employee_pb2'
    # @@protoc_insertion_point(class_scope:Employee.ComplexRole)
    })
  ,
  'DESCRIPTOR' : _EMPLOYEE,
  '__module__' : 'v1.company.employee_pb2'
  # @@protoc_insertion_point(class_scope:Employee)
  })
_sym_db.RegisterMessage(Employee)
_sym_db.RegisterMessage(Employee.PhoneNumber)
_sym_db.RegisterMessage(Employee.ComplexRole)


DESCRIPTOR._options = None
_EMPLOYEE_PHONENUMBER.fields_by_name['number']._options = None
_EMPLOYEE.fields_by_name['email']._options = None
_EMPLOYEE.fields_by_name['first_name']._options = None
_EMPLOYEE.fields_by_name['last_name']._options = None
# @@protoc_insertion_point(module_scope)
