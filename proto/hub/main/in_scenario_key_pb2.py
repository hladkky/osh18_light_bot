# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/in_scenario_key.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/in_scenario_key.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\031systems.ajax.protobuf.hubP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!v1/hub/main/in_scenario_key.proto*\xfe\x01\n\rInScenarioKey\x12\x1b\n\x17NO_IN_SCENARIO_KEY_INFO\x10\x00\x12\x19\n\x15LIGHT_SWITCH_CHANNEL1\x10}\x12\x19\n\x15LIGHT_SWITCH_CHANNEL2\x10~\x12%\n!FOUR_CHANNEL_RELAY_FIBRA_CHANNEL1\x10\x44\x12%\n!FOUR_CHANNEL_RELAY_FIBRA_CHANNEL2\x10L\x12%\n!FOUR_CHANNEL_RELAY_FIBRA_CHANNEL3\x10t\x12%\n!FOUR_CHANNEL_RELAY_FIBRA_CHANNEL4\x10|B\'\n\x19systems.ajax.protobuf.hubP\x01\xba\x02\x07Systemsb\x06proto3'
)

_INSCENARIOKEY = _descriptor.EnumDescriptor(
  name='InScenarioKey',
  full_name='InScenarioKey',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_IN_SCENARIO_KEY_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LIGHT_SWITCH_CHANNEL1', index=1, number=125,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LIGHT_SWITCH_CHANNEL2', index=2, number=126,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FOUR_CHANNEL_RELAY_FIBRA_CHANNEL1', index=3, number=68,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FOUR_CHANNEL_RELAY_FIBRA_CHANNEL2', index=4, number=76,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FOUR_CHANNEL_RELAY_FIBRA_CHANNEL3', index=5, number=116,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FOUR_CHANNEL_RELAY_FIBRA_CHANNEL4', index=6, number=124,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=38,
  serialized_end=292,
)
_sym_db.RegisterEnumDescriptor(_INSCENARIOKEY)

InScenarioKey = enum_type_wrapper.EnumTypeWrapper(_INSCENARIOKEY)
NO_IN_SCENARIO_KEY_INFO = 0
LIGHT_SWITCH_CHANNEL1 = 125
LIGHT_SWITCH_CHANNEL2 = 126
FOUR_CHANNEL_RELAY_FIBRA_CHANNEL1 = 68
FOUR_CHANNEL_RELAY_FIBRA_CHANNEL2 = 76
FOUR_CHANNEL_RELAY_FIBRA_CHANNEL3 = 116
FOUR_CHANNEL_RELAY_FIBRA_CHANNEL4 = 124


DESCRIPTOR.enum_types_by_name['InScenarioKey'] = _INSCENARIOKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
