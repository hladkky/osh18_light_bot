# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/device/button.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.hub.main.device import common_device_pb2 as v1_dot_hub_dot_main_dot_device_dot_common__device__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/device/button.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n%systems.ajax.a911.grpc.v1.main.deviceP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fv1/hub/main/device/button.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a&v1/hub/main/device/common_device.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbe\r\n\x06\x42utton\x12J\n\x0b\x63ommon_part\x18\xe8\x07 \x01(\x0b\x32\x34.systems.ajax.a911.grpc.v1.hub.main.CommonDevicePart\x12O\n\x0esiren_triggers\x18. \x03(\x0e\x32\x37.systems.ajax.a911.grpc.v1.hub.main.Button.SirenTrigger\x12J\n\x0b\x62utton_mode\x18\x31 \x01(\x0e\x32\x35.systems.ajax.a911.grpc.v1.hub.main.Button.ButtonMode\x12\x1a\n\x12\x61ssociated_user_id\x18\x32 \x01(\t\x12I\n\nbrightness\x18\x33 \x01(\x0e\x32\x35.systems.ajax.a911.grpc.v1.hub.main.Button.Brightness\x12W\n\x12\x66\x61lse_press_filter\x18\x35 \x01(\x0e\x32;.systems.ajax.a911.grpc.v1.hub.main.Button.FalsePressFilter\x12U\n\x11\x63ustom_alarm_type\x18\x37 \x01(\x0e\x32:.systems.ajax.a911.grpc.v1.hub.main.Button.CustomAlarmType\x12L\n\x0c\x62\x61ttery_ping\x18\x38 \x01(\x0e\x32\x36.systems.ajax.a911.grpc.v1.hub.main.Button.BatteryPing\x12\x34\n\x10last_update_time\x18\x39 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12O\n\x0e\x65vent_settings\x18\x41 \x03(\x0e\x32\x37.systems.ajax.a911.grpc.v1.hub.main.Button.EventSetting\x12Y\n\x13\x62\x61ttery_ping_status\x18\x42 \x01(\x0e\x32<.systems.ajax.a911.grpc.v1.hub.main.Button.BatteryPingStatus\x12\x44\n\x07subtype\x18\xc3\x01 \x01(\x0e\x32\x32.systems.ajax.a911.grpc.v1.hub.main.Button.Subtype\">\n\x0cSirenTrigger\x12\x19\n\x15NO_SIREN_TRIGGER_INFO\x10\x00\x12\x13\n\x0fSECURITY_BUTTON\x10\x01\"a\n\nButtonMode\x12\x17\n\x13NO_BUTTON_MODE_INFO\x10\x00\x12\x10\n\x0cPANIC_BUTTON\x10\x01\x12\x10\n\x0cSMART_BUTTON\x10\x02\x12\x16\n\x12INTERCONNECT_DELAY\x10\x03\"@\n\nBrightness\x12\x16\n\x12NO_BRIGHTNESS_INFO\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x07\n\x03LOW\x10\x02\x12\x08\n\x04HIGH\x10\x04\"a\n\x10\x46\x61lsePressFilter\x12\x1e\n\x1aNO_FALSE_PRESS_FILTER_INFO\x10\x00\x12\x0c\n\x08\x44ISABLED\x10\x01\x12\r\n\tLONG_PUSH\x10\x02\x12\x10\n\x0c\x44OUBLE_CLICK\x10\x03\"\x9a\x01\n\x0f\x43ustomAlarmType\x12\x18\n\x14NO_CUSTOM_ALARM_TYPE\x10\x00\x12\x0c\n\x08\x42URGLARY\x10\x01\x12\x08\n\x04\x46IRE\x10\x02\x12\x0b\n\x07MEDICAL\x10\x03\x12\t\n\x05PANIC\x10\x04\x12\x07\n\x03GAS\x10\x05\x12\x0c\n\x08RESERVED\x10\x06\x12\x0f\n\x0bMALFUNCTION\x10\x07\x12\x08\n\x04LEAK\x10\x08\x12\x0b\n\x07SERVICE\x10\t\"`\n\x0b\x42\x61tteryPing\x12\x1c\n\x18\x42\x41TTERY_PING_UNSPECIFIED\x10\x00\x12\x19\n\x15\x42\x41TTERY_PING_DISABLED\x10\x01\x12\x18\n\x14\x42\x41TTERY_PING_ENABLED\x10\x02\"X\n\x0c\x45ventSetting\x12\x1e\n\x1a\x45VENT_SETTINGS_UNSPECIFIED\x10\x00\x12(\n$EVENT_SETTINGS_PINGS_FAILED_EVENT_EN\x10\x01\"t\n\x11\x42\x61tteryPingStatus\x12#\n\x1f\x42\x41TTERY_PING_STATUS_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x42\x41TTERY_PING_STATUS_OK\x10\x01\x12\x1e\n\x1a\x42\x41TTERY_PING_STATUS_NOT_OK\x10\x02\"\'\n\x07Subtype\x12\x0e\n\nNO_SUBTYPE\x10\x00\x12\x0c\n\x08\x42UTTON_S\x10\x01\x42\x33\n%systems.ajax.a911.grpc.v1.main.deviceP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[v1_dot_hub_dot_main_dot_device_dot_common__device__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_BUTTON_SIRENTRIGGER = _descriptor.EnumDescriptor(
  name='SirenTrigger',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Button.SirenTrigger',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_SIREN_TRIGGER_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SECURITY_BUTTON', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1041,
  serialized_end=1103,
)
_sym_db.RegisterEnumDescriptor(_BUTTON_SIRENTRIGGER)

_BUTTON_BUTTONMODE = _descriptor.EnumDescriptor(
  name='ButtonMode',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Button.ButtonMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_BUTTON_MODE_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PANIC_BUTTON', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SMART_BUTTON', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERCONNECT_DELAY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1105,
  serialized_end=1202,
)
_sym_db.RegisterEnumDescriptor(_BUTTON_BUTTONMODE)

_BUTTON_BRIGHTNESS = _descriptor.EnumDescriptor(
  name='Brightness',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Button.Brightness',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_BRIGHTNESS_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OFF', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1204,
  serialized_end=1268,
)
_sym_db.RegisterEnumDescriptor(_BUTTON_BRIGHTNESS)

_BUTTON_FALSEPRESSFILTER = _descriptor.EnumDescriptor(
  name='FalsePressFilter',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Button.FalsePressFilter',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_FALSE_PRESS_FILTER_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LONG_PUSH', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE_CLICK', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1270,
  serialized_end=1367,
)
_sym_db.RegisterEnumDescriptor(_BUTTON_FALSEPRESSFILTER)

_BUTTON_CUSTOMALARMTYPE = _descriptor.EnumDescriptor(
  name='CustomAlarmType',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Button.CustomAlarmType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_CUSTOM_ALARM_TYPE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BURGLARY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIRE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEDICAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PANIC', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GAS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESERVED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MALFUNCTION', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LEAK', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVICE', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1370,
  serialized_end=1524,
)
_sym_db.RegisterEnumDescriptor(_BUTTON_CUSTOMALARMTYPE)

_BUTTON_BATTERYPING = _descriptor.EnumDescriptor(
  name='BatteryPing',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Button.BatteryPing',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BATTERY_PING_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BATTERY_PING_DISABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BATTERY_PING_ENABLED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1526,
  serialized_end=1622,
)
_sym_db.RegisterEnumDescriptor(_BUTTON_BATTERYPING)

_BUTTON_EVENTSETTING = _descriptor.EnumDescriptor(
  name='EventSetting',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Button.EventSetting',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EVENT_SETTINGS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EVENT_SETTINGS_PINGS_FAILED_EVENT_EN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1624,
  serialized_end=1712,
)
_sym_db.RegisterEnumDescriptor(_BUTTON_EVENTSETTING)

_BUTTON_BATTERYPINGSTATUS = _descriptor.EnumDescriptor(
  name='BatteryPingStatus',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Button.BatteryPingStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BATTERY_PING_STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BATTERY_PING_STATUS_OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BATTERY_PING_STATUS_NOT_OK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1714,
  serialized_end=1830,
)
_sym_db.RegisterEnumDescriptor(_BUTTON_BATTERYPINGSTATUS)

_BUTTON_SUBTYPE = _descriptor.EnumDescriptor(
  name='Subtype',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Button.Subtype',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_SUBTYPE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUTTON_S', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1832,
  serialized_end=1871,
)
_sym_db.RegisterEnumDescriptor(_BUTTON_SUBTYPE)


_BUTTON = _descriptor.Descriptor(
  name='Button',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Button',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_part', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.common_part', index=0,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='siren_triggers', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.siren_triggers', index=1,
      number=46, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='button_mode', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.button_mode', index=2,
      number=49, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='associated_user_id', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.associated_user_id', index=3,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='brightness', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.brightness', index=4,
      number=51, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='false_press_filter', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.false_press_filter', index=5,
      number=53, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_alarm_type', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.custom_alarm_type', index=6,
      number=55, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery_ping', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.battery_ping', index=7,
      number=56, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_update_time', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.last_update_time', index=8,
      number=57, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_settings', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.event_settings', index=9,
      number=65, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery_ping_status', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.battery_ping_status', index=10,
      number=66, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='systems.ajax.a911.grpc.v1.hub.main.Button.subtype', index=11,
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
    _BUTTON_SIRENTRIGGER,
    _BUTTON_BUTTONMODE,
    _BUTTON_BRIGHTNESS,
    _BUTTON_FALSEPRESSFILTER,
    _BUTTON_CUSTOMALARMTYPE,
    _BUTTON_BATTERYPING,
    _BUTTON_EVENTSETTING,
    _BUTTON_BATTERYPINGSTATUS,
    _BUTTON_SUBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=1871,
)

_BUTTON.fields_by_name['common_part'].message_type = v1_dot_hub_dot_main_dot_device_dot_common__device__pb2._COMMONDEVICEPART
_BUTTON.fields_by_name['siren_triggers'].enum_type = _BUTTON_SIRENTRIGGER
_BUTTON.fields_by_name['button_mode'].enum_type = _BUTTON_BUTTONMODE
_BUTTON.fields_by_name['brightness'].enum_type = _BUTTON_BRIGHTNESS
_BUTTON.fields_by_name['false_press_filter'].enum_type = _BUTTON_FALSEPRESSFILTER
_BUTTON.fields_by_name['custom_alarm_type'].enum_type = _BUTTON_CUSTOMALARMTYPE
_BUTTON.fields_by_name['battery_ping'].enum_type = _BUTTON_BATTERYPING
_BUTTON.fields_by_name['last_update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUTTON.fields_by_name['event_settings'].enum_type = _BUTTON_EVENTSETTING
_BUTTON.fields_by_name['battery_ping_status'].enum_type = _BUTTON_BATTERYPINGSTATUS
_BUTTON.fields_by_name['subtype'].enum_type = _BUTTON_SUBTYPE
_BUTTON_SIRENTRIGGER.containing_type = _BUTTON
_BUTTON_BUTTONMODE.containing_type = _BUTTON
_BUTTON_BRIGHTNESS.containing_type = _BUTTON
_BUTTON_FALSEPRESSFILTER.containing_type = _BUTTON
_BUTTON_CUSTOMALARMTYPE.containing_type = _BUTTON
_BUTTON_BATTERYPING.containing_type = _BUTTON
_BUTTON_EVENTSETTING.containing_type = _BUTTON
_BUTTON_BATTERYPINGSTATUS.containing_type = _BUTTON
_BUTTON_SUBTYPE.containing_type = _BUTTON
DESCRIPTOR.message_types_by_name['Button'] = _BUTTON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Button = _reflection.GeneratedProtocolMessageType('Button', (_message.Message,), {
  'DESCRIPTOR' : _BUTTON,
  '__module__' : 'v1.hub.main.device.button_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.Button)
  })
_sym_db.RegisterMessage(Button)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)