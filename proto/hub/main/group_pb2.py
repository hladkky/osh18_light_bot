# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.hub.main import image_urls_pb2 as v1_dot_hub_dot_main_dot_image__urls__pb2
from proto.hub.main import name_pb2 as v1_dot_hub_dot_main_dot_name__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/group.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\036systems.ajax.a911.grpc.v1.mainP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17v1/hub/main/group.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x1cv1/hub/main/image_urls.proto\x1a\x16v1/hub/main/name.proto\"\x9f\x08\n\x05Group\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08image_id\x18\x03 \x01(\t\x12\x19\n\x11\x62ulk_arm_involved\x18\x04 \x01(\x08\x12\x1c\n\x14\x62ulk_disarm_involved\x18\x05 \x01(\x08\x12>\n\x05state\x18\x06 \x01(\x0e\x32/.systems.ajax.a911.grpc.v1.hub.main.Group.State\x12\x37\n\x04name\x18\xe8\x07 \x01(\x0b\x32(.systems.ajax.a911.grpc.v1.hub.main.Name\x12\x42\n\nimage_urls\x18\xf2\x07 \x01(\x0b\x32-.systems.ajax.a911.grpc.v1.hub.main.ImageUrls\x12\x1d\n\x15second_stage_required\x18\t \x01(\x08\x12_\n\x17two_stage_arming_status\x18\n \x01(\x0e\x32>.systems.ajax.a911.grpc.v1.hub.main.Group.TwoStageArmingStatus\x12M\n\rchimes_status\x18\x0b \x03(\x0e\x32\x36.systems.ajax.a911.grpc.v1.hub.main.Group.ChimesStatus\x12T\n\x11sia_arming_status\x18\x0e \x03(\x0e\x32\x39.systems.ajax.a911.grpc.v1.hub.main.Group.SiaArmingStatus\"3\n\x05State\x12\x11\n\rNO_STATE_INFO\x10\x00\x12\x0c\n\x08\x44ISARMED\x10\x01\x12\t\n\x05\x41RMED\x10\x02\"\xc6\x01\n\x14TwoStageArmingStatus\x12 \n\x1cNO_TWO_STORAGE_ARMING_STATUS\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x1e\n\x1a\x41PP_EXIT_TIMER_IN_PROGRESS\x10\x02\x12\"\n\x1eSECOND_STAGE_TIMER_IN_PROGRESS\x10\x03\x12\x15\n\x11\x41RMING_INCOMPLETE\x10\x04\x12\'\n#FINAL_DOOR_BOUNCE_TIMER_IN_PROGRESS\x10\x05\"c\n\x0c\x43himesStatus\x12\x19\n\x15NO_CHIMES_STATUS_INFO\x10\x00\x12\x12\n\x0e\x43HIMES_ENABLED\x10\x01\x12\x10\n\x0cSIRENS_READY\x10\x02\x12\x12\n\x0eTRIGGERS_READY\x10\x03\"z\n\x0fSiaArmingStatus\x12!\n\x1dSIA_ARMING_STATUS_UNSPECIFIED\x10\x00\x12\"\n\x1eSIA_ARMING_STATUS_TIME_RESTART\x10\x01\x12 \n\x1cSIA_ARMING_STATUS_EXIT_ERROR\x10\x02\x42,\n\x1esystems.ajax.a911.grpc.v1.mainP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[v1_dot_hub_dot_main_dot_image__urls__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_name__pb2.DESCRIPTOR,])



_GROUP_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Group.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_STATE_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISARMED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ARMED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=696,
  serialized_end=747,
)
_sym_db.RegisterEnumDescriptor(_GROUP_STATE)

_GROUP_TWOSTAGEARMINGSTATUS = _descriptor.EnumDescriptor(
  name='TwoStageArmingStatus',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Group.TwoStageArmingStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_TWO_STORAGE_ARMING_STATUS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APP_EXIT_TIMER_IN_PROGRESS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SECOND_STAGE_TIMER_IN_PROGRESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ARMING_INCOMPLETE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINAL_DOOR_BOUNCE_TIMER_IN_PROGRESS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=750,
  serialized_end=948,
)
_sym_db.RegisterEnumDescriptor(_GROUP_TWOSTAGEARMINGSTATUS)

_GROUP_CHIMESSTATUS = _descriptor.EnumDescriptor(
  name='ChimesStatus',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Group.ChimesStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_CHIMES_STATUS_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHIMES_ENABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIRENS_READY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRIGGERS_READY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=950,
  serialized_end=1049,
)
_sym_db.RegisterEnumDescriptor(_GROUP_CHIMESSTATUS)

_GROUP_SIAARMINGSTATUS = _descriptor.EnumDescriptor(
  name='SiaArmingStatus',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Group.SiaArmingStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIA_ARMING_STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIA_ARMING_STATUS_TIME_RESTART', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIA_ARMING_STATUS_EXIT_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1051,
  serialized_end=1173,
)
_sym_db.RegisterEnumDescriptor(_GROUP_SIAARMINGSTATUS)


_GROUP = _descriptor.Descriptor(
  name='Group',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_id', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.image_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bulk_arm_involved', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.bulk_arm_involved', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bulk_disarm_involved', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.bulk_disarm_involved', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.state', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.name', index=5,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_urls', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.image_urls', index=6,
      number=1010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='second_stage_required', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.second_stage_required', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='two_stage_arming_status', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.two_stage_arming_status', index=8,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chimes_status', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.chimes_status', index=9,
      number=11, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sia_arming_status', full_name='systems.ajax.a911.grpc.v1.hub.main.Group.sia_arming_status', index=10,
      number=14, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GROUP_STATE,
    _GROUP_TWOSTAGEARMINGSTATUS,
    _GROUP_CHIMESSTATUS,
    _GROUP_SIAARMINGSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=1173,
)

_GROUP.fields_by_name['state'].enum_type = _GROUP_STATE
_GROUP.fields_by_name['name'].message_type = v1_dot_hub_dot_main_dot_name__pb2._NAME
_GROUP.fields_by_name['image_urls'].message_type = v1_dot_hub_dot_main_dot_image__urls__pb2._IMAGEURLS
_GROUP.fields_by_name['two_stage_arming_status'].enum_type = _GROUP_TWOSTAGEARMINGSTATUS
_GROUP.fields_by_name['chimes_status'].enum_type = _GROUP_CHIMESSTATUS
_GROUP.fields_by_name['sia_arming_status'].enum_type = _GROUP_SIAARMINGSTATUS
_GROUP_STATE.containing_type = _GROUP
_GROUP_TWOSTAGEARMINGSTATUS.containing_type = _GROUP
_GROUP_CHIMESSTATUS.containing_type = _GROUP
_GROUP_SIAARMINGSTATUS.containing_type = _GROUP
DESCRIPTOR.message_types_by_name['Group'] = _GROUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Group = _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), {
  'DESCRIPTOR' : _GROUP,
  '__module__' : 'v1.hub.main.group_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.Group)
  })
_sym_db.RegisterMessage(Group)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
