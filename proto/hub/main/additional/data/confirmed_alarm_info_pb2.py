# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/additional/data/confirmed_alarm_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/additional/data/confirmed_alarm_info.proto',
  package='systems.ajax.a911.grpc.v1.hub.main.additional.data',
  syntax='proto3',
  serialized_options=b'\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6v1/hub/main/additional/data/confirmed_alarm_info.proto\x12\x32systems.ajax.a911.grpc.v1.hub.main.additional.data\"-\n\x12\x43onfirmedAlarmInfo\x12\x17\n\x0fparent_alarm_id\x18\x01 \x01(\tB6\n2systems.ajax.a911.grpc.v1.hub.main.additional.dataP\x01\x62\x06proto3'
)




_CONFIRMEDALARMINFO = _descriptor.Descriptor(
  name='ConfirmedAlarmInfo',
  full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.ConfirmedAlarmInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent_alarm_id', full_name='systems.ajax.a911.grpc.v1.hub.main.additional.data.ConfirmedAlarmInfo.parent_alarm_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=110,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['ConfirmedAlarmInfo'] = _CONFIRMEDALARMINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfirmedAlarmInfo = _reflection.GeneratedProtocolMessageType('ConfirmedAlarmInfo', (_message.Message,), {
  'DESCRIPTOR' : _CONFIRMEDALARMINFO,
  '__module__' : 'v1.hub.main.additional.data.confirmed_alarm_info_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.additional.data.ConfirmedAlarmInfo)
  })
_sym_db.RegisterMessage(ConfirmedAlarmInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
