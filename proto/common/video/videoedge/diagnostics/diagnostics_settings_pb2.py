# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/common/video/videoedge/diagnostics/diagnostics_settings.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2/common/video/videoedge/diagnostics/diagnostics_settings.proto',
  package='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics',
  syntax='proto3',
  serialized_options=b'P\001\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n@v2/common/video/videoedge/diagnostics/diagnostics_settings.proto\x12>systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics\"\xf8\x02\n\x0fLoggingSettings\x12\x15\n\rlog_max_bytes\x18\x01 \x01(\r\x12\\\n\nroot_level\x18\x02 \x01(\x0e\x32H.systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LogLevel\x12u\n\rmodule_levels\x18\x03 \x03(\x0b\x32^.systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings.ModuleLogLevel\x1ay\n\x0eModuleLogLevel\x12\x0e\n\x06module\x18\x01 \x01(\t\x12W\n\x05level\x18\x02 \x01(\x0e\x32H.systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LogLevel\"\x80\x01\n\x13\x44iagnosticsSettings\x12i\n\x10logging_settings\x18\x01 \x01(\x0b\x32O.systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings*\x81\x01\n\x08LogLevel\x12\x0b\n\x07LL_NONE\x10\x00\x12\n\n\x06LL_OFF\x10\x01\x12\x0c\n\x08LL_FATAL\x10\x02\x12\x0c\n\x08LL_ERROR\x10\x03\x12\x0b\n\x07LL_WARN\x10\x04\x12\x0b\n\x07LL_INFO\x10\x05\x12\x0c\n\x08LL_DEBUG\x10\x06\x12\x0c\n\x08LL_TRACE\x10\x07\x12\n\n\x06LL_ALL\x10\x08\x42\x05P\x01\xba\x02\x00\x62\x06proto3'
)

_LOGLEVEL = _descriptor.EnumDescriptor(
  name='LogLevel',
  full_name='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LogLevel',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LL_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LL_OFF', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LL_FATAL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LL_ERROR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LL_WARN', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LL_INFO', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LL_DEBUG', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LL_TRACE', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LL_ALL', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=643,
  serialized_end=772,
)
_sym_db.RegisterEnumDescriptor(_LOGLEVEL)

LogLevel = enum_type_wrapper.EnumTypeWrapper(_LOGLEVEL)
LL_NONE = 0
LL_OFF = 1
LL_FATAL = 2
LL_ERROR = 3
LL_WARN = 4
LL_INFO = 5
LL_DEBUG = 6
LL_TRACE = 7
LL_ALL = 8



_LOGGINGSETTINGS_MODULELOGLEVEL = _descriptor.Descriptor(
  name='ModuleLogLevel',
  full_name='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings.ModuleLogLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='module', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings.ModuleLogLevel.module', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings.ModuleLogLevel.level', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=388,
  serialized_end=509,
)

_LOGGINGSETTINGS = _descriptor.Descriptor(
  name='LoggingSettings',
  full_name='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_max_bytes', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings.log_max_bytes', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='root_level', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings.root_level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_levels', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings.module_levels', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LOGGINGSETTINGS_MODULELOGLEVEL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=509,
)


_DIAGNOSTICSSETTINGS = _descriptor.Descriptor(
  name='DiagnosticsSettings',
  full_name='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.DiagnosticsSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='logging_settings', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.DiagnosticsSettings.logging_settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=512,
  serialized_end=640,
)

_LOGGINGSETTINGS_MODULELOGLEVEL.fields_by_name['level'].enum_type = _LOGLEVEL
_LOGGINGSETTINGS_MODULELOGLEVEL.containing_type = _LOGGINGSETTINGS
_LOGGINGSETTINGS.fields_by_name['root_level'].enum_type = _LOGLEVEL
_LOGGINGSETTINGS.fields_by_name['module_levels'].message_type = _LOGGINGSETTINGS_MODULELOGLEVEL
_DIAGNOSTICSSETTINGS.fields_by_name['logging_settings'].message_type = _LOGGINGSETTINGS
DESCRIPTOR.message_types_by_name['LoggingSettings'] = _LOGGINGSETTINGS
DESCRIPTOR.message_types_by_name['DiagnosticsSettings'] = _DIAGNOSTICSSETTINGS
DESCRIPTOR.enum_types_by_name['LogLevel'] = _LOGLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoggingSettings = _reflection.GeneratedProtocolMessageType('LoggingSettings', (_message.Message,), {

  'ModuleLogLevel' : _reflection.GeneratedProtocolMessageType('ModuleLogLevel', (_message.Message,), {
    'DESCRIPTOR' : _LOGGINGSETTINGS_MODULELOGLEVEL,
    '__module__' : 'v2.common.video.videoedge.diagnostics.diagnostics_settings_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings.ModuleLogLevel)
    })
  ,
  'DESCRIPTOR' : _LOGGINGSETTINGS,
  '__module__' : 'v2.common.video.videoedge.diagnostics.diagnostics_settings_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.LoggingSettings)
  })
_sym_db.RegisterMessage(LoggingSettings)
_sym_db.RegisterMessage(LoggingSettings.ModuleLogLevel)

DiagnosticsSettings = _reflection.GeneratedProtocolMessageType('DiagnosticsSettings', (_message.Message,), {
  'DESCRIPTOR' : _DIAGNOSTICSSETTINGS,
  '__module__' : 'v2.common.video.videoedge.diagnostics.diagnostics_settings_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.DiagnosticsSettings)
  })
_sym_db.RegisterMessage(DiagnosticsSettings)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
