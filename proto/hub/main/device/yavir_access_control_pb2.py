# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/device/yavir_access_control.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from proto.hub.main import name_pb2 as v1_dot_hub_dot_main_dot_name__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/device/yavir_access_control.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n%systems.ajax.a911.grpc.v1.main.deviceP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-v1/hub/main/device/yavir_access_control.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x16v1/hub/main/name.proto\"\xf1\t\n\x12YavirAccessControl\x12\n\n\x02id\x18\x01 \x01(\t\x12\x37\n\x04name\x18\xe8\x07 \x01(\x0b\x32(.systems.ajax.a911.grpc.v1.hub.main.Name\x12\x10\n\x08group_id\x18\x03 \x01(\t\x12;\n3time_to_block_on_multiple_password_failures_minutes\x18\x06 \x01(\x05\x12\x18\n\x10\x63ms_device_index\x18\x07 \x01(\x05\x12\x18\n\x10\x62locking_enabled\x18\x08 \x01(\x08\x12\x1b\n\x13\x61ssociated_group_id\x18\x0c \x01(\t\x12]\n\x0f\x61\x63\x63\x65ss_profiles\x18\r \x03(\x0e\x32\x44.systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.AccessProfile\x12V\n\x0b\x64\x65vice_type\x18\x0e \x01(\x0e\x32\x41.systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.DeviceType\x12\x0f\n\x07\x65nabled\x18\x0f \x01(\x08\x12\x0f\n\x07room_id\x18\x12 \x01(\t\x12+\n\x07\x62locked\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06online\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x08tampered\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12;\n\x16service_problems_count\x18\x13 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12V\n\x0b\x62ypass_mode\x18\x15 \x01(\x0e\x32\x41.systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.BypassMode\x12[\n\x0eis_bypass_mode\x18\x16 \x03(\x0e\x32\x43.systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.IsBypassMode\x12\x15\n\rpassword_hash\x18\x17 \x01(\t\x12\x1c\n\x14password_hash_duress\x18\x18 \x01(\t\"U\n\rAccessProfile\x12\x1a\n\x16NO_ACCESS_PROFILE_INFO\x10\x00\x12\x15\n\x11KEYBOARD_PASSWORD\x10\x01\x12\x11\n\rUSER_PASSWORD\x10\x02\"K\n\nDeviceType\x12\x17\n\x13NO_DEVICE_TYPE_INFO\x10\x00\x12\x12\n\x0e\x44UNAY_KEYBOARD\x10\x01\x12\x10\n\x0cYAVIR_READER\x10\x02\"l\n\nBypassMode\x12\x17\n\x13NO_BYPASS_MODE_INFO\x10\x00\x12\x17\n\x13\x45NGINEER_BYPASS_OFF\x10\x01\x12\x16\n\x12\x45NGINEER_BYPASS_ON\x10\x02\x12\x14\n\x10TAMPER_BYPASS_ON\x10\x03\"]\n\x0cIsBypassMode\x12\x15\n\x11NO_IN_BYPASS_MODE\x10\x00\x12\x1b\n\x17\x45NABLED_ENGINEER_BYPASS\x10\x01\x12\x19\n\x15\x45NABLED_TAMPER_BYPASS\x10\x02\x42\x33\n%systems.ajax.a911.grpc.v1.main.deviceP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_name__pb2.DESCRIPTOR,])



_YAVIRACCESSCONTROL_ACCESSPROFILE = _descriptor.EnumDescriptor(
  name='AccessProfile',
  full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.AccessProfile',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ACCESS_PROFILE_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYBOARD_PASSWORD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='USER_PASSWORD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1040,
  serialized_end=1125,
)
_sym_db.RegisterEnumDescriptor(_YAVIRACCESSCONTROL_ACCESSPROFILE)

_YAVIRACCESSCONTROL_DEVICETYPE = _descriptor.EnumDescriptor(
  name='DeviceType',
  full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.DeviceType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_DEVICE_TYPE_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DUNAY_KEYBOARD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='YAVIR_READER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1127,
  serialized_end=1202,
)
_sym_db.RegisterEnumDescriptor(_YAVIRACCESSCONTROL_DEVICETYPE)

_YAVIRACCESSCONTROL_BYPASSMODE = _descriptor.EnumDescriptor(
  name='BypassMode',
  full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.BypassMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_BYPASS_MODE_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENGINEER_BYPASS_OFF', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENGINEER_BYPASS_ON', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TAMPER_BYPASS_ON', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1204,
  serialized_end=1312,
)
_sym_db.RegisterEnumDescriptor(_YAVIRACCESSCONTROL_BYPASSMODE)

_YAVIRACCESSCONTROL_ISBYPASSMODE = _descriptor.EnumDescriptor(
  name='IsBypassMode',
  full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.IsBypassMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_IN_BYPASS_MODE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENABLED_ENGINEER_BYPASS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENABLED_TAMPER_BYPASS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1314,
  serialized_end=1407,
)
_sym_db.RegisterEnumDescriptor(_YAVIRACCESSCONTROL_ISBYPASSMODE)


_YAVIRACCESSCONTROL = _descriptor.Descriptor(
  name='YavirAccessControl',
  full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.name', index=1,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.group_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_to_block_on_multiple_password_failures_minutes', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.time_to_block_on_multiple_password_failures_minutes', index=3,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cms_device_index', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.cms_device_index', index=4,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blocking_enabled', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.blocking_enabled', index=5,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='associated_group_id', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.associated_group_id', index=6,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_profiles', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.access_profiles', index=7,
      number=13, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.device_type', index=8,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.enabled', index=9,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room_id', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.room_id', index=10,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blocked', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.blocked', index=11,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='online', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.online', index=12,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tampered', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.tampered', index=13,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_problems_count', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.service_problems_count', index=14,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bypass_mode', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.bypass_mode', index=15,
      number=21, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_bypass_mode', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.is_bypass_mode', index=16,
      number=22, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password_hash', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.password_hash', index=17,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password_hash_duress', full_name='systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl.password_hash_duress', index=18,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _YAVIRACCESSCONTROL_ACCESSPROFILE,
    _YAVIRACCESSCONTROL_DEVICETYPE,
    _YAVIRACCESSCONTROL_BYPASSMODE,
    _YAVIRACCESSCONTROL_ISBYPASSMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=1407,
)

_YAVIRACCESSCONTROL.fields_by_name['name'].message_type = v1_dot_hub_dot_main_dot_name__pb2._NAME
_YAVIRACCESSCONTROL.fields_by_name['access_profiles'].enum_type = _YAVIRACCESSCONTROL_ACCESSPROFILE
_YAVIRACCESSCONTROL.fields_by_name['device_type'].enum_type = _YAVIRACCESSCONTROL_DEVICETYPE
_YAVIRACCESSCONTROL.fields_by_name['blocked'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_YAVIRACCESSCONTROL.fields_by_name['online'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_YAVIRACCESSCONTROL.fields_by_name['tampered'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_YAVIRACCESSCONTROL.fields_by_name['service_problems_count'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_YAVIRACCESSCONTROL.fields_by_name['bypass_mode'].enum_type = _YAVIRACCESSCONTROL_BYPASSMODE
_YAVIRACCESSCONTROL.fields_by_name['is_bypass_mode'].enum_type = _YAVIRACCESSCONTROL_ISBYPASSMODE
_YAVIRACCESSCONTROL_ACCESSPROFILE.containing_type = _YAVIRACCESSCONTROL
_YAVIRACCESSCONTROL_DEVICETYPE.containing_type = _YAVIRACCESSCONTROL
_YAVIRACCESSCONTROL_BYPASSMODE.containing_type = _YAVIRACCESSCONTROL
_YAVIRACCESSCONTROL_ISBYPASSMODE.containing_type = _YAVIRACCESSCONTROL
DESCRIPTOR.message_types_by_name['YavirAccessControl'] = _YAVIRACCESSCONTROL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

YavirAccessControl = _reflection.GeneratedProtocolMessageType('YavirAccessControl', (_message.Message,), {
  'DESCRIPTOR' : _YAVIRACCESSCONTROL,
  '__module__' : 'v1.hub.main.device.yavir_access_control_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.YavirAccessControl)
  })
_sym_db.RegisterMessage(YavirAccessControl)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
