# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/firmware/get_firmware_metadata_request.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.hub.main import firmware_id_pb2 as v1_dot_hub_dot_main_dot_firmware__id__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto.common.hub import firmware_id_pb2 as v2_dot_common_dot_hub_dot_firmware__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/firmware/get_firmware_metadata_request.proto',
  package='systems.ajax.a911.grpc.v1.hub.firmware',
  syntax='proto3',
  serialized_options=b'\n&systems.ajax.a911.grpc.hub.v1.firmwareP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3v1/hub/firmware/get_firmware_metadata_request.proto\x12&systems.ajax.a911.grpc.v1.hub.firmware\x1a\x1dv1/hub/main/firmware_id.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fv2/common/hub/firmware_id.proto\"\xdf\x01\n\x1aGetFirmwareMetadataRequest\x12\x45\n\x0b\x66irmware_id\x18\x01 \x01(\x0b\x32..systems.ajax.a911.grpc.v1.hub.main.FirmwareIdH\x00\x12L\n\x0e\x66irmware_id_v2\x18\x03 \x01(\x0b\x32\x32.systems.ajax.api.desktop.v2.common.hub.FirmwareIdH\x00\x12\x15\n\rlanguage_code\x18\x02 \x01(\tB\x15\n\x13\x66irmware_id_version\"\xb0\x03\n\x1bGetFirmwareMetadataResponse\x12^\n\x07success\x18\x01 \x01(\x0b\x32K.systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.SuccessH\x00\x12^\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32K.systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.FailureH\x00\x1a>\n\x07Success\x12\x15\n\rrelease_notes\x18\x01 \x03(\t\x12\x1c\n\x14\x62\x65\x66ore_proceed_notes\x18\x02 \x03(\t\x1a\x84\x01\n\x07\x46\x61ilure\x12\x0f\n\x07message\x18\x64 \x01(\t\x12\x32\n\x10illegal_argument\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12+\n\tnot_found\x18\x02 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x42\x07\n\x05\x65rrorB\n\n\x08responseB*\n&systems.ajax.a911.grpc.hub.v1.firmwareP\x01\x62\x06proto3'
  ,
  dependencies=[v1_dot_hub_dot_main_dot_firmware__id__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,v2_dot_common_dot_hub_dot_firmware__id__pb2.DESCRIPTOR,])




_GETFIRMWAREMETADATAREQUEST = _descriptor.Descriptor(
  name='GetFirmwareMetadataRequest',
  full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='firmware_id', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataRequest.firmware_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='firmware_id_v2', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataRequest.firmware_id_v2', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataRequest.language_code', index=2,
      number=2, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='firmware_id_version', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataRequest.firmware_id_version',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=189,
  serialized_end=412,
)


_GETFIRMWAREMETADATARESPONSE_SUCCESS = _descriptor.Descriptor(
  name='Success',
  full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.Success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='release_notes', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.Success.release_notes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='before_proceed_notes', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.Success.before_proceed_notes', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=638,
  serialized_end=700,
)

_GETFIRMWAREMETADATARESPONSE_FAILURE = _descriptor.Descriptor(
  name='Failure',
  full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.Failure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.Failure.message', index=0,
      number=100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='illegal_argument', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.Failure.illegal_argument', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='not_found', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.Failure.not_found', index=2,
      number=2, type=11, cpp_type=10, label=1,
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
      name='error', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.Failure.error',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=703,
  serialized_end=835,
)

_GETFIRMWAREMETADATARESPONSE = _descriptor.Descriptor(
  name='GetFirmwareMetadataResponse',
  full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failure', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.failure', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETFIRMWAREMETADATARESPONSE_SUCCESS, _GETFIRMWAREMETADATARESPONSE_FAILURE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='response', full_name='systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.response',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=415,
  serialized_end=847,
)

_GETFIRMWAREMETADATAREQUEST.fields_by_name['firmware_id'].message_type = v1_dot_hub_dot_main_dot_firmware__id__pb2._FIRMWAREID
_GETFIRMWAREMETADATAREQUEST.fields_by_name['firmware_id_v2'].message_type = v2_dot_common_dot_hub_dot_firmware__id__pb2._FIRMWAREID
_GETFIRMWAREMETADATAREQUEST.oneofs_by_name['firmware_id_version'].fields.append(
  _GETFIRMWAREMETADATAREQUEST.fields_by_name['firmware_id'])
_GETFIRMWAREMETADATAREQUEST.fields_by_name['firmware_id'].containing_oneof = _GETFIRMWAREMETADATAREQUEST.oneofs_by_name['firmware_id_version']
_GETFIRMWAREMETADATAREQUEST.oneofs_by_name['firmware_id_version'].fields.append(
  _GETFIRMWAREMETADATAREQUEST.fields_by_name['firmware_id_v2'])
_GETFIRMWAREMETADATAREQUEST.fields_by_name['firmware_id_v2'].containing_oneof = _GETFIRMWAREMETADATAREQUEST.oneofs_by_name['firmware_id_version']
_GETFIRMWAREMETADATARESPONSE_SUCCESS.containing_type = _GETFIRMWAREMETADATARESPONSE
_GETFIRMWAREMETADATARESPONSE_FAILURE.fields_by_name['illegal_argument'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_GETFIRMWAREMETADATARESPONSE_FAILURE.fields_by_name['not_found'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_GETFIRMWAREMETADATARESPONSE_FAILURE.containing_type = _GETFIRMWAREMETADATARESPONSE
_GETFIRMWAREMETADATARESPONSE_FAILURE.oneofs_by_name['error'].fields.append(
  _GETFIRMWAREMETADATARESPONSE_FAILURE.fields_by_name['illegal_argument'])
_GETFIRMWAREMETADATARESPONSE_FAILURE.fields_by_name['illegal_argument'].containing_oneof = _GETFIRMWAREMETADATARESPONSE_FAILURE.oneofs_by_name['error']
_GETFIRMWAREMETADATARESPONSE_FAILURE.oneofs_by_name['error'].fields.append(
  _GETFIRMWAREMETADATARESPONSE_FAILURE.fields_by_name['not_found'])
_GETFIRMWAREMETADATARESPONSE_FAILURE.fields_by_name['not_found'].containing_oneof = _GETFIRMWAREMETADATARESPONSE_FAILURE.oneofs_by_name['error']
_GETFIRMWAREMETADATARESPONSE.fields_by_name['success'].message_type = _GETFIRMWAREMETADATARESPONSE_SUCCESS
_GETFIRMWAREMETADATARESPONSE.fields_by_name['failure'].message_type = _GETFIRMWAREMETADATARESPONSE_FAILURE
_GETFIRMWAREMETADATARESPONSE.oneofs_by_name['response'].fields.append(
  _GETFIRMWAREMETADATARESPONSE.fields_by_name['success'])
_GETFIRMWAREMETADATARESPONSE.fields_by_name['success'].containing_oneof = _GETFIRMWAREMETADATARESPONSE.oneofs_by_name['response']
_GETFIRMWAREMETADATARESPONSE.oneofs_by_name['response'].fields.append(
  _GETFIRMWAREMETADATARESPONSE.fields_by_name['failure'])
_GETFIRMWAREMETADATARESPONSE.fields_by_name['failure'].containing_oneof = _GETFIRMWAREMETADATARESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['GetFirmwareMetadataRequest'] = _GETFIRMWAREMETADATAREQUEST
DESCRIPTOR.message_types_by_name['GetFirmwareMetadataResponse'] = _GETFIRMWAREMETADATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFirmwareMetadataRequest = _reflection.GeneratedProtocolMessageType('GetFirmwareMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFIRMWAREMETADATAREQUEST,
  '__module__' : 'v1.hub.firmware.get_firmware_metadata_request_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataRequest)
  })
_sym_db.RegisterMessage(GetFirmwareMetadataRequest)

GetFirmwareMetadataResponse = _reflection.GeneratedProtocolMessageType('GetFirmwareMetadataResponse', (_message.Message,), {

  'Success' : _reflection.GeneratedProtocolMessageType('Success', (_message.Message,), {
    'DESCRIPTOR' : _GETFIRMWAREMETADATARESPONSE_SUCCESS,
    '__module__' : 'v1.hub.firmware.get_firmware_metadata_request_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.Success)
    })
  ,

  'Failure' : _reflection.GeneratedProtocolMessageType('Failure', (_message.Message,), {
    'DESCRIPTOR' : _GETFIRMWAREMETADATARESPONSE_FAILURE,
    '__module__' : 'v1.hub.firmware.get_firmware_metadata_request_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse.Failure)
    })
  ,
  'DESCRIPTOR' : _GETFIRMWAREMETADATARESPONSE,
  '__module__' : 'v1.hub.firmware.get_firmware_metadata_request_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.firmware.GetFirmwareMetadataResponse)
  })
_sym_db.RegisterMessage(GetFirmwareMetadataResponse)
_sym_db.RegisterMessage(GetFirmwareMetadataResponse.Success)
_sym_db.RegisterMessage(GetFirmwareMetadataResponse.Failure)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)