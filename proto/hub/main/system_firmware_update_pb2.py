# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/system_firmware_update.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/system_firmware_update.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\"systems.ajax.a911.grpc.hub.v1.mainP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(v1/hub/main/system_firmware_update.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x1bgoogle/protobuf/empty.proto\"\x91\x02\n\x14SystemFirmwareUpdate\x12\x18\n\x10\x66irmware_version\x18\x01 \x01(\t\x12O\n\x06status\x18\x02 \x01(\x0b\x32?.systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate.Status\x12\x1c\n\x14\x66irmware_version_raw\x18\x03 \x01(\x05\x1ap\n\x06Status\x12-\n\x0bnot_started\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12-\n\x0b\x64ownloading\x18\x02 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x42\x08\n\x06statusB&\n\"systems.ajax.a911.grpc.hub.v1.mainP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SYSTEMFIRMWAREUPDATE_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='not_started', full_name='systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate.Status.not_started', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downloading', full_name='systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate.Status.downloading', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='status', full_name='systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate.Status.status',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=271,
  serialized_end=383,
)

_SYSTEMFIRMWAREUPDATE = _descriptor.Descriptor(
  name='SystemFirmwareUpdate',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='firmware_version', full_name='systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate.firmware_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='firmware_version_raw', full_name='systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate.firmware_version_raw', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SYSTEMFIRMWAREUPDATE_STATUS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=383,
)

_SYSTEMFIRMWAREUPDATE_STATUS.fields_by_name['not_started'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_SYSTEMFIRMWAREUPDATE_STATUS.fields_by_name['downloading'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_SYSTEMFIRMWAREUPDATE_STATUS.containing_type = _SYSTEMFIRMWAREUPDATE
_SYSTEMFIRMWAREUPDATE_STATUS.oneofs_by_name['status'].fields.append(
  _SYSTEMFIRMWAREUPDATE_STATUS.fields_by_name['not_started'])
_SYSTEMFIRMWAREUPDATE_STATUS.fields_by_name['not_started'].containing_oneof = _SYSTEMFIRMWAREUPDATE_STATUS.oneofs_by_name['status']
_SYSTEMFIRMWAREUPDATE_STATUS.oneofs_by_name['status'].fields.append(
  _SYSTEMFIRMWAREUPDATE_STATUS.fields_by_name['downloading'])
_SYSTEMFIRMWAREUPDATE_STATUS.fields_by_name['downloading'].containing_oneof = _SYSTEMFIRMWAREUPDATE_STATUS.oneofs_by_name['status']
_SYSTEMFIRMWAREUPDATE.fields_by_name['status'].message_type = _SYSTEMFIRMWAREUPDATE_STATUS
DESCRIPTOR.message_types_by_name['SystemFirmwareUpdate'] = _SYSTEMFIRMWAREUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SystemFirmwareUpdate = _reflection.GeneratedProtocolMessageType('SystemFirmwareUpdate', (_message.Message,), {

  'Status' : _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
    'DESCRIPTOR' : _SYSTEMFIRMWAREUPDATE_STATUS,
    '__module__' : 'v1.hub.main.system_firmware_update_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate.Status)
    })
  ,
  'DESCRIPTOR' : _SYSTEMFIRMWAREUPDATE,
  '__module__' : 'v1.hub.main.system_firmware_update_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate)
  })
_sym_db.RegisterMessage(SystemFirmwareUpdate)
_sym_db.RegisterMessage(SystemFirmwareUpdate.Status)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)