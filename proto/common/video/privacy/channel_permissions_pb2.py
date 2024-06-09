# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/common/video/privacy/channel_permissions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from proto.common.video.privacy import channel_permission_pb2 as v2_dot_common_dot_video_dot_privacy_dot_channel__permission__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2/common/video/privacy/channel_permissions.proto',
  package='systems.ajax.api.desktop.v2.common.video.privacy',
  syntax='proto3',
  serialized_options=b'\n0systems.ajax.api.desktop.v2.common.video.privacyP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1v2/common/video/privacy/channel_permissions.proto\x12\x30systems.ajax.api.desktop.v2.common.video.privacy\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x30v2/common/video/privacy/channel_permission.proto\"\x89\x07\n\x12\x43hannelPermissions\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12m\n\x06\x61\x63tive\x18\x02 \x01(\x0b\x32].systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.ActiveChannelPermissions\x12o\n\x07granted\x18\x03 \x01(\x0b\x32^.systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.GrantedChannelPermissions\x1at\n\x18\x41\x63tiveChannelPermissions\x12X\n\x0bpermissions\x18\x01 \x03(\x0e\x32\x43.systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermission\x1a\x88\x04\n\x19GrantedChannelPermissions\x12X\n\x0bpermissions\x18\x01 \x03(\x0e\x32\x43.systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermission\x12\x82\x01\n\x04type\x18\x02 \x01(\x0e\x32t.systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.GrantedChannelPermissions.ChannelPermissionType\x12-\n\texpire_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xdc\x01\n\x15\x43hannelPermissionType\x12\'\n#CHANNEL_PERMISSION_TYPE_UNSPECIFIED\x10\x00\x12\"\n\x1e\x43HANNEL_PERMISSION_TYPE_ALWAYS\x10\x01\x12&\n\"CHANNEL_PERMISSION_TYPE_WHEN_ARMED\x10\x02\x12\'\n#CHANNEL_PERMISSION_TYPE_AFTER_ALARM\x10\x03\x12%\n!CHANNEL_PERMISSION_TYPE_TEMPORARY\x10\x04\x42\x34\n0systems.ajax.api.desktop.v2.common.video.privacyP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_privacy_dot_channel__permission__pb2.DESCRIPTOR,])



_CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS_CHANNELPERMISSIONTYPE = _descriptor.EnumDescriptor(
  name='ChannelPermissionType',
  full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.GrantedChannelPermissions.ChannelPermissionType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_PERMISSION_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_PERMISSION_TYPE_ALWAYS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_PERMISSION_TYPE_WHEN_ARMED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_PERMISSION_TYPE_AFTER_ALARM', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANNEL_PERMISSION_TYPE_TEMPORARY', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=872,
  serialized_end=1092,
)
_sym_db.RegisterEnumDescriptor(_CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS_CHANNELPERMISSIONTYPE)


_CHANNELPERMISSIONS_ACTIVECHANNELPERMISSIONS = _descriptor.Descriptor(
  name='ActiveChannelPermissions',
  full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.ActiveChannelPermissions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='permissions', full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.ActiveChannelPermissions.permissions', index=0,
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
  serialized_start=453,
  serialized_end=569,
)

_CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS = _descriptor.Descriptor(
  name='GrantedChannelPermissions',
  full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.GrantedChannelPermissions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='permissions', full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.GrantedChannelPermissions.permissions', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.GrantedChannelPermissions.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expire_at', full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.GrantedChannelPermissions.expire_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS_CHANNELPERMISSIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=572,
  serialized_end=1092,
)

_CHANNELPERMISSIONS = _descriptor.Descriptor(
  name='ChannelPermissions',
  full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.channel_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.active', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='granted', full_name='systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.granted', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CHANNELPERMISSIONS_ACTIVECHANNELPERMISSIONS, _CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=1092,
)

_CHANNELPERMISSIONS_ACTIVECHANNELPERMISSIONS.fields_by_name['permissions'].enum_type = v2_dot_common_dot_video_dot_privacy_dot_channel__permission__pb2._CHANNELPERMISSION
_CHANNELPERMISSIONS_ACTIVECHANNELPERMISSIONS.containing_type = _CHANNELPERMISSIONS
_CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS.fields_by_name['permissions'].enum_type = v2_dot_common_dot_video_dot_privacy_dot_channel__permission__pb2._CHANNELPERMISSION
_CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS.fields_by_name['type'].enum_type = _CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS_CHANNELPERMISSIONTYPE
_CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS.fields_by_name['expire_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS.containing_type = _CHANNELPERMISSIONS
_CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS_CHANNELPERMISSIONTYPE.containing_type = _CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS
_CHANNELPERMISSIONS.fields_by_name['active'].message_type = _CHANNELPERMISSIONS_ACTIVECHANNELPERMISSIONS
_CHANNELPERMISSIONS.fields_by_name['granted'].message_type = _CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS
DESCRIPTOR.message_types_by_name['ChannelPermissions'] = _CHANNELPERMISSIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelPermissions = _reflection.GeneratedProtocolMessageType('ChannelPermissions', (_message.Message,), {

  'ActiveChannelPermissions' : _reflection.GeneratedProtocolMessageType('ActiveChannelPermissions', (_message.Message,), {
    'DESCRIPTOR' : _CHANNELPERMISSIONS_ACTIVECHANNELPERMISSIONS,
    '__module__' : 'v2.common.video.privacy.channel_permissions_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.ActiveChannelPermissions)
    })
  ,

  'GrantedChannelPermissions' : _reflection.GeneratedProtocolMessageType('GrantedChannelPermissions', (_message.Message,), {
    'DESCRIPTOR' : _CHANNELPERMISSIONS_GRANTEDCHANNELPERMISSIONS,
    '__module__' : 'v2.common.video.privacy.channel_permissions_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions.GrantedChannelPermissions)
    })
  ,
  'DESCRIPTOR' : _CHANNELPERMISSIONS,
  '__module__' : 'v2.common.video.privacy.channel_permissions_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.privacy.ChannelPermissions)
  })
_sym_db.RegisterMessage(ChannelPermissions)
_sym_db.RegisterMessage(ChannelPermissions.ActiveChannelPermissions)
_sym_db.RegisterMessage(ChannelPermissions.GrantedChannelPermissions)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)