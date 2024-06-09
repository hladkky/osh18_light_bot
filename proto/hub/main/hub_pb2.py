# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/hub/main/hub.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from proto.hub.main.device import device_pb2 as v1_dot_hub_dot_main_dot_device_dot_device__pb2
from proto.hub.main.device import hub_device_pb2 as v1_dot_hub_dot_main_dot_device_dot_hub__device__pb2
from proto.hub.main import room_pb2 as v1_dot_hub_dot_main_dot_room__pb2
from proto.hub.main import group_pb2 as v1_dot_hub_dot_main_dot_group__pb2
from proto.hub.main import user_pb2 as v1_dot_hub_dot_main_dot_user__pb2
from proto.hub.main import image_urls_pb2 as v1_dot_hub_dot_main_dot_image__urls__pb2
from proto.hub.main import camera_pb2 as v1_dot_hub_dot_main_dot_camera__pb2
from proto.hub.main import scenario_pb2 as v1_dot_hub_dot_main_dot_scenario__pb2
from proto.hub.main import company_binding_pb2 as v1_dot_hub_dot_main_dot_company__binding__pb2
from proto.hub.main import config_migration_state_pb2 as v1_dot_hub_dot_main_dot_config__migration__state__pb2
from proto.hub.main import access_code_pb2 as v1_dot_hub_dot_main_dot_access__code__pb2
from proto.hub.main import bus_pb2 as v1_dot_hub_dot_main_dot_bus__pb2
from proto.hub.main import device_firmware_update_pb2 as v1_dot_hub_dot_main_dot_device__firmware__update__pb2
from proto.hub.main import security_management_pb2 as v1_dot_hub_dot_main_dot_security__management__pb2
from proto.hub.main import system_firmware_update_pb2 as v1_dot_hub_dot_main_dot_system__firmware__update__pb2
from proto.hub.main import cross_zone_pb2 as v1_dot_hub_dot_main_dot_cross__zone__pb2
from proto.hub.main import sip_base_pb2 as v1_dot_hub_dot_main_dot_sip__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/hub/main/hub.proto',
  package='systems.ajax.a911.grpc.v1.hub.main',
  syntax='proto3',
  serialized_options=b'\n\036systems.ajax.a911.grpc.v1.mainP\001\272\002\007Systems',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15v1/hub/main/hub.proto\x12\"systems.ajax.a911.grpc.v1.hub.main\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fv1/hub/main/device/device.proto\x1a#v1/hub/main/device/hub_device.proto\x1a\x16v1/hub/main/room.proto\x1a\x17v1/hub/main/group.proto\x1a\x16v1/hub/main/user.proto\x1a\x1cv1/hub/main/image_urls.proto\x1a\x18v1/hub/main/camera.proto\x1a\x1av1/hub/main/scenario.proto\x1a!v1/hub/main/company_binding.proto\x1a(v1/hub/main/config_migration_state.proto\x1a\x1dv1/hub/main/access_code.proto\x1a\x15v1/hub/main/bus.proto\x1a(v1/hub/main/device_firmware_update.proto\x1a%v1/hub/main/security_management.proto\x1a(v1/hub/main/system_firmware_update.proto\x1a\x1cv1/hub/main/cross_zone.proto\x1a\x1av1/hub/main/sip_base.proto\"\xc7\x08\n\x03Hub\x12<\n\x07\x64\x65vices\x18\xe8\x07 \x03(\x0b\x32*.systems.ajax.a911.grpc.v1.hub.main.Device\x12\x38\n\x05rooms\x18\xf2\x07 \x03(\x0b\x32(.systems.ajax.a911.grpc.v1.hub.main.Room\x12:\n\x06groups\x18\xfc\x07 \x03(\x0b\x32).systems.ajax.a911.grpc.v1.hub.main.Group\x12\x38\n\x05users\x18\x86\x08 \x03(\x0b\x32(.systems.ajax.a911.grpc.v1.hub.main.User\x12<\n\x07\x63\x61meras\x18\x90\x08 \x03(\x0b\x32*.systems.ajax.a911.grpc.v1.hub.main.Camera\x12@\n\tscenarios\x18\x9a\x08 \x03(\x0b\x32,.systems.ajax.a911.grpc.v1.hub.main.Scenario\x12M\n\x10\x63ompany_bindings\x18\xae\x08 \x03(\x0b\x32\x32.systems.ajax.a911.grpc.v1.hub.main.CompanyBinding\x12Y\n\x16\x63onfig_migration_state\x18\xb8\x08 \x01(\x0b\x32\x38.systems.ajax.a911.grpc.v1.hub.main.ConfigMigrationState\x12\x14\n\x0bsettings_id\x18\xd0\x0f \x01(\t\x12\x45\n\x0c\x61\x63\x63\x65ss_codes\x18\xda\x0f \x03(\x0b\x32..systems.ajax.a911.grpc.v1.hub.main.AccessCode\x12\x37\n\x05\x62uses\x18\xe4\x0f \x03(\x0b\x32\'.systems.ajax.a911.grpc.v1.hub.main.Bus\x12Z\n\x17\x64\x65vice_firmware_updates\x18\xee\x0f \x03(\x0b\x32\x38.systems.ajax.a911.grpc.v1.hub.main.DeviceFirmwareUpdate\x12U\n\x14security_managements\x18\xf8\x0f \x03(\x0b\x32\x36.systems.ajax.a911.grpc.v1.hub.main.SecurityManagement\x12Y\n\x16system_firmware_update\x18\x82\x10 \x01(\x0b\x32\x38.systems.ajax.a911.grpc.v1.hub.main.SystemFirmwareUpdate\x12\x43\n\x0b\x63ross_zones\x18\x8c\x10 \x03(\x0b\x32-.systems.ajax.a911.grpc.v1.hub.main.CrossZone\x12?\n\tsip_bases\x18\x96\x10 \x03(\x0b\x32+.systems.ajax.a911.grpc.v1.hub.main.SipBaseB,\n\x1esystems.ajax.a911.grpc.v1.mainP\x01\xba\x02\x07Systemsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_device_dot_device__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_device_dot_hub__device__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_room__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_group__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_user__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_image__urls__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_camera__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_scenario__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_company__binding__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_config__migration__state__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_access__code__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_bus__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_device__firmware__update__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_security__management__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_system__firmware__update__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_cross__zone__pb2.DESCRIPTOR,v1_dot_hub_dot_main_dot_sip__base__pb2.DESCRIPTOR,])




_HUB = _descriptor.Descriptor(
  name='Hub',
  full_name='systems.ajax.a911.grpc.v1.hub.main.Hub',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='devices', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.devices', index=0,
      number=1000, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rooms', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.rooms', index=1,
      number=1010, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groups', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.groups', index=2,
      number=1020, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='users', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.users', index=3,
      number=1030, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cameras', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.cameras', index=4,
      number=1040, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scenarios', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.scenarios', index=5,
      number=1050, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_bindings', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.company_bindings', index=6,
      number=1070, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config_migration_state', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.config_migration_state', index=7,
      number=1080, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settings_id', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.settings_id', index=8,
      number=2000, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_codes', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.access_codes', index=9,
      number=2010, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buses', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.buses', index=10,
      number=2020, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_firmware_updates', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.device_firmware_updates', index=11,
      number=2030, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security_managements', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.security_managements', index=12,
      number=2040, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system_firmware_update', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.system_firmware_update', index=13,
      number=2050, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cross_zones', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.cross_zones', index=14,
      number=2060, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sip_bases', full_name='systems.ajax.a911.grpc.v1.hub.main.Hub.sip_bases', index=15,
      number=2070, type=11, cpp_type=10, label=3,
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
  serialized_start=633,
  serialized_end=1728,
)

_HUB.fields_by_name['devices'].message_type = v1_dot_hub_dot_main_dot_device_dot_device__pb2._DEVICE
_HUB.fields_by_name['rooms'].message_type = v1_dot_hub_dot_main_dot_room__pb2._ROOM
_HUB.fields_by_name['groups'].message_type = v1_dot_hub_dot_main_dot_group__pb2._GROUP
_HUB.fields_by_name['users'].message_type = v1_dot_hub_dot_main_dot_user__pb2._USER
_HUB.fields_by_name['cameras'].message_type = v1_dot_hub_dot_main_dot_camera__pb2._CAMERA
_HUB.fields_by_name['scenarios'].message_type = v1_dot_hub_dot_main_dot_scenario__pb2._SCENARIO
_HUB.fields_by_name['company_bindings'].message_type = v1_dot_hub_dot_main_dot_company__binding__pb2._COMPANYBINDING
_HUB.fields_by_name['config_migration_state'].message_type = v1_dot_hub_dot_main_dot_config__migration__state__pb2._CONFIGMIGRATIONSTATE
_HUB.fields_by_name['access_codes'].message_type = v1_dot_hub_dot_main_dot_access__code__pb2._ACCESSCODE
_HUB.fields_by_name['buses'].message_type = v1_dot_hub_dot_main_dot_bus__pb2._BUS
_HUB.fields_by_name['device_firmware_updates'].message_type = v1_dot_hub_dot_main_dot_device__firmware__update__pb2._DEVICEFIRMWAREUPDATE
_HUB.fields_by_name['security_managements'].message_type = v1_dot_hub_dot_main_dot_security__management__pb2._SECURITYMANAGEMENT
_HUB.fields_by_name['system_firmware_update'].message_type = v1_dot_hub_dot_main_dot_system__firmware__update__pb2._SYSTEMFIRMWAREUPDATE
_HUB.fields_by_name['cross_zones'].message_type = v1_dot_hub_dot_main_dot_cross__zone__pb2._CROSSZONE
_HUB.fields_by_name['sip_bases'].message_type = v1_dot_hub_dot_main_dot_sip__base__pb2._SIPBASE
DESCRIPTOR.message_types_by_name['Hub'] = _HUB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Hub = _reflection.GeneratedProtocolMessageType('Hub', (_message.Message,), {
  'DESCRIPTOR' : _HUB,
  '__module__' : 'v1.hub.main.hub_pb2'
  # @@protoc_insertion_point(class_scope:systems.ajax.a911.grpc.v1.hub.main.Hub)
  })
_sym_db.RegisterMessage(Hub)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)