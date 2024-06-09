# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/device/universal_device.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.hub.main.device import common_device_pb2 as v1_dot_hub_dot_main_dot_device_dot_common__device__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/device/universal_device.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n%systems.ajax.a911.grpc.v1.main.deviceP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)v1/hub/main/device/universal_device.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a&v1/hub/main/device/common_device.proto\"\xaf\x0f\n\x0fUniversalDevice\x12J\n\x0b\x63ommon_part\x18\xe8\x07 \x01(\x0b\x32\x34.systems.ajax.a911.grpc.v1.hub.main.CommonDevicePart\x12\x1c\n\x14\x64\x65vice_debug_enabled\x18\x12 \x01(\x08\x12M\n\x08settings\x18\x31 \x03(\x0e\x32;.systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.Setting\x12L\n\x08statuses\x18\x32 \x03(\x0e\x32:.systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.Status\x12I\n\x06\x61larms\x18\x33 \x03(\x0e\x32\x39.systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.Alarm\x12M\n\x07subtype\x18\xc3\x01 \x01(\x0e\x32;.systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.Subtype\"\x95\x04\n\x07Setting\x12\x13\n\x0fNO_SETTING_INFO\x10\x00\x12\r\n\tSETTING_1\x10\x01\x12\r\n\tSETTING_2\x10\x02\x12\r\n\tSETTING_3\x10\x03\x12\r\n\tSETTING_4\x10\x04\x12\r\n\tSETTING_5\x10\x05\x12\r\n\tSETTING_6\x10\x06\x12\r\n\tSETTING_7\x10\x07\x12\r\n\tSETTING_8\x10\x08\x12\r\n\tSETTING_9\x10\t\x12\x0e\n\nSETTING_10\x10\n\x12\x0e\n\nSETTING_11\x10\x0b\x12\x0e\n\nSETTING_12\x10\x0c\x12\x0e\n\nSETTING_13\x10\r\x12\x0e\n\nSETTING_14\x10\x0e\x12\x0e\n\nSETTING_15\x10\x0f\x12\x0e\n\nSETTING_16\x10\x10\x12\x0e\n\nSETTING_17\x10\x11\x12\x0e\n\nSETTING_18\x10\x12\x12\x0e\n\nSETTING_19\x10\x13\x12\x0e\n\nSETTING_20\x10\x14\x12\x0e\n\nSETTING_21\x10\x15\x12\x0e\n\nSETTING_22\x10\x16\x12\x0e\n\nSETTING_23\x10\x17\x12\x0e\n\nSETTING_24\x10\x18\x12\x0e\n\nSETTING_25\x10\x19\x12\x0e\n\nSETTING_26\x10\x1a\x12\x0e\n\nSETTING_27\x10\x1b\x12\x0e\n\nSETTING_28\x10\x1c\x12\x0e\n\nSETTING_29\x10\x1d\x12\x0e\n\nSETTING_30\x10\x1e\x12\x0e\n\nSETTING_31\x10\x1f\x12\x0e\n\nSETTING_32\x10 \"\xf3\x03\n\x06Status\x12\x12\n\x0eNO_STATUS_INFO\x10\x00\x12\x0c\n\x08STATUS_1\x10\x01\x12\x0c\n\x08STATUS_2\x10\x02\x12\x0c\n\x08STATUS_3\x10\x03\x12\x0c\n\x08STATUS_4\x10\x04\x12\x0c\n\x08STATUS_5\x10\x05\x12\x0c\n\x08STATUS_6\x10\x06\x12\x0c\n\x08STATUS_7\x10\x07\x12\x0c\n\x08STATUS_8\x10\x08\x12\x0c\n\x08STATUS_9\x10\t\x12\r\n\tSTATUS_10\x10\n\x12\r\n\tSTATUS_11\x10\x0b\x12\r\n\tSTATUS_12\x10\x0c\x12\r\n\tSTATUS_13\x10\r\x12\r\n\tSTATUS_14\x10\x0e\x12\r\n\tSTATUS_15\x10\x0f\x12\r\n\tSTATUS_16\x10\x10\x12\r\n\tSTATUS_17\x10\x11\x12\r\n\tSTATUS_18\x10\x12\x12\r\n\tSTATUS_19\x10\x13\x12\r\n\tSTATUS_20\x10\x14\x12\r\n\tSTATUS_21\x10\x15\x12\r\n\tSTATUS_22\x10\x16\x12\r\n\tSTATUS_23\x10\x17\x12\r\n\tSTATUS_24\x10\x18\x12\r\n\tSTATUS_25\x10\x19\x12\r\n\tSTATUS_26\x10\x1a\x12\r\n\tSTATUS_27\x10\x1b\x12\r\n\tSTATUS_28\x10\x1c\x12\r\n\tSTATUS_29\x10\x1d\x12\r\n\tSTATUS_30\x10\x1e\x12\r\n\tSTATUS_31\x10\x1f\x12\r\n\tSTATUS_32\x10 \"\xd1\x03\n\x05\x41larm\x12\x11\n\rNO_ALARM_INFO\x10\x00\x12\x0b\n\x07\x41LARM_1\x10\x01\x12\x0b\n\x07\x41LARM_2\x10\x02\x12\x0b\n\x07\x41LARM_3\x10\x03\x12\x0b\n\x07\x41LARM_4\x10\x04\x12\x0b\n\x07\x41LARM_5\x10\x05\x12\x0b\n\x07\x41LARM_6\x10\x06\x12\x0b\n\x07\x41LARM_7\x10\x07\x12\x0b\n\x07\x41LARM_8\x10\x08\x12\x0b\n\x07\x41LARM_9\x10\t\x12\x0c\n\x08\x41LARM_10\x10\n\x12\x0c\n\x08\x41LARM_11\x10\x0b\x12\x0c\n\x08\x41LARM_12\x10\x0c\x12\x0c\n\x08\x41LARM_13\x10\r\x12\x0c\n\x08\x41LARM_14\x10\x0e\x12\x0c\n\x08\x41LARM_15\x10\x0f\x12\x0c\n\x08\x41LARM_16\x10\x10\x12\x0c\n\x08\x41LARM_17\x10\x11\x12\x0c\n\x08\x41LARM_18\x10\x12\x12\x0c\n\x08\x41LARM_19\x10\x13\x12\x0c\n\x08\x41LARM_20\x10\x14\x12\x0c\n\x08\x41LARM_21\x10\x15\x12\x0c\n\x08\x41LARM_22\x10\x16\x12\x0c\n\x08\x41LARM_23\x10\x17\x12\x0c\n\x08\x41LARM_24\x10\x18\x12\x0c\n\x08\x41LARM_25\x10\x19\x12\x0c\n\x08\x41LARM_26\x10\x1a\x12\x0c\n\x08\x41LARM_27\x10\x1b\x12\x0c\n\x08\x41LARM_28\x10\x1c\x12\x0c\n\x08\x41LARM_29\x10\x1d\x12\x0c\n\x08\x41LARM_30\x10\x1e\x12\x0c\n\x08\x41LARM_31\x10\x1f\x12\x0c\n\x08\x41LARM_32\x10 \"\x19\n\x07Subtype\x12\x0e\n\nNO_SUBTYPE\x10\x00\x42\x33\n%systems.ajax.a911.grpc.v1.main.deviceP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[v1_dot_hub_dot_main_dot_device_dot_common__device__pb2.DESCRIPTOR,])



_UNIVERSALDEVICE_SETTING = _descriptor.EnumDescriptor(
  name='Setting',
  full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.Setting',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_SETTING_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_3', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_4', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_5', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_6', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_7', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_8', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_9', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_10', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_11', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_12', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_13', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_14', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_15', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_16', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_17', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_18', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_19', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_20', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_21', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_22', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_23', index=23, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_24', index=24, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_25', index=25, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_26', index=26, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_27', index=27, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_28', index=28, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_29', index=29, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_30', index=30, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_31', index=31, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETTING_32', index=32, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=559,
  serialized_end=1092,
)
_sym_db.RegisterEnumDescriptor(_UNIVERSALDEVICE_SETTING)

_UNIVERSALDEVICE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_STATUS_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_3', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_4', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_5', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_6', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_7', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_8', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_9', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_10', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_11', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_12', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_13', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_14', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_15', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_16', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_17', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_18', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_19', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_20', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_21', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_22', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_23', index=23, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_24', index=24, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_25', index=25, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_26', index=26, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_27', index=27, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_28', index=28, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_29', index=29, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_30', index=30, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_31', index=31, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_32', index=32, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1095,
  serialized_end=1594,
)
_sym_db.RegisterEnumDescriptor(_UNIVERSALDEVICE_STATUS)

_UNIVERSALDEVICE_ALARM = _descriptor.EnumDescriptor(
  name='Alarm',
  full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.Alarm',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ALARM_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_3', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_4', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_5', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_6', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_7', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_8', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_9', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_10', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_11', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_12', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_13', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_14', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_15', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_16', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_17', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_18', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_19', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_20', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_21', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_22', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_23', index=23, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_24', index=24, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_25', index=25, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_26', index=26, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_27', index=27, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_28', index=28, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_29', index=29, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_30', index=30, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_31', index=31, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALARM_32', index=32, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1597,
  serialized_end=2062,
)
_sym_db.RegisterEnumDescriptor(_UNIVERSALDEVICE_ALARM)

_UNIVERSALDEVICE_SUBTYPE = _descriptor.EnumDescriptor(
  name='Subtype',
  full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.Subtype',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_SUBTYPE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2064,
  serialized_end=2089,
)
_sym_db.RegisterEnumDescriptor(_UNIVERSALDEVICE_SUBTYPE)


_UNIVERSALDEVICE = _descriptor.Descriptor(
  name='UniversalDevice',
  full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_part', full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.common_part', index=0,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_debug_enabled', full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.device_debug_enabled', index=1,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settings', full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.settings', index=2,
      number=49, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statuses', full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.statuses', index=3,
      number=50, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alarms', full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.alarms', index=4,
      number=51, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='systems.ajax.a911.grpc.v1.hub.main.UniversalDevice.subtype', index=5,
      number=195, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UNIVERSALDEVICE_SETTING,
    _UNIVERSALDEVICE_STATUS,
    _UNIVERSALDEVICE_ALARM,
    _UNIVERSALDEVICE_SUBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=2089,
)

_UNIVERSALDEVICE.fields_by_name['common_part'].message_type = v1_dot_hub_dot_main_dot_device_dot_common__device__pb2._COMMONDEVICEPART
_UNIVERSALDEVICE.fields_by_name['settings'].enum_type = _UNIVERSALDEVICE_SETTING
_UNIVERSALDEVICE.fields_by_name['statuses'].enum_type = _UNIVERSALDEVICE_STATUS
_UNIVERSALDEVICE.fields_by_name['alarms'].enum_type = _UNIVERSALDEVICE_ALARM
_UNIVERSALDEVICE.fields_by_name['subtype'].enum_type = _UNIVERSALDEVICE_SUBTYPE
_UNIVERSALDEVICE_SETTING.containing_type = _UNIVERSALDEVICE
_UNIVERSALDEVICE_STATUS.containing_type = _UNIVERSALDEVICE
_UNIVERSALDEVICE_ALARM.containing_type = _UNIVERSALDEVICE
_UNIVERSALDEVICE_SUBTYPE.containing_type = _UNIVERSALDEVICE
DESCRIPTOR.message_types_by_name['UniversalDevice'] = _UNIVERSALDEVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UniversalDevice = _reflection.GeneratedProtocolMessageType('UniversalDevice', (_message.Message,), {
  'DESCRIPTOR' : _UNIVERSALDEVICE,
  '__module__' : 'v1.hub.main.device.universal_device_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.UniversalDevice)
  })
_sym_db.RegisterMessage(UniversalDevice)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
