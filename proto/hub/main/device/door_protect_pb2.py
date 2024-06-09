# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/device/door_protect.proto
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
  name='v1/hub/main/device/door_protect.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n%systems.ajax.a911.grpc.v1.main.deviceP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%v1/hub/main/device/door_protect.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x1egoogle/protobuf/wrappers.proto\x1a&v1/hub/main/device/common_device.proto\"\xf6\x06\n\x0b\x44oorProtect\x12J\n\x0b\x63ommon_part\x18\xe8\x07 \x01(\x0b\x32\x34.systems.ajax.a911.grpc.v1.hub.main.CommonDevicePart\x12T\n\x0esiren_triggers\x18. \x03(\x0e\x32<.systems.ajax.a911.grpc.v1.hub.main.DoorProtect.SirenTrigger\x12/\n\x0breed_closed\x18\x31 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x14\x65xtra_contact_closed\x18\x32 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x15\n\ralways_active\x18\x33 \x01(\x08\x12\x1b\n\x13\x65xtra_contact_aware\x18\x34 \x01(\x08\x12\x1a\n\x12reed_contact_aware\x18\x35 \x01(\x08\x12T\n\x0e\x63hime_triggers\x18N \x03(\x0e\x32<.systems.ajax.a911.grpc.v1.hub.main.DoorProtect.ChimeTrigger\x12\x14\n\x0c\x63hime_signal\x18O \x01(\x05\x12I\n\x07subtype\x18\xc3\x01 \x01(\x0e\x32\x37.systems.ajax.a911.grpc.v1.hub.main.DoorProtect.Subtype\x12W\n\x0e\x64oor_protect_s\x18\x80\n \x01(\x0b\x32<.systems.ajax.a911.grpc.v1.hub.main.DoorProtect.DoorProtectSH\x00\x1a#\n\x0c\x44oorProtectS\x12\x13\n\x0b\x66\x61st_tamper\x18s \x01(\x08\"F\n\x0cSirenTrigger\x12\x19\n\x15NO_SIREN_TRIGGER_INFO\x10\x00\x12\x08\n\x04REED\x10\x01\x12\x11\n\rEXTRA_CONTACT\x10\x02\"R\n\x0c\x43himeTrigger\x12\x19\n\x15NO_CHIME_TRIGGER_INFO\x10\x00\x12\x0e\n\nCHIME_REED\x10\x01\x12\x17\n\x13\x43HIME_EXTRA_CONTACT\x10\x02\"-\n\x07Subtype\x12\x0e\n\nNO_SUBTYPE\x10\x00\x12\x12\n\x0e\x44OOR_PROTECT_S\x10\x01\x42\n\n\x08subtypesB3\n%systems.ajax.a911.grpc.v1.main.deviceP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_device_dot_common__device__pb2.DESCRIPTOR,])



_DOORPROTECT_SIRENTRIGGER = _descriptor.EnumDescriptor(
  name='SirenTrigger',
  full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.SirenTrigger',
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
      name='REED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXTRA_CONTACT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=823,
  serialized_end=893,
)
_sym_db.RegisterEnumDescriptor(_DOORPROTECT_SIRENTRIGGER)

_DOORPROTECT_CHIMETRIGGER = _descriptor.EnumDescriptor(
  name='ChimeTrigger',
  full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.ChimeTrigger',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_CHIME_TRIGGER_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHIME_REED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHIME_EXTRA_CONTACT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=895,
  serialized_end=977,
)
_sym_db.RegisterEnumDescriptor(_DOORPROTECT_CHIMETRIGGER)

_DOORPROTECT_SUBTYPE = _descriptor.EnumDescriptor(
  name='Subtype',
  full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.Subtype',
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
      name='DOOR_PROTECT_S', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=979,
  serialized_end=1024,
)
_sym_db.RegisterEnumDescriptor(_DOORPROTECT_SUBTYPE)


_DOORPROTECT_DOORPROTECTS = _descriptor.Descriptor(
  name='DoorProtectS',
  full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.DoorProtectS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fast_tamper', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.DoorProtectS.fast_tamper', index=0,
      number=115, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=786,
  serialized_end=821,
)

_DOORPROTECT = _descriptor.Descriptor(
  name='DoorProtect',
  full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_part', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.common_part', index=0,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='siren_triggers', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.siren_triggers', index=1,
      number=46, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reed_closed', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.reed_closed', index=2,
      number=49, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra_contact_closed', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.extra_contact_closed', index=3,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='always_active', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.always_active', index=4,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra_contact_aware', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.extra_contact_aware', index=5,
      number=52, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reed_contact_aware', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.reed_contact_aware', index=6,
      number=53, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chime_triggers', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.chime_triggers', index=7,
      number=78, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chime_signal', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.chime_signal', index=8,
      number=79, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.subtype', index=9,
      number=195, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='door_protect_s', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.door_protect_s', index=10,
      number=1280, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DOORPROTECT_DOORPROTECTS, ],
  enum_types=[
    _DOORPROTECT_SIRENTRIGGER,
    _DOORPROTECT_CHIMETRIGGER,
    _DOORPROTECT_SUBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='subtypes', full_name='systems.ajax.a911.grpc.v1.hub.main.DoorProtect.subtypes',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=150,
  serialized_end=1036,
)

_DOORPROTECT_DOORPROTECTS.containing_type = _DOORPROTECT
_DOORPROTECT.fields_by_name['common_part'].message_type = v1_dot_hub_dot_main_dot_device_dot_common__device__pb2._COMMONDEVICEPART
_DOORPROTECT.fields_by_name['siren_triggers'].enum_type = _DOORPROTECT_SIRENTRIGGER
_DOORPROTECT.fields_by_name['reed_closed'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_DOORPROTECT.fields_by_name['extra_contact_closed'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_DOORPROTECT.fields_by_name['chime_triggers'].enum_type = _DOORPROTECT_CHIMETRIGGER
_DOORPROTECT.fields_by_name['subtype'].enum_type = _DOORPROTECT_SUBTYPE
_DOORPROTECT.fields_by_name['door_protect_s'].message_type = _DOORPROTECT_DOORPROTECTS
_DOORPROTECT_SIRENTRIGGER.containing_type = _DOORPROTECT
_DOORPROTECT_CHIMETRIGGER.containing_type = _DOORPROTECT
_DOORPROTECT_SUBTYPE.containing_type = _DOORPROTECT
_DOORPROTECT.oneofs_by_name['subtypes'].fields.append(
  _DOORPROTECT.fields_by_name['door_protect_s'])
_DOORPROTECT.fields_by_name['door_protect_s'].containing_oneof = _DOORPROTECT.oneofs_by_name['subtypes']
DESCRIPTOR.message_types_by_name['DoorProtect'] = _DOORPROTECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DoorProtect = _reflection.GeneratedProtocolMessageType('DoorProtect', (_message.Message,), {

  'DoorProtectS' : _reflection.GeneratedProtocolMessageType('DoorProtectS', (_message.Message,), {
    'DESCRIPTOR' : _DOORPROTECT_DOORPROTECTS,
    '__module__' : 'v1.hub.main.device.door_protect_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.DoorProtect.DoorProtectS)
    })
  ,
  'DESCRIPTOR' : _DOORPROTECT,
  '__module__' : 'v1.hub.main.device.door_protect_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.DoorProtect)
  })
_sym_db.RegisterMessage(DoorProtect)
_sym_db.RegisterMessage(DoorProtect.DoorProtectS)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)