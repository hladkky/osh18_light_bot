# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/unread_events_update.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.systems.ajax.logging.proto import log_marker_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/unread_events_update.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\036systems.ajax.a911.grpc.v1.mainP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&v1/hub/main/unread_events_update.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a+systems/ajax/logging/proto/log_marker.proto\">\n\x12UnreadEventsUpdate\x12\x13\n\x06hub_id\x18\x01 \x01(\tB\x03\xf0\x44\x05\x12\x13\n\x0b\x65vent_count\x18\x02 \x01(\x05\x42,\n\x1esystems.ajax.a911.grpc.v1.mainP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2.DESCRIPTOR,])




_UNREADEVENTSUPDATE = _descriptor.Descriptor(
  name='UnreadEventsUpdate',
  full_name='systems.ajax.a911.grpc.v1.hub.main.UnreadEventsUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hub_id', full_name='systems.ajax.a911.grpc.v1.hub.main.UnreadEventsUpdate.hub_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360D\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_count', full_name='systems.ajax.a911.grpc.v1.hub.main.UnreadEventsUpdate.event_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=123,
  serialized_end=185,
)

DESCRIPTOR.message_types_by_name['UnreadEventsUpdate'] = _UNREADEVENTSUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnreadEventsUpdate = _reflection.GeneratedProtocolMessageType('UnreadEventsUpdate', (_message.Message,), {
  'DESCRIPTOR' : _UNREADEVENTSUPDATE,
  '__module__' : 'v1.hub.main.unread_events_update_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.UnreadEventsUpdate)
  })
_sym_db.RegisterMessage(UnreadEventsUpdate)


DESCRIPTOR._options = None
_UNREADEVENTSUPDATE.fields_by_name['hub_id']._options = None
# @@protoc_insertion_point(module_scope)