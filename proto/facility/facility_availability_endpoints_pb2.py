# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/facility/facility-availability-endpoints.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/facility/facility-availability-endpoints.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\"systems.ajax.a911.grpc.facility.v1\210\001\001\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1v1/facility/facility-availability-endpoints.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9e\x01\n\x1b\x46\x61\x63ilityAvailabilityRequest\x12-\n\tfrom_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07to_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12#\n\x1bregistration_number_pattern\x18\x03 \x01(\t\"V\n\x1c\x46\x61\x63ilityAvailabilityResponse\x12\x36\n\x17\x66\x61\x63ility_availabilities\x18\x01 \x03(\x0b\x32\x15.FacilityAvailability\"Q\n\x14\x46\x61\x63ilityAvailability\x12\x1b\n\x13registration_number\x18\x01 \x01(\t\x12\x1c\n\x14\x61vailability_percent\x18\x02 \x01(\x01\x32~\n\x1b\x46\x61\x63ilityAvailabilityService\x12_\n getFacilitiesAvailabilityPercent\x12\x1c.FacilityAvailabilityRequest\x1a\x1d.FacilityAvailabilityResponseB*\n\"systems.ajax.a911.grpc.facility.v1\x88\x01\x01\xba\x02\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_FACILITYAVAILABILITYREQUEST = _descriptor.Descriptor(
  name='FacilityAvailabilityRequest',
  full_name='FacilityAvailabilityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_date', full_name='FacilityAvailabilityRequest.from_date', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_date', full_name='FacilityAvailabilityRequest.to_date', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registration_number_pattern', full_name='FacilityAvailabilityRequest.registration_number_pattern', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=87,
  serialized_end=245,
)


_FACILITYAVAILABILITYRESPONSE = _descriptor.Descriptor(
  name='FacilityAvailabilityResponse',
  full_name='FacilityAvailabilityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='facility_availabilities', full_name='FacilityAvailabilityResponse.facility_availabilities', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=247,
  serialized_end=333,
)


_FACILITYAVAILABILITY = _descriptor.Descriptor(
  name='FacilityAvailability',
  full_name='FacilityAvailability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='registration_number', full_name='FacilityAvailability.registration_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='availability_percent', full_name='FacilityAvailability.availability_percent', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=335,
  serialized_end=416,
)

_FACILITYAVAILABILITYREQUEST.fields_by_name['from_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FACILITYAVAILABILITYREQUEST.fields_by_name['to_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FACILITYAVAILABILITYRESPONSE.fields_by_name['facility_availabilities'].message_type = _FACILITYAVAILABILITY
DESCRIPTOR.message_types_by_name['FacilityAvailabilityRequest'] = _FACILITYAVAILABILITYREQUEST
DESCRIPTOR.message_types_by_name['FacilityAvailabilityResponse'] = _FACILITYAVAILABILITYRESPONSE
DESCRIPTOR.message_types_by_name['FacilityAvailability'] = _FACILITYAVAILABILITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FacilityAvailabilityRequest = _reflection.GeneratedProtocolMessageType('FacilityAvailabilityRequest', (_message.Message,), {
  'DESCRIPTOR' : _FACILITYAVAILABILITYREQUEST,
  '__module__' : 'v1.facility.facility_availability_endpoints_pb2'
  # @@protoc_insertion_point(class_scope:FacilityAvailabilityRequest)
  })
_sym_db.RegisterMessage(FacilityAvailabilityRequest)

FacilityAvailabilityResponse = _reflection.GeneratedProtocolMessageType('FacilityAvailabilityResponse', (_message.Message,), {
  'DESCRIPTOR' : _FACILITYAVAILABILITYRESPONSE,
  '__module__' : 'v1.facility.facility_availability_endpoints_pb2'
  # @@protoc_insertion_point(class_scope:FacilityAvailabilityResponse)
  })
_sym_db.RegisterMessage(FacilityAvailabilityResponse)

FacilityAvailability = _reflection.GeneratedProtocolMessageType('FacilityAvailability', (_message.Message,), {
  'DESCRIPTOR' : _FACILITYAVAILABILITY,
  '__module__' : 'v1.facility.facility_availability_endpoints_pb2'
  # @@protoc_insertion_point(class_scope:FacilityAvailability)
  })
_sym_db.RegisterMessage(FacilityAvailability)


DESCRIPTOR._options = None

_FACILITYAVAILABILITYSERVICE = _descriptor.ServiceDescriptor(
  name='FacilityAvailabilityService',
  full_name='FacilityAvailabilityService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=418,
  serialized_end=544,
  methods=[
  _descriptor.MethodDescriptor(
    name='getFacilitiesAvailabilityPercent',
    full_name='FacilityAvailabilityService.getFacilitiesAvailabilityPercent',
    index=0,
    containing_service=None,
    input_type=_FACILITYAVAILABILITYREQUEST,
    output_type=_FACILITYAVAILABILITYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FACILITYAVAILABILITYSERVICE)

DESCRIPTOR.services_by_name['FacilityAvailabilityService'] = _FACILITYAVAILABILITYSERVICE

# @@protoc_insertion_point(module_scope)