# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/common/hub/device/common/device_transmition_power_mode.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2/common/hub/device/common/device_transmition_power_mode.proto',
  package='systems.ajax.api.desktop.v2.common.hub.device.common',
  syntax='proto3',
  serialized_options=b'\n4systems.ajax.api.desktop.v2.common.hub.device.commonP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?v2/common/hub/device/common/device_transmition_power_mode.proto\x12\x34systems.ajax.api.desktop.v2.common.hub.device.common*\xed\x01\n\x1a\x44\x65viceTransmitionPowerMode\x12-\n)DEVICE_TRANSMITION_POWER_MODE_UNSPECIFIED\x10\x00\x12&\n\"DEVICE_TRANSMITION_POWER_MODE_AUTO\x10\x01\x12%\n!DEVICE_TRANSMITION_POWER_MODE_FIX\x10\x02\x12*\n&DEVICE_TRANSMITION_POWER_MODE_RESERVED\x10\x03\x12%\n!DEVICE_TRANSMITION_POWER_MODE_MAX\x10\x04\x42\x38\n4systems.ajax.api.desktop.v2.common.hub.device.commonP\x01\x62\x06proto3'
)

_DEVICETRANSMITIONPOWERMODE = _descriptor.EnumDescriptor(
  name='DeviceTransmitionPowerMode',
  full_name='systems.ajax.api.desktop.v2.common.hub.device.common.DeviceTransmitionPowerMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TRANSMITION_POWER_MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TRANSMITION_POWER_MODE_AUTO', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TRANSMITION_POWER_MODE_FIX', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TRANSMITION_POWER_MODE_RESERVED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TRANSMITION_POWER_MODE_MAX', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=122,
  serialized_end=359,
)
_sym_db.RegisterEnumDescriptor(_DEVICETRANSMITIONPOWERMODE)

DeviceTransmitionPowerMode = enum_type_wrapper.EnumTypeWrapper(_DEVICETRANSMITIONPOWERMODE)
DEVICE_TRANSMITION_POWER_MODE_UNSPECIFIED = 0
DEVICE_TRANSMITION_POWER_MODE_AUTO = 1
DEVICE_TRANSMITION_POWER_MODE_FIX = 2
DEVICE_TRANSMITION_POWER_MODE_RESERVED = 3
DEVICE_TRANSMITION_POWER_MODE_MAX = 4


DESCRIPTOR.enum_types_by_name['DeviceTransmitionPowerMode'] = _DEVICETRANSMITIONPOWERMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)