# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/device/fire_protect.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from proto.hub.main.device import common_device_pb2 as v1_dot_hub_dot_main_dot_device_dot_common__device__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/device/fire_protect.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n%systems.ajax.a911.grpc.v1.main.deviceP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%v1/hub/main/device/fire_protect.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x1egoogle/protobuf/wrappers.proto\x1a&v1/hub/main/device/common_device.proto\"\xfa\x07\n\x0b\x46ireProtect\x12J\n\x0b\x63ommon_part\x18\xe8\x07 \x01(\x0b\x32\x34.systems.ajax.a911.grpc.v1.hub.main.CommonDevicePart\x12T\n\x0esiren_triggers\x18. \x03(\x0e\x32<.systems.ajax.a911.grpc.v1.hub.main.FireProtect.SirenTrigger\x12\x38\n\x14smoke_alarm_detected\x18\x31 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12>\n\x1atemperature_alarm_detected\x18\x32 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12;\n\x17\x62\x61\x63kup_battery_inserted\x18\x33 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x18\x62\x61\x63kup_battery_charge_ok\x18\x34 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x15\n\ralways_active\x18\x35 \x01(\x08\x12*\n\"temperature_diff_detection_enabled\x18\x36 \x01(\x08\x12\x36\n\x12\x63\x61mera_malfunction\x18\x37 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x12smoke_camera_dusty\x18\x38 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\'\n\x1fhigh_temperature_alarms_enabled\x18\x39 \x01(\x08\x12\x42\n\x1ehigh_temperature_diff_detected\x18< \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12Q\n\x0c\x62uzzer_state\x18> \x01(\x0e\x32;.systems.ajax.a911.grpc.v1.hub.main.FireProtect.BuzzerState\x12I\n\x07subtype\x18\xc3\x01 \x01(\x0e\x32\x37.systems.ajax.a911.grpc.v1.hub.main.FireProtect.Subtype\"\x1e\n\x0b\x42uzzerState\x12\x07\n\x03OFF\x10\x00\x12\x06\n\x02ON\x10\x01\"[\n\x0cSirenTrigger\x12\x19\n\x15NO_SIREN_TRIGGER_INFO\x10\x00\x12\x0f\n\x0bTEMPERATURE\x10\x01\x12\x14\n\x10TEMPERATURE_DIFF\x10\x02\x12\t\n\x05SMOKE\x10\x03\"\x19\n\x07Subtype\x12\x0e\n\nNO_SUBTYPE\x10\x00\x42\x33\n%systems.ajax.a911.grpc.v1.main.deviceP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_device_dot_common__device__pb2.DESCRIPTOR,])



_FIREPROTECT_BUZZERSTATE = _descriptor.EnumDescriptor(
  name='BuzzerState',
  full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.BuzzerState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OFF', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ON', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1018,
  serialized_end=1048,
)
_sym_db.RegisterEnumDescriptor(_FIREPROTECT_BUZZERSTATE)

_FIREPROTECT_SIRENTRIGGER = _descriptor.EnumDescriptor(
  name='SirenTrigger',
  full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.SirenTrigger',
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
      name='TEMPERATURE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEMPERATURE_DIFF', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SMOKE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1050,
  serialized_end=1141,
)
_sym_db.RegisterEnumDescriptor(_FIREPROTECT_SIRENTRIGGER)

_FIREPROTECT_SUBTYPE = _descriptor.EnumDescriptor(
  name='Subtype',
  full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.Subtype',
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
  serialized_start=1143,
  serialized_end=1168,
)
_sym_db.RegisterEnumDescriptor(_FIREPROTECT_SUBTYPE)


_FIREPROTECT = _descriptor.Descriptor(
  name='FireProtect',
  full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_part', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.common_part', index=0,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='siren_triggers', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.siren_triggers', index=1,
      number=46, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='smoke_alarm_detected', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.smoke_alarm_detected', index=2,
      number=49, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='temperature_alarm_detected', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.temperature_alarm_detected', index=3,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup_battery_inserted', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.backup_battery_inserted', index=4,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup_battery_charge_ok', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.backup_battery_charge_ok', index=5,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='always_active', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.always_active', index=6,
      number=53, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='temperature_diff_detection_enabled', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.temperature_diff_detection_enabled', index=7,
      number=54, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='camera_malfunction', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.camera_malfunction', index=8,
      number=55, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='smoke_camera_dusty', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.smoke_camera_dusty', index=9,
      number=56, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high_temperature_alarms_enabled', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.high_temperature_alarms_enabled', index=10,
      number=57, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high_temperature_diff_detected', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.high_temperature_diff_detected', index=11,
      number=60, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buzzer_state', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.buzzer_state', index=12,
      number=62, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='systems.ajax.a911.grpc.v1.hub.main.FireProtect.subtype', index=13,
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
    _FIREPROTECT_BUZZERSTATE,
    _FIREPROTECT_SIRENTRIGGER,
    _FIREPROTECT_SUBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=1168,
)

_FIREPROTECT.fields_by_name['common_part'].message_type = v1_dot_hub_dot_main_dot_device_dot_common__device__pb2._COMMONDEVICEPART
_FIREPROTECT.fields_by_name['siren_triggers'].enum_type = _FIREPROTECT_SIRENTRIGGER
_FIREPROTECT.fields_by_name['smoke_alarm_detected'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_FIREPROTECT.fields_by_name['temperature_alarm_detected'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_FIREPROTECT.fields_by_name['backup_battery_inserted'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_FIREPROTECT.fields_by_name['backup_battery_charge_ok'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_FIREPROTECT.fields_by_name['camera_malfunction'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_FIREPROTECT.fields_by_name['smoke_camera_dusty'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_FIREPROTECT.fields_by_name['high_temperature_diff_detected'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_FIREPROTECT.fields_by_name['buzzer_state'].enum_type = _FIREPROTECT_BUZZERSTATE
_FIREPROTECT.fields_by_name['subtype'].enum_type = _FIREPROTECT_SUBTYPE
_FIREPROTECT_BUZZERSTATE.containing_type = _FIREPROTECT
_FIREPROTECT_SIRENTRIGGER.containing_type = _FIREPROTECT
_FIREPROTECT_SUBTYPE.containing_type = _FIREPROTECT
DESCRIPTOR.message_types_by_name['FireProtect'] = _FIREPROTECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FireProtect = _reflection.GeneratedProtocolMessageType('FireProtect', (_message.Message,), {
  'DESCRIPTOR' : _FIREPROTECT,
  '__module__' : 'v1.hub.main.device.fire_protect_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.FireProtect)
  })
_sym_db.RegisterMessage(FireProtect)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)