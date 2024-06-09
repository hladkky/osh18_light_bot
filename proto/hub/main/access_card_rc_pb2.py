# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/access_card_rc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/access_card_rc.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\036systems.ajax.a911.grpc.v1.mainP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n v1/hub/main/access_card_rc.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\"\xc3\x01\n\x0c\x41\x63\x63\x65ssCardRc\x12@\n\x02rc\x18\xe8\x07 \x01(\x0e\x32\x33.systems.ajax.a911.grpc.v1.hub.main.AccessCardRc.Rc\"q\n\x02Rc\x12\t\n\x05\x41\x44\x44\x45\x44\x10\x00\x12\x11\n\rALREADY_ADDED\x10\x01\x12\r\n\tCARD_FULL\x10\x02\x12\x0b\n\x07TIMEOUT\x10\x03\x12\x10\n\x0cINVALID_CARD\x10\x04\x12\x10\n\x0cUSER_TIMEOUT\x10\x05\x12\r\n\tNO_ANSWER\x10\x06\x42,\n\x1esystems.ajax.a911.grpc.v1.mainP\x01\xba\x02\x07Systemsb\x06proto3'
)



_ACCESSCARDRC_RC = _descriptor.EnumDescriptor(
  name='Rc',
  full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCardRc.Rc',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADDED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALREADY_ADDED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CARD_FULL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CARD', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='USER_TIMEOUT', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_ANSWER', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=155,
  serialized_end=268,
)
_sym_db.RegisterEnumDescriptor(_ACCESSCARDRC_RC)


_ACCESSCARDRC = _descriptor.Descriptor(
  name='AccessCardRc',
  full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCardRc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rc', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCardRc.rc', index=0,
      number=1000, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACCESSCARDRC_RC,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=268,
)

_ACCESSCARDRC.fields_by_name['rc'].enum_type = _ACCESSCARDRC_RC
_ACCESSCARDRC_RC.containing_type = _ACCESSCARDRC
DESCRIPTOR.message_types_by_name['AccessCardRc'] = _ACCESSCARDRC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessCardRc = _reflection.GeneratedProtocolMessageType('AccessCardRc', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSCARDRC,
  '__module__' : 'v1.hub.main.access_card_rc_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.AccessCardRc)
  })
_sym_db.RegisterMessage(AccessCardRc)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
