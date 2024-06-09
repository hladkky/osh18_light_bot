# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/common/video/videoedge/video_edge.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common.video.videoedge.about import about_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_about_dot_about__pb2
from proto.common.video.videoedge.archive import archive_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_archive_dot_archive__pb2
from proto.common.video.videoedge.channel import channel_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_channel_dot_channel__pb2
from proto.common.video.videoedge.detector import detector_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_detector_dot_detector__pb2
from proto.common.video.videoedge.diagnostics import diagnostics_settings_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_diagnostics_dot_diagnostics__settings__pb2
from proto.common.video.videoedge.firmware import firmware_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_firmware_dot_firmware__pb2
from proto.common.video.videoedge.leds import leds_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_leds_dot_leds__pb2
from proto.common.video.videoedge.mediadevice import media_device_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_mediadevice_dot_media__device__pb2
from proto.common.video.videoedge.network import network_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_network_dot_network__pb2
from proto.common.video.videoedge.network import network_interface_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_network_dot_network__interface__pb2
from proto.common.video.videoedge.storage import storage_device_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_storage_dot_storage__device__pb2
from proto.common.video.videoedge.system import system_info_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_system_dot_system__info__pb2
from proto.common.video.videoedge.spacesettings import video_edge_space_settings_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_spacesettings_dot_video__edge__space__settings__pb2
from proto.common.video.videoedge.storage import storage_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_storage_dot_storage__pb2
from proto.systems.ajax.logging.proto import log_marker_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2
from proto.systems.ajax.logging.proto import formatting_options_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2
from proto.common.video.videoedge.mcu import mcu_pb2 as v2_dot_common_dot_video_dot_videoedge_dot_mcu_dot_mcu__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2/common/video/videoedge/video_edge.proto',
  package='systems.ajax.api.desktop.v2.common.video.videoedge',
  syntax='proto3',
  serialized_options=b'P\001\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*v2/common/video/videoedge/video_edge.proto\x12\x32systems.ajax.api.desktop.v2.common.video.videoedge\x1a+v2/common/video/videoedge/about/about.proto\x1a/v2/common/video/videoedge/archive/archive.proto\x1a/v2/common/video/videoedge/channel/channel.proto\x1a\x31v2/common/video/videoedge/detector/detector.proto\x1a@v2/common/video/videoedge/diagnostics/diagnostics_settings.proto\x1a\x31v2/common/video/videoedge/firmware/firmware.proto\x1a)v2/common/video/videoedge/leds/leds.proto\x1a\x38v2/common/video/videoedge/mediadevice/media_device.proto\x1a/v2/common/video/videoedge/network/network.proto\x1a\x39v2/common/video/videoedge/network/network_interface.proto\x1a\x36v2/common/video/videoedge/storage/storage_device.proto\x1a\x32v2/common/video/videoedge/system/system_info.proto\x1aGv2/common/video/videoedge/spacesettings/video_edge_space_settings.proto\x1a/v2/common/video/videoedge/storage/storage.proto\x1a+systems/ajax/logging/proto/log_marker.proto\x1a\x33systems/ajax/logging/proto/formatting_options.proto\x1a\'v2/common/video/videoedge/mcu/mcu.proto\"\xf3\x0b\n\tVideoEdge\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xf0\x44\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12]\n\x10\x63onnection_state\x18\x03 \x01(\x0e\x32\x43.systems.ajax.api.desktop.v2.common.video.videoedge.ConnectionState\x12Y\n\x07\x61rchive\x18\x04 \x01(\x0b\x32\x43.systems.ajax.api.desktop.v2.common.video.videoedge.archive.ArchiveB\x03\xe8\x44\x01\x12\\\n\x07\x64\x65vices\x18\x05 \x03(\x0b\x32K.systems.ajax.api.desktop.v2.common.video.videoedge.mediadevice.MediaDevice\x12U\n\x08\x63hannels\x18\x06 \x03(\x0b\x32\x43.systems.ajax.api.desktop.v2.common.video.videoedge.channel.Channel\x12X\n\tdetectors\x18\x07 \x03(\x0b\x32\x45.systems.ajax.api.desktop.v2.common.video.videoedge.detector.Detector\x12T\n\x07network\x18\x08 \x01(\x0b\x32\x43.systems.ajax.api.desktop.v2.common.video.videoedge.network.Network\x12v\n\x14\x64iagnostics_settings\x18\t \x01(\x0b\x32S.systems.ajax.api.desktop.v2.common.video.videoedge.diagnostics.DiagnosticsSettingsB\x03\xe8\x44\x01\x12Z\n\x0bsystem_info\x18\n \x01(\x0b\x32\x45.systems.ajax.api.desktop.v2.common.video.videoedge.system.SystemInfo\x12h\n\x12network_interfaces\x18\x0b \x03(\x0b\x32L.systems.ajax.api.desktop.v2.common.video.videoedge.network.NetworkInterface\x12\x62\n\x0fstorage_devices\x18\x0c \x03(\x0b\x32I.systems.ajax.api.desktop.v2.common.video.videoedge.storage.StorageDevice\x12W\n\x08\x66irmware\x18\r \x01(\x0b\x32\x45.systems.ajax.api.desktop.v2.common.video.videoedge.firmware.Firmware\x12N\n\x05\x61\x62out\x18\x0e \x01(\x0b\x32?.systems.ajax.api.desktop.v2.common.video.videoedge.about.About\x12K\n\x04leds\x18\x0f \x01(\x0b\x32=.systems.ajax.api.desktop.v2.common.video.videoedge.leds.Leds\x12T\n\x07storage\x18\x10 \x01(\x0b\x32\x43.systems.ajax.api.desktop.v2.common.video.videoedge.storage.Storage\x12H\n\x03mcu\x18\x11 \x01(\x0b\x32;.systems.ajax.api.desktop.v2.common.video.videoedge.mcu.Mcu\x12p\n\x0espace_settings\x18\x64 \x01(\x0b\x32X.systems.ajax.api.desktop.v2.common.video.videoedge.spacesettings.VideoEdgeSpaceSettings*4\n\x0f\x43onnectionState\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07OFFLINE\x10\x01\x12\n\n\x06ONLINE\x10\x02\x42\x05P\x01\xba\x02\x00\x62\x06proto3'
  ,
  dependencies=[v2_dot_common_dot_video_dot_videoedge_dot_about_dot_about__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_archive_dot_archive__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_channel_dot_channel__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_detector_dot_detector__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_diagnostics_dot_diagnostics__settings__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_firmware_dot_firmware__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_leds_dot_leds__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_mediadevice_dot_media__device__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_network_dot_network__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_network_dot_network__interface__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_storage_dot_storage__device__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_system_dot_system__info__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_spacesettings_dot_video__edge__space__settings__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_storage_dot_storage__pb2.DESCRIPTOR,systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2.DESCRIPTOR,systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2.DESCRIPTOR,v2_dot_common_dot_video_dot_videoedge_dot_mcu_dot_mcu__pb2.DESCRIPTOR,])

_CONNECTIONSTATE = _descriptor.EnumDescriptor(
  name='ConnectionState',
  full_name='systems.ajax.api.desktop.v2.common.video.videoedge.ConnectionState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OFFLINE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONLINE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2513,
  serialized_end=2565,
)
_sym_db.RegisterEnumDescriptor(_CONNECTIONSTATE)

ConnectionState = enum_type_wrapper.EnumTypeWrapper(_CONNECTIONSTATE)
NONE = 0
OFFLINE = 1
ONLINE = 2



_VIDEOEDGE = _descriptor.Descriptor(
  name='VideoEdge',
  full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_state', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.connection_state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='archive', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.archive', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='devices', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.devices', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.channels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detectors', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.detectors', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.network', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='diagnostics_settings', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.diagnostics_settings', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system_info', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.system_info', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_interfaces', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.network_interfaces', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storage_devices', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.storage_devices', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='firmware', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.firmware', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='about', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.about', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leds', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.leds', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storage', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.storage', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mcu', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.mcu', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='space_settings', full_name='systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge.space_settings', index=17,
      number=100, type=11, cpp_type=10, label=1,
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
  serialized_start=988,
  serialized_end=2511,
)

_VIDEOEDGE.fields_by_name['connection_state'].enum_type = _CONNECTIONSTATE
_VIDEOEDGE.fields_by_name['archive'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_archive_dot_archive__pb2._ARCHIVE
_VIDEOEDGE.fields_by_name['devices'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_mediadevice_dot_media__device__pb2._MEDIADEVICE
_VIDEOEDGE.fields_by_name['channels'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_channel_dot_channel__pb2._CHANNEL
_VIDEOEDGE.fields_by_name['detectors'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_detector_dot_detector__pb2._DETECTOR
_VIDEOEDGE.fields_by_name['network'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_network_dot_network__pb2._NETWORK
_VIDEOEDGE.fields_by_name['diagnostics_settings'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_diagnostics_dot_diagnostics__settings__pb2._DIAGNOSTICSSETTINGS
_VIDEOEDGE.fields_by_name['system_info'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_system_dot_system__info__pb2._SYSTEMINFO
_VIDEOEDGE.fields_by_name['network_interfaces'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_network_dot_network__interface__pb2._NETWORKINTERFACE
_VIDEOEDGE.fields_by_name['storage_devices'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_storage_dot_storage__device__pb2._STORAGEDEVICE
_VIDEOEDGE.fields_by_name['firmware'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_firmware_dot_firmware__pb2._FIRMWARE
_VIDEOEDGE.fields_by_name['about'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_about_dot_about__pb2._ABOUT
_VIDEOEDGE.fields_by_name['leds'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_leds_dot_leds__pb2._LEDS
_VIDEOEDGE.fields_by_name['storage'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_storage_dot_storage__pb2._STORAGE
_VIDEOEDGE.fields_by_name['mcu'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_mcu_dot_mcu__pb2._MCU
_VIDEOEDGE.fields_by_name['space_settings'].message_type = v2_dot_common_dot_video_dot_videoedge_dot_spacesettings_dot_video__edge__space__settings__pb2._VIDEOEDGESPACESETTINGS
DESCRIPTOR.message_types_by_name['VideoEdge'] = _VIDEOEDGE
DESCRIPTOR.enum_types_by_name['ConnectionState'] = _CONNECTIONSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoEdge = _reflection.GeneratedProtocolMessageType('VideoEdge', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOEDGE,
  '__module__' : 'v2.common.video.videoedge.video_edge_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.api.desktop.v2.common.video.videoedge.VideoEdge)
  })
_sym_db.RegisterMessage(VideoEdge)


DESCRIPTOR._options = None
_VIDEOEDGE.fields_by_name['id']._options = None
_VIDEOEDGE.fields_by_name['archive']._options = None
_VIDEOEDGE.fields_by_name['diagnostics_settings']._options = None
# @@protoc_insertion_point(module_scope)
