# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/additional/data/firmware_version.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/additional/data/firmware_version.proto',
  package='systems.ajax.a911.grpc.v1.hub.main.additional.data',
  syntax='proto3',
  serialized_options=b'\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2v1/hub/main/additional/data/firmware_version.proto\x12\x32systems.ajax.a911.grpc.v1.hub.main.additional.data\"\"\n\x0f\x46irmwareVersion\x12\x0f\n\x07version\x18\x01 \x01(\tB6\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\x01\x62\x06proto3'
)




_FIRMWAREVERSION = _descriptor.Descriptor(
  name='FirmwareVersion',
  full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.FirmwareVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.FirmwareVersion.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=106,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['FirmwareVersion'] = _FIRMWAREVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FirmwareVersion = _reflection.GeneratedProtocolMessageType('FirmwareVersion', (_message.Message,), {
  'DESCRIPTOR' : _FIRMWAREVERSION,
  '__module__' : 'v1.hub.main.additional.data.firmware_version_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.additional.data.FirmwareVersion)
  })
_sym_db.RegisterMessage(FirmwareVersion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
