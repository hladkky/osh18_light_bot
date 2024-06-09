# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/device/access_card.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.hub.main import name_pb2 as v1_dot_hub_dot_main_dot_name__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/device/access_card.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n%systems.ajax.a911.grpc.v1.main.deviceP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$v1/hub/main/device/access_card.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x16v1/hub/main/name.proto\"\xd2\x06\n\nAccessCard\x12\n\n\x02id\x18\x01 \x01(\t\x12\x37\n\x04name\x18\xe8\x07 \x01(\x0b\x32(.systems.ajax.a911.grpc.v1.hub.main.Name\x12\x13\n\x0b\x63\x61rd_record\x18\x03 \x01(\x05\x12\x10\n\x08\x63\x61rd_UID\x18\x04 \x01(\x03\x12\x15\n\rcard_key_seed\x18\x05 \x01(\x05\x12\x0e\n\x06\x61pp_id\x18\x06 \x01(\x05\x12[\n\x11group_permissions\x18\xf2\x07 \x03(\x0b\x32?.systems.ajax.a911.grpc.v1.hub.main.AccessCard.GroupPermissions\x12\x1a\n\x12\x61ssociated_user_id\x18\t \x01(\t\x12\x14\n\x0c\x64\x65vice_index\x18\n \x01(\x05\x12\x15\n\rperimeter_arm\x18\x0b \x01(\x08\x12\x10\n\x08\x66ull_arm\x18\x0c \x01(\x08\x12\x14\n\x0c\x63\x61rd_enabled\x18\r \x01(\x08\x12L\n\tattribute\x18\xfc\x07 \x01(\x0b\x32\x38.systems.ajax.a911.grpc.v1.hub.main.AccessCard.Attribute\x1a\xc2\x01\n\x10GroupPermissions\x12\x11\n\x08group_id\x18\xe8\x07 \x01(\t\x12`\n\x0bpermissions\x18\xe9\x07 \x03(\x0e\x32J.systems.ajax.a911.grpc.v1.hub.main.AccessCard.GroupPermissions.Permission\"9\n\nPermission\x12\x16\n\x12NO_PERMISSION_INFO\x10\x00\x12\x07\n\x03\x41RM\x10\x01\x12\n\n\x06\x44ISARM\x10\x02\x1a\x95\x01\n\tAttribute\x12\x44\n\x05\x63olor\x18\xe8\x07 \x01(\x0e\x32\x34.systems.ajax.a911.grpc.v1.hub.main.AccessCard.Color\x12\x42\n\x04type\x18\xe9\x07 \x01(\x0e\x32\x33.systems.ajax.a911.grpc.v1.hub.main.AccessCard.Type\"\x1d\n\x05\x43olor\x12\t\n\x05WHITE\x10\x00\x12\t\n\x05\x42LACK\x10\x10\"\x19\n\x04Type\x12\x08\n\x04\x43\x41RD\x10\x00\x12\x07\n\x03TAG\x10\x01\x42\x33\n%systems.ajax.a911.grpc.v1.main.deviceP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[v1_dot_hub_dot_main_dot_name__pb2.DESCRIPTOR,])



_ACCESSCARD_GROUPPERMISSIONS_PERMISSION = _descriptor.EnumDescriptor(
  name='Permission',
  full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.GroupPermissions.Permission',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_PERMISSION_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ARM', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISARM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=684,
  serialized_end=741,
)
_sym_db.RegisterEnumDescriptor(_ACCESSCARD_GROUPPERMISSIONS_PERMISSION)

_ACCESSCARD_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.Color',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WHITE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLACK', index=1, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=895,
  serialized_end=924,
)
_sym_db.RegisterEnumDescriptor(_ACCESSCARD_COLOR)

_ACCESSCARD_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CARD', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TAG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=926,
  serialized_end=951,
)
_sym_db.RegisterEnumDescriptor(_ACCESSCARD_TYPE)


_ACCESSCARD_GROUPPERMISSIONS = _descriptor.Descriptor(
  name='GroupPermissions',
  full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.GroupPermissions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.GroupPermissions.group_id', index=0,
      number=1000, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.GroupPermissions.permissions', index=1,
      number=1001, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACCESSCARD_GROUPPERMISSIONS_PERMISSION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=741,
)

_ACCESSCARD_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.Attribute.color', index=0,
      number=1000, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.Attribute.type', index=1,
      number=1001, type=14, cpp_type=8, label=1,
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
  serialized_start=744,
  serialized_end=893,
)

_ACCESSCARD = _descriptor.Descriptor(
  name='AccessCard',
  full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.name', index=1,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='card_record', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.card_record', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='card_UID', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.card_UID', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='card_key_seed', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.card_key_seed', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.app_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_permissions', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.group_permissions', index=6,
      number=1010, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='associated_user_id', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.associated_user_id', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_index', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.device_index', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='perimeter_arm', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.perimeter_arm', index=9,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='full_arm', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.full_arm', index=10,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='card_enabled', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.card_enabled', index=11,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='systems.ajax.a911.grpc.v1.hub.main.AccessCard.attribute', index=12,
      number=1020, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ACCESSCARD_GROUPPERMISSIONS, _ACCESSCARD_ATTRIBUTE, ],
  enum_types=[
    _ACCESSCARD_COLOR,
    _ACCESSCARD_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=951,
)

_ACCESSCARD_GROUPPERMISSIONS.fields_by_name['permissions'].enum_type = _ACCESSCARD_GROUPPERMISSIONS_PERMISSION
_ACCESSCARD_GROUPPERMISSIONS.containing_type = _ACCESSCARD
_ACCESSCARD_GROUPPERMISSIONS_PERMISSION.containing_type = _ACCESSCARD_GROUPPERMISSIONS
_ACCESSCARD_ATTRIBUTE.fields_by_name['color'].enum_type = _ACCESSCARD_COLOR
_ACCESSCARD_ATTRIBUTE.fields_by_name['type'].enum_type = _ACCESSCARD_TYPE
_ACCESSCARD_ATTRIBUTE.containing_type = _ACCESSCARD
_ACCESSCARD.fields_by_name['name'].message_type = v1_dot_hub_dot_main_dot_name__pb2._NAME
_ACCESSCARD.fields_by_name['group_permissions'].message_type = _ACCESSCARD_GROUPPERMISSIONS
_ACCESSCARD.fields_by_name['attribute'].message_type = _ACCESSCARD_ATTRIBUTE
_ACCESSCARD_COLOR.containing_type = _ACCESSCARD
_ACCESSCARD_TYPE.containing_type = _ACCESSCARD
DESCRIPTOR.message_types_by_name['AccessCard'] = _ACCESSCARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessCard = _reflection.GeneratedProtocolMessageType('AccessCard', (_message.Message,), {

  'GroupPermissions' : _reflection.GeneratedProtocolMessageType('GroupPermissions', (_message.Message,), {
    'DESCRIPTOR' : _ACCESSCARD_GROUPPERMISSIONS,
    '__module__' : 'v1.hub.main.device.access_card_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.AccessCard.GroupPermissions)
    })
  ,

  'Attribute' : _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {
    'DESCRIPTOR' : _ACCESSCARD_ATTRIBUTE,
    '__module__' : 'v1.hub.main.device.access_card_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.AccessCard.Attribute)
    })
  ,
  'DESCRIPTOR' : _ACCESSCARD,
  '__module__' : 'v1.hub.main.device.access_card_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.AccessCard)
  })
_sym_db.RegisterMessage(AccessCard)
_sym_db.RegisterMessage(AccessCard.GroupPermissions)
_sym_db.RegisterMessage(AccessCard.Attribute)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)