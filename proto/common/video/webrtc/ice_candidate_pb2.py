# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/common/video/webrtc/ice_candidate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.systems.ajax.logging.proto import formatting_options_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2/common/video/webrtc/ice_candidate.proto',
  package='systems.ajax.api.desktop.v2.common.video.webrtc',
  syntax='proto3',
  serialized_options=b'P\001\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*v2/common/video/webrtc/ice_candidate.proto\x12/systems.ajax.api.desktop.v2.common.video.webrtc\x1a\x33systems/ajax/logging/proto/formatting_options.proto\"O\n\x0cIceCandidate\x12\x14\n\x07sdp_mid\x18\x01 \x01(\tB\x03\xe8\x44\x01\x12\x17\n\x0fsdp_mline_index\x18\x02 \x01(\r\x12\x10\n\x03sdp\x18\x03 \x01(\tB\x03\xe8\x44\x01\x42\x05P\x01\xba\x02\x00\x62\x06proto3'
  ,
  dependencies=[systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2.DESCRIPTOR,])




_ICECANDIDATE = _descriptor.Descriptor(
  name='IceCandidate',
  full_name='systems.ajax.api.desktop.v2.common.video.webrtc.IceCandidate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sdp_mid', full_name='systems.ajax.api.desktop.v2.common.video.webrtc.IceCandidate.sdp_mid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sdp_mline_index', full_name='systems.ajax.api.desktop.v2.common.video.webrtc.IceCandidate.sdp_mline_index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sdp', full_name='systems.ajax.api.desktop.v2.common.video.webrtc.IceCandidate.sdp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=148,
  serialized_end=227,
)

DESCRIPTOR.message_types_by_name['IceCandidate'] = _ICECANDIDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IceCandidate = _reflection.GeneratedProtocolMessageType('IceCandidate', (_message.Message,), {
  'DESCRIPTOR' : _ICECANDIDATE,
  '__module__' : 'v2.common.video.webrtc.ice_candidate_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.webrtc.IceCandidate)
  })
_sym_db.RegisterMessage(IceCandidate)


DESCRIPTOR._options = None
_ICECANDIDATE.fields_by_name['sdp_mid']._options = None
_ICECANDIDATE.fields_by_name['sdp']._options = None
# @@protoc_insertion_point(module_scope)
