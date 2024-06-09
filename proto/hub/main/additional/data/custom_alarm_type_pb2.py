# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/additional/data/custom_alarm_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/additional/data/custom_alarm_type.proto',
  package='systems.ajax.a911.grpc.v1.hub.main.additional.data',
  syntax='proto3',
  serialized_options=b'\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3v1/hub/main/additional/data/custom_alarm_type.proto\x12\x32systems.ajax.a911.grpc.v1.hub.main.additional.data\"\xff\x06\n\x13\x43ustomAlarmTypeInfo\x12r\n\x11\x63ustom_alarm_type\x18\x01 \x01(\x0e\x32W.systems.ajax.a911.grpc.v1.hub.main.additional.data.CustomAlarmTypeInfo.CustomAlarmType\"\xf3\x05\n\x0f\x43ustomAlarmType\x12!\n\x1d\x43USTOM_ALARM_TYPE_UNSPECIFIED\x10\x00\x12$\n CUSTOM_ALARM_TYPE_BURGLARY_ALARM\x10\x01\x12 \n\x1c\x43USTOM_ALARM_TYPE_FIRE_ALARM\x10\x02\x12#\n\x1f\x43USTOM_ALARM_TYPE_MEDICAL_ALARM\x10\x03\x12!\n\x1d\x43USTOM_ALARM_TYPE_PANIC_ALARM\x10\x04\x12\x1f\n\x1b\x43USTOM_ALARM_TYPE_GAS_ALARM\x10\x05\x12\x1c\n\x18\x43USTOM_ALARM_TYPE_TAMPER\x10\x06\x12\'\n#CUSTOM_ALARM_TYPE_MALFUNCTION_ALARM\x10\x07\x12\x1a\n\x16\x43USTOM_ALARM_TYPE_LEAK\x10\x08\x12#\n\x1f\x43USTOM_ALARM_TYPE_SERVICE_EVENT\x10\t\x12\x1c\n\x18\x43USTOM_ALARM_TYPE_KEYARM\x10\n\x12\x1c\n\x18\x43USTOM_ALARM_TYPE_BUTTON\x10\x0b\x12\'\n#CUSTOM_ALARM_TYPE_GLASS_BREAK_ALARM\x10\x0c\x12,\n(CUSTOM_ALARM_TYPE_HIGH_TEMPERATURE_ALARM\x10\r\x12+\n\'CUSTOM_ALARM_TYPE_LOW_TEMPERATURE_ALARM\x10\x0e\x12#\n\x1f\x43USTOM_ALARM_TYPE_MASKING_ALARM\x10\x0f\x12\'\n#CUSTOM_ALARM_TYPE_DURESS_CODE_ALARM\x10\x10\x12#\n\x1f\x43USTOM_ALARM_TYPE_SEISMIC_ALARM\x10\x11\x12&\n\"CUSTOM_ALARM_TYPE_BLOCKING_ELEMENT\x10\x12\x12)\n%CUSTOM_ALARM_TYPE_BOLT_SWITCH_CONTACT\x10\x13\x42\x36\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\x01\x62\x06proto3'
)



_CUSTOMALARMTYPEINFO_CUSTOMALARMTYPE = _descriptor.EnumDescriptor(
  name='CustomAlarmType',
  full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.CustomAlarmTypeInfo.CustomAlarmType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_BURGLARY_ALARM', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_FIRE_ALARM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_MEDICAL_ALARM', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_PANIC_ALARM', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_GAS_ALARM', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_TAMPER', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_MALFUNCTION_ALARM', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_LEAK', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_SERVICE_EVENT', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_KEYARM', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_BUTTON', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_GLASS_BREAK_ALARM', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_HIGH_TEMPERATURE_ALARM', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_LOW_TEMPERATURE_ALARM', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_MASKING_ALARM', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_DURESS_CODE_ALARM', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_SEISMIC_ALARM', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_BLOCKING_ELEMENT', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ALARM_TYPE_BOLT_SWITCH_CONTACT', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=248,
  serialized_end=1003,
)
_sym_db.RegisterEnumDescriptor(_CUSTOMALARMTYPEINFO_CUSTOMALARMTYPE)


_CUSTOMALARMTYPEINFO = _descriptor.Descriptor(
  name='CustomAlarmTypeInfo',
  full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.CustomAlarmTypeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='custom_alarm_type', full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.CustomAlarmTypeInfo.custom_alarm_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CUSTOMALARMTYPEINFO_CUSTOMALARMTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=1003,
)

_CUSTOMALARMTYPEINFO.fields_by_name['custom_alarm_type'].enum_type = _CUSTOMALARMTYPEINFO_CUSTOMALARMTYPE
_CUSTOMALARMTYPEINFO_CUSTOMALARMTYPE.containing_type = _CUSTOMALARMTYPEINFO
DESCRIPTOR.message_types_by_name['CustomAlarmTypeInfo'] = _CUSTOMALARMTYPEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomAlarmTypeInfo = _reflection.GeneratedProtocolMessageType('CustomAlarmTypeInfo', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMALARMTYPEINFO,
  '__module__' : 'v1.hub.main.additional.data.custom_alarm_type_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.additional.data.CustomAlarmTypeInfo)
  })
_sym_db.RegisterMessage(CustomAlarmTypeInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
