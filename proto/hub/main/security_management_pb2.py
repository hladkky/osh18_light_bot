# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/security_management.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/security_management.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\036systems.ajax.a911.grpc.v1.mainP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%v1/hub/main/security_management.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\"\x8b\x0c\n\x12SecurityManagement\x12\n\n\x02id\x18\x01 \x01(\x05\x12P\n\x07subtype\x18\xc3\x01 \x01(\x0e\x32>.systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Subtype\x12P\n\x06keyarm\x18\xe8\x07 \x01(\x0b\x32=.systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.KeyarmH\x00\x1a\x90\x05\n\x06Keyarm\x12V\n\x0bkeyarm_type\x18\x03 \x01(\x0e\x32\x41.systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.KeyarmType\x12\\\n\x0ekeyarm_control\x18\x04 \x01(\x0e\x32\x44.systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.KeyarmControl\x12o\n\x15keyarm_groups_control\x18\x05 \x03(\x0b\x32P.systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.KeyarmGroupControl\x12Q\n\x08\x62locking\x18\x06 \x01(\x0e\x32?.systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Blocking\x12X\n\x0ckeyarm_state\x18\x07 \x03(\x0e\x32\x42.systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.KeyarmState\x12l\n\x17\x65vent_lock_violation_en\x18\x08 \x01(\x0e\x32K.systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.EventLockViolationEn\x1a\x44\n\x12KeyarmGroupControl\x12\x11\n\x08group_id\x18\xe8\x07 \x01(\t\x12\x1b\n\x12permission_enabled\x18\xe9\x07 \x01(\x08\"6\n\x07Subtype\x12\x17\n\x13SUBTYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eSUBTYPE_KEYARM\x10\x01\"\x85\x01\n\nKeyarmType\x12\x1b\n\x17KEYARM_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1fKEYARM_TYPE_ARM_DISARM_TOGGLING\x10\x01\x12\x18\n\x14KEYARM_TYPE_ARM_ONLY\x10\x02\x12\x1b\n\x17KEYARM_TYPE_DISARM_ONLY\x10\x03\"\x81\x01\n\rKeyarmControl\x12\x1e\n\x1aKEYARM_CONTROL_UNSPECIFIED\x10\x00\x12\x16\n\x12KEYARM_CONTROL_HUB\x10\x01\x12\x19\n\x15KEYARM_CONTROL_GROUPS\x10\x02\x12\x1d\n\x19KEYARM_CONTROL_NIGHT_MODE\x10\x03\"Q\n\x08\x42locking\x12\x18\n\x14\x42LOCKING_UNSPECIFIED\x10\x00\x12\x15\n\x11\x42LOCKING_DISABLED\x10\x01\x12\x14\n\x10\x42LOCKING_ENABLED\x10\x02\"\x8a\x01\n\x14\x45ventLockViolationEn\x12\'\n#EVENT_LOCK_VIOLATION_EN_UNSPECIFIED\x10\x00\x12$\n EVENT_LOCK_VIOLATION_EN_DISABLED\x10\x01\x12#\n\x1f\x45VENT_LOCK_VIOLATION_EN_ENABLED\x10\x02\"\x81\x01\n\x0bKeyarmState\x12\x1c\n\x18KEYARM_STATE_UNSPECIFIED\x10\x00\x12\x18\n\x14KEYARM_STATE_BLOCKED\x10\x01\x12\x30\n,KEYARM_STATE_BLOCKING_AFTER_TAMPER_SUPPORTED\x10\x02\"\x08\x08\x03\x10\xff\xff\xff\xff\x07\x42\n\n\x08subtypesB,\n\x1esystems.ajax.a911.grpc.v1.mainP\x01\xba\x02\x07Systemsb\x06proto3'
)



_SECURITYMANAGEMENT_SUBTYPE = _descriptor.EnumDescriptor(
  name='Subtype',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Subtype',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUBTYPE_KEYARM', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=935,
  serialized_end=989,
)
_sym_db.RegisterEnumDescriptor(_SECURITYMANAGEMENT_SUBTYPE)

_SECURITYMANAGEMENT_KEYARMTYPE = _descriptor.EnumDescriptor(
  name='KeyarmType',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.KeyarmType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KEYARM_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYARM_TYPE_ARM_DISARM_TOGGLING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYARM_TYPE_ARM_ONLY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYARM_TYPE_DISARM_ONLY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=992,
  serialized_end=1125,
)
_sym_db.RegisterEnumDescriptor(_SECURITYMANAGEMENT_KEYARMTYPE)

_SECURITYMANAGEMENT_KEYARMCONTROL = _descriptor.EnumDescriptor(
  name='KeyarmControl',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.KeyarmControl',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KEYARM_CONTROL_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYARM_CONTROL_HUB', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYARM_CONTROL_GROUPS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYARM_CONTROL_NIGHT_MODE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1128,
  serialized_end=1257,
)
_sym_db.RegisterEnumDescriptor(_SECURITYMANAGEMENT_KEYARMCONTROL)

_SECURITYMANAGEMENT_BLOCKING = _descriptor.EnumDescriptor(
  name='Blocking',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Blocking',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BLOCKING_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLOCKING_DISABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLOCKING_ENABLED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1259,
  serialized_end=1340,
)
_sym_db.RegisterEnumDescriptor(_SECURITYMANAGEMENT_BLOCKING)

_SECURITYMANAGEMENT_EVENTLOCKVIOLATIONEN = _descriptor.EnumDescriptor(
  name='EventLockViolationEn',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.EventLockViolationEn',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EVENT_LOCK_VIOLATION_EN_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EVENT_LOCK_VIOLATION_EN_DISABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EVENT_LOCK_VIOLATION_EN_ENABLED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1343,
  serialized_end=1481,
)
_sym_db.RegisterEnumDescriptor(_SECURITYMANAGEMENT_EVENTLOCKVIOLATIONEN)

_SECURITYMANAGEMENT_KEYARMSTATE = _descriptor.EnumDescriptor(
  name='KeyarmState',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.KeyarmState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KEYARM_STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYARM_STATE_BLOCKED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYARM_STATE_BLOCKING_AFTER_TAMPER_SUPPORTED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1484,
  serialized_end=1613,
)
_sym_db.RegisterEnumDescriptor(_SECURITYMANAGEMENT_KEYARMSTATE)


_SECURITYMANAGEMENT_KEYARM_KEYARMGROUPCONTROL = _descriptor.Descriptor(
  name='KeyarmGroupControl',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.KeyarmGroupControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.KeyarmGroupControl.group_id', index=0,
      number=1000, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permission_enabled', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.KeyarmGroupControl.permission_enabled', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=865,
  serialized_end=933,
)

_SECURITYMANAGEMENT_KEYARM = _descriptor.Descriptor(
  name='Keyarm',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyarm_type', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.keyarm_type', index=0,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyarm_control', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.keyarm_control', index=1,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyarm_groups_control', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.keyarm_groups_control', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blocking', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.blocking', index=3,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyarm_state', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.keyarm_state', index=4,
      number=7, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_lock_violation_en', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.event_lock_violation_en', index=5,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SECURITYMANAGEMENT_KEYARM_KEYARMGROUPCONTROL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=933,
)

_SECURITYMANAGEMENT = _descriptor.Descriptor(
  name='SecurityManagement',
  full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.subtype', index=1,
      number=195, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyarm', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.keyarm', index=2,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SECURITYMANAGEMENT_KEYARM, ],
  enum_types=[
    _SECURITYMANAGEMENT_SUBTYPE,
    _SECURITYMANAGEMENT_KEYARMTYPE,
    _SECURITYMANAGEMENT_KEYARMCONTROL,
    _SECURITYMANAGEMENT_BLOCKING,
    _SECURITYMANAGEMENT_EVENTLOCKVIOLATIONEN,
    _SECURITYMANAGEMENT_KEYARMSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='subtypes', full_name='systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.subtypes',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=78,
  serialized_end=1625,
)

_SECURITYMANAGEMENT_KEYARM_KEYARMGROUPCONTROL.containing_type = _SECURITYMANAGEMENT_KEYARM
_SECURITYMANAGEMENT_KEYARM.fields_by_name['keyarm_type'].enum_type = _SECURITYMANAGEMENT_KEYARMTYPE
_SECURITYMANAGEMENT_KEYARM.fields_by_name['keyarm_control'].enum_type = _SECURITYMANAGEMENT_KEYARMCONTROL
_SECURITYMANAGEMENT_KEYARM.fields_by_name['keyarm_groups_control'].message_type = _SECURITYMANAGEMENT_KEYARM_KEYARMGROUPCONTROL
_SECURITYMANAGEMENT_KEYARM.fields_by_name['blocking'].enum_type = _SECURITYMANAGEMENT_BLOCKING
_SECURITYMANAGEMENT_KEYARM.fields_by_name['keyarm_state'].enum_type = _SECURITYMANAGEMENT_KEYARMSTATE
_SECURITYMANAGEMENT_KEYARM.fields_by_name['event_lock_violation_en'].enum_type = _SECURITYMANAGEMENT_EVENTLOCKVIOLATIONEN
_SECURITYMANAGEMENT_KEYARM.containing_type = _SECURITYMANAGEMENT
_SECURITYMANAGEMENT.fields_by_name['subtype'].enum_type = _SECURITYMANAGEMENT_SUBTYPE
_SECURITYMANAGEMENT.fields_by_name['keyarm'].message_type = _SECURITYMANAGEMENT_KEYARM
_SECURITYMANAGEMENT_SUBTYPE.containing_type = _SECURITYMANAGEMENT
_SECURITYMANAGEMENT_KEYARMTYPE.containing_type = _SECURITYMANAGEMENT
_SECURITYMANAGEMENT_KEYARMCONTROL.containing_type = _SECURITYMANAGEMENT
_SECURITYMANAGEMENT_BLOCKING.containing_type = _SECURITYMANAGEMENT
_SECURITYMANAGEMENT_EVENTLOCKVIOLATIONEN.containing_type = _SECURITYMANAGEMENT
_SECURITYMANAGEMENT_KEYARMSTATE.containing_type = _SECURITYMANAGEMENT
_SECURITYMANAGEMENT.oneofs_by_name['subtypes'].fields.append(
  _SECURITYMANAGEMENT.fields_by_name['keyarm'])
_SECURITYMANAGEMENT.fields_by_name['keyarm'].containing_oneof = _SECURITYMANAGEMENT.oneofs_by_name['subtypes']
DESCRIPTOR.message_types_by_name['SecurityManagement'] = _SECURITYMANAGEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SecurityManagement = _reflection.GeneratedProtocolMessageType('SecurityManagement', (_message.Message,), {

  'Keyarm' : _reflection.GeneratedProtocolMessageType('Keyarm', (_message.Message,), {

    'KeyarmGroupControl' : _reflection.GeneratedProtocolMessageType('KeyarmGroupControl', (_message.Message,), {
      'DESCRIPTOR' : _SECURITYMANAGEMENT_KEYARM_KEYARMGROUPCONTROL,
      '__module__' : 'v1.hub.main.security_management_pb2'
      # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm.KeyarmGroupControl)
      })
    ,
    'DESCRIPTOR' : _SECURITYMANAGEMENT_KEYARM,
    '__module__' : 'v1.hub.main.security_management_pb2'
    # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.SecurityManagement.Keyarm)
    })
  ,
  'DESCRIPTOR' : _SECURITYMANAGEMENT,
  '__module__' : 'v1.hub.main.security_management_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.SecurityManagement)
  })
_sym_db.RegisterMessage(SecurityManagement)
_sym_db.RegisterMessage(SecurityManagement.Keyarm)
_sym_db.RegisterMessage(SecurityManagement.Keyarm.KeyarmGroupControl)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
