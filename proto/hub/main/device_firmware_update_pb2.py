# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/device_firmware_update.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from proto.hub.main import firmware_id_pb2 as v1_dot_hub_dot_main_dot_firmware__id__pb2
from proto.common.hub import firmware_id_pb2 as v2_dot_common_dot_hub_dot_firmware__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/device_firmware_update.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\"systems.ajax.a911.grpc.hub.v1.mainP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(v1/hub/main/device_firmware_update.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dv1/hub/main/firmware_id.proto\x1a\x1fv2/common/hub/firmware_id.proto\"\xca\x04\n\x14\x44\x65viceFirmwareUpdate\x12\x11\n\tdevice_id\x18\x03 \x01(\t\x12O\n\x06status\x18\x04 \x01(\x0b\x32?.systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.Status\x12\x43\n\x0b\x66irmware_id\x18\x05 \x01(\x0b\x32..systems.ajax.a911.grpc.v1.hub.main.FirmwareId\x12J\n\x0e\x66irmware_id_v2\x18\x07 \x01(\x0b\x32\x32.systems.ajax.api.desktop.v2.common.hub.FirmwareId\x12/\n\x0bis_critical\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1a\x8b\x02\n\x06Status\x12-\n\x0bnot_started\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x15\n\x0b\x64ownloading\x18\x02 \x01(\x05H\x00\x12,\n\ndownloaded\x18\x03 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12,\n\ninstalling\x18\x04 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12+\n\tcompleted\x18\x05 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12(\n\x06\x66\x61iled\x18\x06 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x42\x08\n\x06statusB&\n\"systems.ajax.a911.grpc.hub.v1.mainP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_firmware__id__pb2.DESCRIPTOR,v2_dot_common_dot_hub_dot_firmware__id__pb2.DESCRIPTOR,])




_DEVICEFIRMWAREUPDATE_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='not_started', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.Status.not_started', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downloading', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.Status.downloading', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downloaded', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.Status.downloaded', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='installing', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.Status.installing', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completed', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.Status.completed', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failed', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.Status.failed', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='status', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.Status.status',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=525,
  serialized_end=792,
)

_DEVICEFIRMWAREUPDATE = _descriptor.Descriptor(
  name='DeviceFirmwareUpdate',
  full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.device_id', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.status', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='firmware_id', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.firmware_id', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='firmware_id_v2', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.firmware_id_v2', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_critical', full_name='systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.is_critical', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DEVICEFIRMWAREUPDATE_STATUS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=792,
)

_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['not_started'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['downloaded'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['installing'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['completed'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['failed'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_DEVICEFIRMWAREUPDATE_STATUS.containing_type = _DEVICEFIRMWAREUPDATE
_DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status'].fields.append(
  _DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['not_started'])
_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['not_started'].containing_oneof = _DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status']
_DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status'].fields.append(
  _DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['downloading'])
_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['downloading'].containing_oneof = _DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status']
_DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status'].fields.append(
  _DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['downloaded'])
_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['downloaded'].containing_oneof = _DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status']
_DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status'].fields.append(
  _DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['installing'])
_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['installing'].containing_oneof = _DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status']
_DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status'].fields.append(
  _DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['completed'])
_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['completed'].containing_oneof = _DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status']
_DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status'].fields.append(
  _DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['failed'])
_DEVICEFIRMWAREUPDATE_STATUS.fields_by_name['failed'].containing_oneof = _DEVICEFIRMWAREUPDATE_STATUS.oneofs_by_name['status']
_DEVICEFIRMWAREUPDATE.fields_by_name['status'].message_type = _DEVICEFIRMWAREUPDATE_STATUS
_DEVICEFIRMWAREUPDATE.fields_by_name['firmware_id'].message_type = v1_dot_hub_dot_main_dot_firmware__id__pb2._FIRMWAREID
_DEVICEFIRMWAREUPDATE.fields_by_name['firmware_id_v2'].message_type = v2_dot_common_dot_hub_dot_firmware__id__pb2._FIRMWAREID
_DEVICEFIRMWAREUPDATE.fields_by_name['is_critical'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['DeviceFirmwareUpdate'] = _DEVICEFIRMWAREUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceFirmwareUpdate = _reflection.GeneratedProtocolMessageType('DeviceFirmwareUpdate', (_message.Message,), {

  'Status' : _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
    'DESCRIPTOR' : _DEVICEFIRMWAREUPDATE_STATUS,
    '__module__' : 'v1.hub.main.device_firmware_update_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate.Status)
    })
  ,
  'DESCRIPTOR' : _DEVICEFIRMWAREUPDATE,
  '__module__' : 'v1.hub.main.device_firmware_update_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate)
  })
_sym_db.RegisterMessage(DeviceFirmwareUpdate)
_sym_db.RegisterMessage(DeviceFirmwareUpdate.Status)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)