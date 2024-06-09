# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/common/video/scenario/target_video_edge.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2/common/video/scenario/target_video_edge.proto',
  package='systems.ajax.api.desktop.v2.common.video.scenario',
  syntax='proto3',
  serialized_options=b'P\001\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0v2/common/video/scenario/target_video_edge.proto\x12\x31systems.ajax.api.desktop.v2.common.video.scenario\"|\n\x0fTargetVideoEdge\x12\x15\n\rvideo_edge_id\x18\x01 \x01(\t\x12R\n\x08\x63hannels\x18\x02 \x03(\x0b\x32@.systems.ajax.api.desktop.v2.common.video.scenario.TargetChannel\"#\n\rTargetChannel\x12\x12\n\nchannel_id\x18\x01 \x01(\tB\x05P\x01\xba\x02\x00\x62\x06proto3'
)




_TARGETVIDEOEDGE = _descriptor.Descriptor(
  name='TargetVideoEdge',
  full_name='systems.ajax.api.desktop.v2.common.video.scenario.TargetVideoEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_edge_id', full_name='systems.ajax.api.desktop.v2.common.video.scenario.TargetVideoEdge.video_edge_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='systems.ajax.api.desktop.v2.common.video.scenario.TargetVideoEdge.channels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=103,
  serialized_end=227,
)


_TARGETCHANNEL = _descriptor.Descriptor(
  name='TargetChannel',
  full_name='systems.ajax.api.desktop.v2.common.video.scenario.TargetChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='systems.ajax.api.desktop.v2.common.video.scenario.TargetChannel.channel_id', index=0,
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
  serialized_start=229,
  serialized_end=264,
)

_TARGETVIDEOEDGE.fields_by_name['channels'].message_type = _TARGETCHANNEL
DESCRIPTOR.message_types_by_name['TargetVideoEdge'] = _TARGETVIDEOEDGE
DESCRIPTOR.message_types_by_name['TargetChannel'] = _TARGETCHANNEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetVideoEdge = _reflection.GeneratedProtocolMessageType('TargetVideoEdge', (_message.Message,), {
  'DESCRIPTOR' : _TARGETVIDEOEDGE,
  '__module__' : 'v2.common.video.scenario.target_video_edge_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.scenario.TargetVideoEdge)
  })
_sym_db.RegisterMessage(TargetVideoEdge)

TargetChannel = _reflection.GeneratedProtocolMessageType('TargetChannel', (_message.Message,), {
  'DESCRIPTOR' : _TARGETCHANNEL,
  '__module__' : 'v2.common.video.scenario.target_video_edge_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.scenario.TargetChannel)
  })
_sym_db.RegisterMessage(TargetChannel)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)