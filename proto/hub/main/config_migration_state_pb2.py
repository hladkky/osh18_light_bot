# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/config_migration_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.hub.main import object_type_pb2 as v1_dot_hub_dot_main_dot_object__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/config_migration_state.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\036systems.ajax.a911.grpc.v1.mainP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(v1/hub/main/config_migration_state.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x1dv1/hub/main/object_type.proto\"\xb3\n\n\x14\x43onfigMigrationState\x12g\n\x13\x64\x61ta_transfer_state\x18\x01 \x01(\x0e\x32J.systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.DataTransferState\x12z\n\x1dmigration_frame_devices_state\x18\x02 \x01(\x0e\x32S.systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.MigrationFrameDevicesState\x12|\n\x1emigration_button_devices_state\x18\x03 \x01(\x0e\x32T.systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.MigrationButtonDevicesState\x12\x62\n\x10migration_result\x18\x04 \x01(\x0e\x32H.systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.MigrationResult\x12\x44\n\x0bobject_type\x18\xe8\x07 \x01(\x0e\x32..systems.ajax.a911.grpc.v1.hub.main.ObjectType\x12\x0b\n\x02id\x18\xe9\x07 \x01(\t\"o\n\x11\x44\x61taTransferState\x12\x1f\n\x1b\x44\x41TA_TRANSFER_UNKNOWN_STATE\x10\x00\x12\x1d\n\x19\x44\x41TA_TRANSFER_IN_PROGRESS\x10\x02\x12\x1a\n\x16\x44\x41TA_TRANSFER_FINISHED\x10\x03\"\xf0\x01\n\x1aMigrationFrameDevicesState\x12)\n%MIGRATION_FRAME_DEVICES_UNKNOWN_STATE\x10\x00\x12)\n%MIGRATION_FRAME_DEVICES_NOT_AVAILABLE\x10\x01\x12-\n)MIGRATION_FRAME_DEVICES_WAITING_FOR_START\x10\x02\x12\'\n#MIGRATION_FRAME_DEVICES_IN_PROGRESS\x10\x03\x12$\n MIGRATION_FRAME_DEVICES_FINISHED\x10\x04\"\xf6\x01\n\x1bMigrationButtonDevicesState\x12*\n&MIGRATION_BUTTON_DEVICES_UNKNOWN_STATE\x10\x00\x12*\n&MIGRATION_BUTTON_DEVICES_NOT_AVAILABLE\x10\x01\x12.\n*MIGRATION_BUTTON_DEVICES_WAITING_FOR_START\x10\x02\x12(\n$MIGRATION_BUTTON_DEVICES_IN_PROGRESS\x10\x03\x12%\n!MIGRATION_BUTTON_DEVICES_FINISHED\x10\x04\"\xa3\x01\n\x0fMigrationResult\x12 \n\x1cMIGRATION_RESULT_IN_PROGRESS\x10\x00\x12%\n!MIGRATION_RESULT_SERVER_TIMED_OUT\x10\x02\x12 \n\x1cMIGRATION_RESULT_FINISHED_OK\x10\x03\x12%\n!MIGRATION_RESULT_MIGRATION_FAILED\x10\x04\x42,\n\x1esystems.ajax.a911.grpc.v1.mainP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[v1_dot_hub_dot_main_dot_object__type__pb2.DESCRIPTOR,])



_CONFIGMIGRATIONSTATE_DATATRANSFERSTATE = _descriptor.EnumDescriptor(
  name='DataTransferState',
  full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.DataTransferState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DATA_TRANSFER_UNKNOWN_STATE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DATA_TRANSFER_IN_PROGRESS', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DATA_TRANSFER_FINISHED', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=674,
  serialized_end=785,
)
_sym_db.RegisterEnumDescriptor(_CONFIGMIGRATIONSTATE_DATATRANSFERSTATE)

_CONFIGMIGRATIONSTATE_MIGRATIONFRAMEDEVICESSTATE = _descriptor.EnumDescriptor(
  name='MigrationFrameDevicesState',
  full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.MigrationFrameDevicesState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_FRAME_DEVICES_UNKNOWN_STATE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_FRAME_DEVICES_NOT_AVAILABLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_FRAME_DEVICES_WAITING_FOR_START', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_FRAME_DEVICES_IN_PROGRESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_FRAME_DEVICES_FINISHED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=788,
  serialized_end=1028,
)
_sym_db.RegisterEnumDescriptor(_CONFIGMIGRATIONSTATE_MIGRATIONFRAMEDEVICESSTATE)

_CONFIGMIGRATIONSTATE_MIGRATIONBUTTONDEVICESSTATE = _descriptor.EnumDescriptor(
  name='MigrationButtonDevicesState',
  full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.MigrationButtonDevicesState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_BUTTON_DEVICES_UNKNOWN_STATE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_BUTTON_DEVICES_NOT_AVAILABLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_BUTTON_DEVICES_WAITING_FOR_START', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_BUTTON_DEVICES_IN_PROGRESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_BUTTON_DEVICES_FINISHED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1031,
  serialized_end=1277,
)
_sym_db.RegisterEnumDescriptor(_CONFIGMIGRATIONSTATE_MIGRATIONBUTTONDEVICESSTATE)

_CONFIGMIGRATIONSTATE_MIGRATIONRESULT = _descriptor.EnumDescriptor(
  name='MigrationResult',
  full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.MigrationResult',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_RESULT_IN_PROGRESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_RESULT_SERVER_TIMED_OUT', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_RESULT_FINISHED_OK', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION_RESULT_MIGRATION_FAILED', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1280,
  serialized_end=1443,
)
_sym_db.RegisterEnumDescriptor(_CONFIGMIGRATIONSTATE_MIGRATIONRESULT)


_CONFIGMIGRATIONSTATE = _descriptor.Descriptor(
  name='ConfigMigrationState',
  full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_transfer_state', full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.data_transfer_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='migration_frame_devices_state', full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.migration_frame_devices_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='migration_button_devices_state', full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.migration_button_devices_state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='migration_result', full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.migration_result', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object_type', full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.object_type', index=4,
      number=1000, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState.id', index=5,
      number=1001, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIGMIGRATIONSTATE_DATATRANSFERSTATE,
    _CONFIGMIGRATIONSTATE_MIGRATIONFRAMEDEVICESSTATE,
    _CONFIGMIGRATIONSTATE_MIGRATIONBUTTONDEVICESSTATE,
    _CONFIGMIGRATIONSTATE_MIGRATIONRESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=1443,
)

_CONFIGMIGRATIONSTATE.fields_by_name['data_transfer_state'].enum_type = _CONFIGMIGRATIONSTATE_DATATRANSFERSTATE
_CONFIGMIGRATIONSTATE.fields_by_name['migration_frame_devices_state'].enum_type = _CONFIGMIGRATIONSTATE_MIGRATIONFRAMEDEVICESSTATE
_CONFIGMIGRATIONSTATE.fields_by_name['migration_button_devices_state'].enum_type = _CONFIGMIGRATIONSTATE_MIGRATIONBUTTONDEVICESSTATE
_CONFIGMIGRATIONSTATE.fields_by_name['migration_result'].enum_type = _CONFIGMIGRATIONSTATE_MIGRATIONRESULT
_CONFIGMIGRATIONSTATE.fields_by_name['object_type'].enum_type = v1_dot_hub_dot_main_dot_object__type__pb2._OBJECTTYPE
_CONFIGMIGRATIONSTATE_DATATRANSFERSTATE.containing_type = _CONFIGMIGRATIONSTATE
_CONFIGMIGRATIONSTATE_MIGRATIONFRAMEDEVICESSTATE.containing_type = _CONFIGMIGRATIONSTATE
_CONFIGMIGRATIONSTATE_MIGRATIONBUTTONDEVICESSTATE.containing_type = _CONFIGMIGRATIONSTATE
_CONFIGMIGRATIONSTATE_MIGRATIONRESULT.containing_type = _CONFIGMIGRATIONSTATE
DESCRIPTOR.message_types_by_name['ConfigMigrationState'] = _CONFIGMIGRATIONSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigMigrationState = _reflection.GeneratedProtocolMessageType('ConfigMigrationState', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGMIGRATIONSTATE,
  '__module__' : 'v1.hub.main.config_migration_state_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState)
  })
_sym_db.RegisterMessage(ConfigMigrationState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)