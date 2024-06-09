# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/facility/facility-employee-acl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from proto.systems.ajax.logging.proto import log_marker_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/facility/facility-employee-acl.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\"systems.ajax.a911.grpc.facility.v1\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'v1/facility/facility-employee-acl.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a+systems/ajax/logging/proto/log_marker.proto\"\xf0\x01\n\x13\x46\x61\x63ilityEmployeeAcl\x12\x18\n\x0b\x65mployee_id\x18\x01 \x01(\tB\x03\xf0\x44\x07\x12\x17\n\ncompany_id\x18\x02 \x01(\tB\x03\xf0\x44\x03\x12\x13\n\x0b\x66\x61\x63ility_id\x18\x03 \x01(\t\x12\x34\n\x0bpermissions\x18\x04 \x03(\x0e\x32\x1f.FacilityEmployeeAcl.Permission\x12\x38\n\x14\x65xpiration_edit_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"!\n\nPermission\x12\x08\n\x04READ\x10\x00\x12\t\n\x05WRITE\x10\x01\"\x8e\x01\n\x0c\x41\x63\x63\x65ssRights\x12\x1a\n\x12\x65xpiration_seconds\x18\x01 \x01(\x03\x12-\n\x0b\x61\x63\x63\x65ss_type\x18\x02 \x01(\x0e\x32\x18.AccessRights.AccessType\"3\n\nAccessType\x12\x0b\n\x07\x45XPIRED\x10\x00\x12\r\n\tPERMANENT\x10\x01\x12\t\n\x05VALID\x10\x02\x42\'\n\"systems.ajax.a911.grpc.facility.v1\xba\x02\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2.DESCRIPTOR,])



_FACILITYEMPLOYEEACL_PERMISSION = _descriptor.EnumDescriptor(
  name='Permission',
  full_name='FacilityEmployeeAcl.Permission',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READ', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=329,
  serialized_end=362,
)
_sym_db.RegisterEnumDescriptor(_FACILITYEMPLOYEEACL_PERMISSION)

_ACCESSRIGHTS_ACCESSTYPE = _descriptor.EnumDescriptor(
  name='AccessType',
  full_name='AccessRights.AccessType',
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
  serialized_start=456,
  serialized_end=507,
)
_sym_db.RegisterEnumDescriptor(_ACCESSRIGHTS_ACCESSTYPE)


_FACILITYEMPLOYEEACL = _descriptor.Descriptor(
  name='FacilityEmployeeAcl',
  full_name='FacilityEmployeeAcl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='employee_id', full_name='FacilityEmployeeAcl.employee_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360D\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_id', full_name='FacilityEmployeeAcl.company_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360D\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='facility_id', full_name='FacilityEmployeeAcl.facility_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='FacilityEmployeeAcl.permissions', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expiration_edit_date', full_name='FacilityEmployeeAcl.expiration_edit_date', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FACILITYEMPLOYEEACL_PERMISSION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=362,
)


_ACCESSRIGHTS = _descriptor.Descriptor(
  name='AccessRights',
  full_name='AccessRights',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='expiration_seconds', full_name='AccessRights.expiration_seconds', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_type', full_name='AccessRights.access_type', index=1,
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
    _ACCESSRIGHTS_ACCESSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=507,
)

_FACILITYEMPLOYEEACL.fields_by_name['permissions'].enum_type = _FACILITYEMPLOYEEACL_PERMISSION
_FACILITYEMPLOYEEACL.fields_by_name['expiration_edit_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FACILITYEMPLOYEEACL_PERMISSION.containing_type = _FACILITYEMPLOYEEACL
_ACCESSRIGHTS.fields_by_name['access_type'].enum_type = _ACCESSRIGHTS_ACCESSTYPE
_ACCESSRIGHTS_ACCESSTYPE.containing_type = _ACCESSRIGHTS
DESCRIPTOR.message_types_by_name['FacilityEmployeeAcl'] = _FACILITYEMPLOYEEACL
DESCRIPTOR.message_types_by_name['AccessRights'] = _ACCESSRIGHTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FacilityEmployeeAcl = _reflection.GeneratedProtocolMessageType('FacilityEmployeeAcl', (_message.Message,), {
  'DESCRIPTOR' : _FACILITYEMPLOYEEACL,
  '__module__' : 'v1.facility.facility_employee_acl_pb2'
  # @@protoc_insertion_point(class_scope:FacilityEmployeeAcl)
  })
_sym_db.RegisterMessage(FacilityEmployeeAcl)

AccessRights = _reflection.GeneratedProtocolMessageType('AccessRights', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSRIGHTS,
  '__module__' : 'v1.facility.facility_employee_acl_pb2'
  # @@protoc_insertion_point(class_scope:AccessRights)
  })
_sym_db.RegisterMessage(AccessRights)


DESCRIPTOR._options = None
_FACILITYEMPLOYEEACL.fields_by_name['employee_id']._options = None
_FACILITYEMPLOYEEACL.fields_by_name['company_id']._options = None
# @@protoc_insertion_point(module_scope)