# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/device/motion_protect_outdoor.proto
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
  name='v1/hub/main/device/motion_protect_outdoor.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n%systems.ajax.a911.grpc.v1.main.deviceP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/v1/hub/main/device/motion_protect_outdoor.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x1egoogle/protobuf/wrappers.proto\x1a&v1/hub/main/device/common_device.proto\"\x9d\x04\n\x14MotionProtectOutdoor\x12J\n\x0b\x63ommon_part\x18\xe8\x07 \x01(\x0b\x32\x34.systems.ajax.a911.grpc.v1.hub.main.CommonDevicePart\x12]\n\x0esiren_triggers\x18. \x03(\x0e\x32\x45.systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.SirenTrigger\x12\x13\n\x0bsensitivity\x18\x32 \x01(\x05\x12\x15\n\ralways_active\x18\x33 \x01(\x08\x12\x13\n\x0b\x61ntimasking\x18\x41 \x01(\x08\x12*\n\x06masked\x18\x42 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x12\x65xternally_powered\x18\x44 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12R\n\x07subtype\x18\xc3\x01 \x01(\x0e\x32@.systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.Subtype\"F\n\x0cSirenTrigger\x12\x19\n\x15NO_SIREN_TRIGGER_INFO\x10\x00\x12\n\n\x06MOTION\x10\x01\x12\x0f\n\x0b\x41NTIMASKING\x10\x02\"\x19\n\x07Subtype\x12\x0e\n\nNO_SUBTYPE\x10\x00\x42\x33\n%systems.ajax.a911.grpc.v1.main.deviceP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_device_dot_common__device__pb2.DESCRIPTOR,])



_MOTIONPROTECTOUTDOOR_SIRENTRIGGER = _descriptor.EnumDescriptor(
  name='SirenTrigger',
  full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.SirenTrigger',
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
      name='MOTION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANTIMASKING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=604,
  serialized_end=674,
)
_sym_db.RegisterEnumDescriptor(_MOTIONPROTECTOUTDOOR_SIRENTRIGGER)

_MOTIONPROTECTOUTDOOR_SUBTYPE = _descriptor.EnumDescriptor(
  name='Subtype',
  full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.Subtype',
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
  serialized_start=676,
  serialized_end=701,
)
_sym_db.RegisterEnumDescriptor(_MOTIONPROTECTOUTDOOR_SUBTYPE)


_MOTIONPROTECTOUTDOOR = _descriptor.Descriptor(
  name='MotionProtectOutdoor',
  full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_part', full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.common_part', index=0,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='siren_triggers', full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.siren_triggers', index=1,
      number=46, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensitivity', full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.sensitivity', index=2,
      number=50, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='always_active', full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.always_active', index=3,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='antimasking', full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.antimasking', index=4,
      number=65, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='masked', full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.masked', index=5,
      number=66, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='externally_powered', full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.externally_powered', index=6,
      number=68, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor.subtype', index=7,
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
    _MOTIONPROTECTOUTDOOR_SIRENTRIGGER,
    _MOTIONPROTECTOUTDOOR_SUBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=701,
)

_MOTIONPROTECTOUTDOOR.fields_by_name['common_part'].message_type = v1_dot_hub_dot_main_dot_device_dot_common__device__pb2._COMMONDEVICEPART
_MOTIONPROTECTOUTDOOR.fields_by_name['siren_triggers'].enum_type = _MOTIONPROTECTOUTDOOR_SIRENTRIGGER
_MOTIONPROTECTOUTDOOR.fields_by_name['masked'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MOTIONPROTECTOUTDOOR.fields_by_name['externally_powered'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MOTIONPROTECTOUTDOOR.fields_by_name['subtype'].enum_type = _MOTIONPROTECTOUTDOOR_SUBTYPE
_MOTIONPROTECTOUTDOOR_SIRENTRIGGER.containing_type = _MOTIONPROTECTOUTDOOR
_MOTIONPROTECTOUTDOOR_SUBTYPE.containing_type = _MOTIONPROTECTOUTDOOR
DESCRIPTOR.message_types_by_name['MotionProtectOutdoor'] = _MOTIONPROTECTOUTDOOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MotionProtectOutdoor = _reflection.GeneratedProtocolMessageType('MotionProtectOutdoor', (_message.Message,), {
  'DESCRIPTOR' : _MOTIONPROTECTOUTDOOR,
  '__module__' : 'v1.hub.main.device.motion_protect_outdoor_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.MotionProtectOutdoor)
  })
_sym_db.RegisterMessage(MotionProtectOutdoor)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
