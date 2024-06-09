# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/common/video/videoedge/mcu/mcu.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.hub.main.device import common_device_pb2 as v1_dot_hub_dot_main_dot_device_dot_common__device__pb2
from proto.hub.main.device import motion_cam_video_base_pb2 as v1_dot_hub_dot_main_dot_device_dot_motion__cam__video__base__pb2
from proto.common.hub.device.common import battery_charged_state_pb2 as v2_dot_common_dot_hub_dot_device_dot_common_dot_battery__charged__state__pb2
from proto.common.hub.device.common import device_transmition_power_mode_pb2 as v2_dot_common_dot_hub_dot_device_dot_common_dot_device__transmition__power__mode__pb2
from proto.common.hub.device.common import jeweller_connection_state_pb2 as v2_dot_common_dot_hub_dot_device_dot_common_dot_jeweller__connection__state__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2/common/video/videoedge/mcu/mcu.proto',
  package='systems.ajax.api.desktop.v2.common.video.videoedge.mcu',
  syntax='proto3',
  serialized_options=b'\n6systems.ajax.api.desktop.v2.common.video.videoedge.mcuP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'v2/common/video/videoedge/mcu/mcu.proto\x12\x36systems.ajax.api.desktop.v2.common.video.videoedge.mcu\x1a&v1/hub/main/device/common_device.proto\x1a.v1/hub/main/device/motion_cam_video_base.proto\x1a\x37v2/common/hub/device/common/battery_charged_state.proto\x1a?v2/common/hub/device/common/device_transmition_power_mode.proto\x1a;v2/common/hub/device/common/jeweller_connection_state.proto\"\x8c\x0c\n\x03Mcu\x12\x61\n\x0e\x62\x61ttery_status\x18\x01 \x01(\x0b\x32I.systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BatteryStatus\x12\x62\n\x14\x65xternal_power_state\x18\x02 \x01(\x0e\x32\x44.systems.ajax.a911.grpc.v1.hub.main.MotionCamVideoBase.ExternalPower\x12W\n\tmcu_state\x18\x03 \x01(\x0e\x32\x44.systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.McuState\x12j\n\x13\x62\x61\x63kup_channel_info\x18\x04 \x01(\x0b\x32M.systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo\x1a\xd5\x01\n\rBatteryStatus\x12Z\n\rbattery_state\x18\x01 \x01(\x0e\x32\x43.systems.ajax.a911.grpc.v1.hub.main.MotionCamVideoBase.BatteryState\x12h\n\x15\x62\x61ttery_charged_state\x18\x02 \x01(\x0e\x32I.systems.ajax.api.desktop.v2.common.hub.device.common.BatteryChargedState\x1a\xa5\x06\n\x11\x42\x61\x63kupChannelInfo\x12p\n\x19jeweller_connection_state\x18\x01 \x01(\x0e\x32M.systems.ajax.api.desktop.v2.common.hub.device.common.JewellerConnectionState\x12g\n\x17jeweller_signal_quality\x18\x02 \x01(\x0e\x32\x46.systems.ajax.a911.grpc.v1.hub.main.CommonDevicePart.DeviceSignalLevel\x12n\n\x1d\x64\x61ta_channel_connection_state\x18\x03 \x01(\x0e\x32G.systems.ajax.a911.grpc.v1.hub.main.MotionCamVideoBase.DataChannelState\x12i\n\x1b\x64\x61ta_channel_signal_quality\x18\x04 \x01(\x0e\x32\x44.systems.ajax.a911.grpc.v1.hub.main.MotionCamVideoBase.SignalQuality\x12w\n\x1d\x64\x65vice_transmition_power_mode\x18\x05 \x01(\x0e\x32P.systems.ajax.api.desktop.v2.common.hub.device.common.DeviceTransmitionPowerMode\x12\x19\n\x11\x61rm_delay_seconds\x18\x06 \x01(\r\x12\x1b\n\x13\x61larm_delay_seconds\x18\x07 \x01(\r\x12$\n\x1cnight_mode_arm_delay_seconds\x18\x08 \x01(\r\x12&\n\x1enight_mode_alarm_delay_seconds\x18\r \x01(\r\x12[\n\x12\x64\x65vice_arming_mode\x18\x0e \x01(\x0e\x32?.systems.ajax.a911.grpc.v1.hub.main.CommonDevicePart.ArmingMode\"y\n\x08McuState\x12\x19\n\x15MCU_STATE_UNSPECIFIED\x10\x00\x12*\n&MCU_STATE_FIRMWARE_UPGRADE_IN_PROGRESS\x10\x01\x12\x10\n\x0cMCU_STATE_OK\x10\x02\x12\x14\n\x10MCU_STATE_FAILED\x10\x03\x42:\n6systems.ajax.api.desktop.v2.common.video.videoedge.mcuP\x01\x62\x06proto3'
  ,
  dependencies=[v1_dot_hub_dot_main_dot_device_dot_common__device__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_device_dot_motion__cam__video__base__pb2.DESCRIPTOR,v2_dot_common_dot_hub_dot_device_dot_common_dot_battery__charged__state__pb2.DESCRIPTOR,v2_dot_common_dot_hub_dot_device_dot_common_dot_device__transmition__power__mode__pb2.DESCRIPTOR,v2_dot_common_dot_hub_dot_device_dot_common_dot_jeweller__connection__state__pb2.DESCRIPTOR,])



_MCU_MCUSTATE = _descriptor.EnumDescriptor(
  name='McuState',
  full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.McuState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MCU_STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MCU_STATE_FIRMWARE_UPGRADE_IN_PROGRESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MCU_STATE_OK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MCU_STATE_FAILED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1798,
  serialized_end=1919,
)
_sym_db.RegisterEnumDescriptor(_MCU_MCUSTATE)


_MCU_BATTERYSTATUS = _descriptor.Descriptor(
  name='BatteryStatus',
  full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BatteryStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='battery_state', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BatteryStatus.battery_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery_charged_state', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BatteryStatus.battery_charged_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=775,
  serialized_end=988,
)

_MCU_BACKUPCHANNELINFO = _descriptor.Descriptor(
  name='BackupChannelInfo',
  full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jeweller_connection_state', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo.jeweller_connection_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jeweller_signal_quality', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo.jeweller_signal_quality', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_channel_connection_state', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo.data_channel_connection_state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_channel_signal_quality', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo.data_channel_signal_quality', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_transmition_power_mode', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo.device_transmition_power_mode', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arm_delay_seconds', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo.arm_delay_seconds', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alarm_delay_seconds', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo.alarm_delay_seconds', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='night_mode_arm_delay_seconds', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo.night_mode_arm_delay_seconds', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='night_mode_alarm_delay_seconds', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo.night_mode_alarm_delay_seconds', index=8,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_arming_mode', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo.device_arming_mode', index=9,
      number=14, type=14, cpp_type=8, label=1,
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
  serialized_start=991,
  serialized_end=1796,
)

_MCU = _descriptor.Descriptor(
  name='Mcu',
  full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='battery_status', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.battery_status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_power_state', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.external_power_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mcu_state', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.mcu_state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup_channel_info', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.backup_channel_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MCU_BATTERYSTATUS, _MCU_BACKUPCHANNELINFO, ],
  enum_types=[
    _MCU_MCUSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=371,
  serialized_end=1919,
)

_MCU_BATTERYSTATUS.fields_by_name['battery_state'].enum_type = v1_dot_hub_dot_main_dot_device_dot_motion__cam__video__base__pb2._MOTIONCAMVIDEOBASE_BATTERYSTATE
_MCU_BATTERYSTATUS.fields_by_name['battery_charged_state'].enum_type = v2_dot_common_dot_hub_dot_device_dot_common_dot_battery__charged__state__pb2._BATTERYCHARGEDSTATE
_MCU_BATTERYSTATUS.containing_type = _MCU
_MCU_BACKUPCHANNELINFO.fields_by_name['jeweller_connection_state'].enum_type = v2_dot_common_dot_hub_dot_device_dot_common_dot_jeweller__connection__state__pb2._JEWELLERCONNECTIONSTATE
_MCU_BACKUPCHANNELINFO.fields_by_name['jeweller_signal_quality'].enum_type = v1_dot_hub_dot_main_dot_device_dot_common__device__pb2._COMMONDEVICEPART_DEVICESIGNALLEVEL
_MCU_BACKUPCHANNELINFO.fields_by_name['data_channel_connection_state'].enum_type = v1_dot_hub_dot_main_dot_device_dot_motion__cam__video__base__pb2._MOTIONCAMVIDEOBASE_DATACHANNELSTATE
_MCU_BACKUPCHANNELINFO.fields_by_name['data_channel_signal_quality'].enum_type = v1_dot_hub_dot_main_dot_device_dot_motion__cam__video__base__pb2._MOTIONCAMVIDEOBASE_SIGNALQUALITY
_MCU_BACKUPCHANNELINFO.fields_by_name['device_transmition_power_mode'].enum_type = v2_dot_common_dot_hub_dot_device_dot_common_dot_device__transmition__power__mode__pb2._DEVICETRANSMITIONPOWERMODE
_MCU_BACKUPCHANNELINFO.fields_by_name['device_arming_mode'].enum_type = v1_dot_hub_dot_main_dot_device_dot_common__device__pb2._COMMONDEVICEPART_ARMINGMODE
_MCU_BACKUPCHANNELINFO.containing_type = _MCU
_MCU.fields_by_name['battery_status'].message_type = _MCU_BATTERYSTATUS
_MCU.fields_by_name['external_power_state'].enum_type = v1_dot_hub_dot_main_dot_device_dot_motion__cam__video__base__pb2._MOTIONCAMVIDEOBASE_EXTERNALPOWER
_MCU.fields_by_name['mcu_state'].enum_type = _MCU_MCUSTATE
_MCU.fields_by_name['backup_channel_info'].message_type = _MCU_BACKUPCHANNELINFO
_MCU_MCUSTATE.containing_type = _MCU
DESCRIPTOR.message_types_by_name['Mcu'] = _MCU
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Mcu = _reflection.GeneratedProtocolMessageType('Mcu', (_message.Message,), {

  'BatteryStatus' : _reflection.GeneratedProtocolMessageType('BatteryStatus', (_message.Message,), {
    'DESCRIPTOR' : _MCU_BATTERYSTATUS,
    '__module__' : 'v2.common.video.videoedge.mcu.mcu_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BatteryStatus)
    })
  ,

  'BackupChannelInfo' : _reflection.GeneratedProtocolMessageType('BackupChannelInfo', (_message.Message,), {
    'DESCRIPTOR' : _MCU_BACKUPCHANNELINFO,
    '__module__' : 'v2.common.video.videoedge.mcu.mcu_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu.BackupChannelInfo)
    })
  ,
  'DESCRIPTOR' : _MCU,
  '__module__' : 'v2.common.video.videoedge.mcu.mcu_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu)
  })
_sym_db.RegisterMessage(Mcu)
_sym_db.RegisterMessage(Mcu.BatteryStatus)
_sym_db.RegisterMessage(Mcu.BackupChannelInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)