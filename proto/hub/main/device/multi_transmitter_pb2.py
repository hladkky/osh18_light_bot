# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/device/multi_transmitter.proto
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
  name='v1/hub/main/device/multi_transmitter.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n%systems.ajax.a911.grpc.v1.main.deviceP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*v1/hub/main/device/multi_transmitter.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x1egoogle/protobuf/wrappers.proto\x1a&v1/hub/main/device/common_device.proto\"\xbe\x06\n\x10MultiTransmitter\x12J\n\x0b\x63ommon_part\x18\xe8\x07 \x01(\x0b\x32\x34.systems.ajax.a911.grpc.v1.hub.main.CommonDevicePart\x12\x16\n\x0e\x65xternal_power\x18\x31 \x01(\x08\x12\x36\n\x11\x65xternal_power_v2\x18\x90\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12$\n\x1c\x65xternal_sensor_power_broken\x18\x33 \x01(\x08\x12\x44\n\x1f\x65xternal_sensor_power_broken_v2\x18\xb0\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x18\n\x10\x62\x61ttery_charging\x18\x34 \x01(\x08\x12\x38\n\x13\x62\x61ttery_charging_v2\x18\xc0\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x16\n\x0e\x62\x61ttery_broken\x18\x35 \x01(\x08\x12\x36\n\x11\x62\x61ttery_broken_v2\x18\xd0\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n$external_fire_notifiers_power_broken\x18\x37 \x01(\x08\x12L\n\'external_fire_notifiers_power_broken_v2\x18\xf0\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12Y\n\x0esiren_triggers\x18. \x03(\x0e\x32\x41.systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.SirenTrigger\x12N\n\x07subtype\x18\xc3\x01 \x01(\x0e\x32<.systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.Subtype\"<\n\x0cSirenTrigger\x12\x19\n\x15NO_SIREN_TRIGGER_INFO\x10\x00\x12\x11\n\rSHORT_CIRCUIT\x10\x01\"\x19\n\x07Subtype\x12\x0e\n\nNO_SUBTYPE\x10\x00\x42\x33\n%systems.ajax.a911.grpc.v1.main.deviceP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_device_dot_common__device__pb2.DESCRIPTOR,])



_MULTITRANSMITTER_SIRENTRIGGER = _descriptor.EnumDescriptor(
  name='SirenTrigger',
  full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.SirenTrigger',
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
      name='SHORT_CIRCUIT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=898,
  serialized_end=958,
)
_sym_db.RegisterEnumDescriptor(_MULTITRANSMITTER_SIRENTRIGGER)

_MULTITRANSMITTER_SUBTYPE = _descriptor.EnumDescriptor(
  name='Subtype',
  full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.Subtype',
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
  serialized_start=960,
  serialized_end=985,
)
_sym_db.RegisterEnumDescriptor(_MULTITRANSMITTER_SUBTYPE)


_MULTITRANSMITTER = _descriptor.Descriptor(
  name='MultiTransmitter',
  full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_part', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.common_part', index=0,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_power', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.external_power', index=1,
      number=49, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_power_v2', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.external_power_v2', index=2,
      number=784, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_sensor_power_broken', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.external_sensor_power_broken', index=3,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_sensor_power_broken_v2', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.external_sensor_power_broken_v2', index=4,
      number=816, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery_charging', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.battery_charging', index=5,
      number=52, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery_charging_v2', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.battery_charging_v2', index=6,
      number=832, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery_broken', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.battery_broken', index=7,
      number=53, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery_broken_v2', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.battery_broken_v2', index=8,
      number=848, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_fire_notifiers_power_broken', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.external_fire_notifiers_power_broken', index=9,
      number=55, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_fire_notifiers_power_broken_v2', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.external_fire_notifiers_power_broken_v2', index=10,
      number=880, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='siren_triggers', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.siren_triggers', index=11,
      number=46, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter.subtype', index=12,
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
    _MULTITRANSMITTER_SIRENTRIGGER,
    _MULTITRANSMITTER_SUBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=985,
)

_MULTITRANSMITTER.fields_by_name['common_part'].message_type = v1_dot_hub_dot_main_dot_device_dot_common__device__pb2._COMMONDEVICEPART
_MULTITRANSMITTER.fields_by_name['external_power_v2'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MULTITRANSMITTER.fields_by_name['external_sensor_power_broken_v2'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MULTITRANSMITTER.fields_by_name['battery_charging_v2'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MULTITRANSMITTER.fields_by_name['battery_broken_v2'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MULTITRANSMITTER.fields_by_name['external_fire_notifiers_power_broken_v2'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MULTITRANSMITTER.fields_by_name['siren_triggers'].enum_type = _MULTITRANSMITTER_SIRENTRIGGER
_MULTITRANSMITTER.fields_by_name['subtype'].enum_type = _MULTITRANSMITTER_SUBTYPE
_MULTITRANSMITTER_SIRENTRIGGER.containing_type = _MULTITRANSMITTER
_MULTITRANSMITTER_SUBTYPE.containing_type = _MULTITRANSMITTER
DESCRIPTOR.message_types_by_name['MultiTransmitter'] = _MULTITRANSMITTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MultiTransmitter = _reflection.GeneratedProtocolMessageType('MultiTransmitter', (_message.Message,), {
  'DESCRIPTOR' : _MULTITRANSMITTER,
  '__module__' : 'v1.hub.main.device.multi_transmitter_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.MultiTransmitter)
  })
_sym_db.RegisterMessage(MultiTransmitter)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)