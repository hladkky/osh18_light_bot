# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/hub-permission.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/hub-permission.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\036systems.ajax.a911.grpc.v1.mainP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n v1/hub/main/hub-permission.proto\x12\"systems.ajax.a911.grpc.v1.hub.main*\x91\x04\n\rHubPermission\x12\x16\n\x12NO_PERMISSION_INFO\x10\x00\x12\x10\n\x0c\x44\x45LETE_USERS\x10\x01\x12\x10\n\x0cINVITE_USERS\x10\x02\x12\x14\n\x10\x43HANGE_USER_ROLE\x10\x03\x12\x1b\n\x17\x43HANGE_USER_PERMISSIONS\x10\x04\x12 \n\x1c\x45\x44IT_NOTIFICATION_PERMISSION\x10\x05\x12\x07\n\x03\x41RM\x10\x06\x12\x0f\n\x0bPARTIAL_ARM\x10\x07\x12\n\n\x06\x44ISARM\x10\x08\x12\x10\n\x0cPANIC_BUTTON\x10\t\x12\x0e\n\nROOMS_EDIT\x10\n\x12\x0f\n\x0b\x44\x45VICE_EDIT\x10\x0b\x12\x12\n\x0eHUB_ADV_PARAMS\x10\x0e\x12\x15\n\x11HUB_COMMON_PARAMS\x10\x0f\x12\x16\n\x12SET_STATE_COMMANDS\x10\x10\x12\x17\n\x13\x46W_UPDATES_COMMANDS\x10\x11\x12\x0f\n\x0b\x43\x41MERA_EDIT\x10\x12\x12\x10\n\x0c\x43\x41MERA_WATCH\x10\x13\x12\x0f\n\x0bGROUPS_EDIT\x10\x14\x12\x14\n\x10\x45VENT_VISIBILITY\x10\x15\x12\x18\n\x14STRUCTURE_VISIBILITY\x10\x16\x12\x11\n\rSCENARIO_EDIT\x10\x17\x12\x0f\n\x0b\x45\x44IT_CHIMES\x10\x18\x12\x1b\n\x17PRIVACY_SETTINGS_ACCESS\x10\x19\x12\x15\n\x11MUTE_FIRE_PROTECT\x10\x1a\x42,\n\x1esystems.ajax.a911.grpc.v1.mainP\x01\xba\x02\x07Systemsb\x06proto3'
)

_HUBPERMISSION = _descriptor.EnumDescriptor(
  name='HubPermission',
  full_name='systems.ajax.a911.grpc.v1.hub.main.HubPermission',
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
      name='DELETE_USERS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVITE_USERS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_USER_ROLE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_USER_PERMISSIONS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EDIT_NOTIFICATION_PERMISSION', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ARM', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PARTIAL_ARM', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISARM', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PANIC_BUTTON', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOMS_EDIT', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_EDIT', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HUB_ADV_PARAMS', index=12, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HUB_COMMON_PARAMS', index=13, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SET_STATE_COMMANDS', index=14, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FW_UPDATES_COMMANDS', index=15, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_EDIT', index=16, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_WATCH', index=17, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GROUPS_EDIT', index=18, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EVENT_VISIBILITY', index=19, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRUCTURE_VISIBILITY', index=20, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCENARIO_EDIT', index=21, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EDIT_CHIMES', index=22, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_SETTINGS_ACCESS', index=23, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MUTE_FIRE_PROTECT', index=24, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=73,
  serialized_end=602,
)
_sym_db.RegisterEnumDescriptor(_HUBPERMISSION)

HubPermission = enum_type_wrapper.EnumTypeWrapper(_HUBPERMISSION)
NO_PERMISSION_INFO = 0
DELETE_USERS = 1
INVITE_USERS = 2
CHANGE_USER_ROLE = 3
CHANGE_USER_PERMISSIONS = 4
EDIT_NOTIFICATION_PERMISSION = 5
ARM = 6
PARTIAL_ARM = 7
DISARM = 8
PANIC_BUTTON = 9
ROOMS_EDIT = 10
DEVICE_EDIT = 11
HUB_ADV_PARAMS = 14
HUB_COMMON_PARAMS = 15
SET_STATE_COMMANDS = 16
FW_UPDATES_COMMANDS = 17
CAMERA_EDIT = 18
CAMERA_WATCH = 19
GROUPS_EDIT = 20
EVENT_VISIBILITY = 21
STRUCTURE_VISIBILITY = 22
SCENARIO_EDIT = 23
EDIT_CHIMES = 24
PRIVACY_SETTINGS_ACCESS = 25
MUTE_FIRE_PROTECT = 26


DESCRIPTOR.enum_types_by_name['HubPermission'] = _HUBPERMISSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
