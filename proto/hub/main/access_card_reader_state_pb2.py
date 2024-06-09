# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/access_card_reader_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/access_card_reader_state.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\036systems.ajax.a911.grpc.v1.mainP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*v1/hub/main/access_card_reader_state.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\"V\n\x15\x41\x63\x63\x65ssCardReaderState\x12\x0b\n\x02id\x18\xe8\x07 \x01(\t\x12\x18\n\x0ftimeout_seconds\x18\xe9\x07 \x01(\x05\x12\x16\n\rreader_active\x18\xea\x07 \x01(\x08\x42,\n\x1esystems.ajax.a911.grpc.v1.mainP\x01\xba\x02\x07Systemsb\x06proto3'
)




_ACCESSCARDREADERSTATE = _descriptor.Descriptor(
  name='AccessCardReaderState',
  full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCardReaderState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCardReaderState.id', index=0,
      number=1000, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout_seconds', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCardReaderState.timeout_seconds', index=1,
      number=1001, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reader_active', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCardReaderState.reader_active', index=2,
      number=1002, type=8, cpp_type=7, label=1,
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
  serialized_start=82,
  serialized_end=168,
)

DESCRIPTOR.message_types_by_name['AccessCardReaderState'] = _ACCESSCARDREADERSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessCardReaderState = _reflection.GeneratedProtocolMessageType('AccessCardReaderState', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSCARDREADERSTATE,
  '__module__' : 'v1.hub.main.access_card_reader_state_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.AccessCardReaderState)
  })
_sym_db.RegisterMessage(AccessCardReaderState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
