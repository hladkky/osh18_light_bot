# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/additional/data/time_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/additional/data/time_data.proto',
  package='systems.ajax.a911.grpc.v1.hub.main.additional.data',
  syntax='proto3',
  serialized_options=b'\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+v1/hub/main/additional/data/time_data.proto\x12\x32systems.ajax.a911.grpc.v1.hub.main.additional.data\",\n\x08TimeData\x12 \n\x18time_seconds_linux_epoch\x18\x01 \x01(\x05\x42\x36\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\x01\x62\x06proto3'
)




_TIMEDATA = _descriptor.Descriptor(
  name='TimeData',
  full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.TimeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_seconds_linux_epoch', full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.TimeData.time_seconds_linux_epoch', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=99,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['TimeData'] = _TIMEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeData = _reflection.GeneratedProtocolMessageType('TimeData', (_message.Message,), {
  'DESCRIPTOR' : _TIMEDATA,
  '__module__' : 'v1.hub.main.additional.data.time_data_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.additional.data.TimeData)
  })
_sym_db.RegisterMessage(TimeData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)