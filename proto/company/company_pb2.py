# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/company/company.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.systems.ajax.logging.proto import log_marker_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2
from proto.systems.ajax.logging.proto import formatting_options_pb2 as systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/company/company.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n!systems.ajax.a911.grpc.company.v1P\001\272\002\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18v1/company/company.proto\x1a+systems/ajax/logging/proto/log_marker.proto\x1a\x33systems/ajax/logging/proto/formatting_options.proto\"\xcc\x13\n\x07\x43ompany\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x04\x12\x11\n\tfull_name\x18\x03 \x01(\t\x12\x12\n\nshort_name\x18\x04 \x01(\t\x12*\n\x0c\x63ompany_logo\x18\x05 \x01(\x0b\x32\x14.Company.CompanyLogo\x12\x1b\n\x13registration_number\x18\x06 \x01(\t\x12\x1c\n\x0fhead_of_company\x18\x07 \x01(\tB\x03\xf8\x44\x01\x12\x34\n\x11provided_services\x18\x08 \x01(\x0b\x32\x19.Company.ProvidedServices\x12+\n\rphone_numbers\x18\x14 \x03(\x0b\x32\x14.Company.PhoneNumber\x12.\n\x0f\x65mail_addresses\x18\x15 \x03(\x0b\x32\x15.Company.EmailAddress\x12\'\n\rlegal_address\x18\x16 \x01(\x0b\x32\x10.Company.Address\x12(\n\x0epostal_address\x18\x17 \x01(\x0b\x32\x10.Company.Address\x12\x16\n\x0ereview_comment\x18\x18 \x01(\t\x12*\n\x0c\x63ompany_type\x18\x19 \x01(\x0e\x32\x14.Company.CompanyType\x12\x32\n\x10\x65mployees_number\x18\x1a \x01(\x0e\x32\x18.Company.EmployeesNumber\x12\x14\n\x0c\x63ountry_code\x18\x1b \x01(\t\x12\x11\n\tlocations\x18\x1c \x03(\t\x12/\n\x10technical_emails\x18\x1d \x03(\x0b\x32\x15.Company.EmailAddress\x12\x38\n\x19\x63ustomer_inquiries_emails\x18\x1e \x03(\x0b\x32\x15.Company.EmailAddress\x12\x14\n\x0cweb_site_url\x18\x1f \x01(\t\x12\x14\n\x0csynchronized\x18  \x01(\x08\x12K\n\x1dmarketplace_visibility_status\x18! \x01(\x0e\x32$.Company.MarketplaceVisibilityStatus\x12\x1f\n\x12\x63luster_company_id\x18\" \x01(\tB\x03\xf0\x44\x03\x12o\n0privacy_override_management_authorization_status\x18# \x01(\x0e\x32\x35.Company.PrivacyOverrideManagementAuthorizationStatus\x1aW\n\x0bPhoneNumber\x12\x13\n\x06number\x18\x01 \x01(\tB\x03\xf8\x44\x01\x12\x19\n\x0c\x63ountry_code\x18\x02 \x01(\tB\x03\xf8\x44\x01\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x03\xf8\x44\x01\x1a\x35\n\x0c\x45mailAddress\x12\x12\n\x05\x65mail\x18\x01 \x01(\tB\x03\xf8\x44\x01\x12\x11\n\tconfirmed\x18\x02 \x01(\x08\x1aw\n\x07\x41\x64\x64ress\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\x10\n\x08zip_code\x18\x04 \x01(\t\x12\x15\n\raddress_line1\x18\x05 \x01(\t\x12\x15\n\raddress_line2\x18\x06 \x01(\t\x1aN\n\x10ProvidedServices\x12\x14\n\x0cinstallation\x18\x01 \x01(\x08\x12\x12\n\nmonitoring\x18\x02 \x01(\x08\x12\x10\n\x08reaction\x18\x03 \x01(\x08\x1au\n\x0b\x43ompanyLogo\x12\x10\n\x08image_id\x18\x01 \x01(\t\x12*\n\x06images\x18\x02 \x03(\x0b\x32\x1a.Company.CompanyLogo.Image\x1a(\n\x05Image\x12\x12\n\nresolution\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"\xa7\x02\n\x0b\x43ompanyType\x12\x18\n\x14NO_COMPANY_TYPE_INFO\x10\x00\x12%\n!INSTALLATION_COMPANY_OR_INSTALLER\x10\x01\x12\x16\n\x12MONITORING_COMPANY\x10\x02\x12\x14\n\x10SECURITY_COMPANY\x10\x03\x12\x0f\n\x0b\x44ISTRIBUTOR\x10\x04\x12\x1f\n\x1bRESELLER_OR_SUB_DISTRIBUTOR\x10\x05\x12\x1a\n\x16\x46IRE_DETECTION_COMPANY\x10\x06\x12\x14\n\x10\x43ORPORATE_CLIENT\x10\x07\x12,\n(SYSTEM_INTEGRATOR_OR_SECURITY_CONSULTANT\x10\x08\x12\x0c\n\x08\x45ND_USER\x10\t\x12\t\n\x05OTHER\x10\n\"\xd1\x02\n\x0f\x45mployeesNumber\x12\x1c\n\x18NO_EMPLOYEES_NUMBER_INFO\x10\x00\x12\x1c\n\x18\x45MPLOYEES_NUMBER_UNKNOWN\x10\x01\x12\x16\n\x12\x45MPLOYEES_NUMBER_1\x10\x02\x12\x19\n\x15\x45MPLOYEES_NUMBER_2_10\x10\x03\x12\x1a\n\x16\x45MPLOYEES_NUMBER_11_30\x10\x04\x12\x1a\n\x16\x45MPLOYEES_NUMBER_31_50\x10\x05\x12\x1b\n\x17\x45MPLOYEES_NUMBER_51_100\x10\x06\x12\x1c\n\x18\x45MPLOYEES_NUMBER_101_200\x10\x07\x12\x1c\n\x18\x45MPLOYEES_NUMBER_201_300\x10\x08\x12\x1c\n\x18\x45MPLOYEES_NUMBER_301_500\x10\t\x12 \n\x1c\x45MPLOYEES_NUMBER_500_OR_MORE\x10\n\"w\n\x1bMarketplaceVisibilityStatus\x12\x1a\n\x16NO_VISIBLE_STATUS_INFO\x10\x00\x12\x1b\n\x17VISIBLE_IN_MARKET_PLACE\x10\x01\x12\x1f\n\x1bNOT_VISIBLE_IN_MARKET_PLACE\x10\x02\"\xf4\x01\n,PrivacyOverrideManagementAuthorizationStatus\x12@\n<PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_UNSPECIFIED\x10\x00\x12?\n;PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_AUTHORIZED\x10\x01\x12\x41\n=PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_UNAUTHORIZED\x10\x02\"[\n\x0bServiceType\x12\x18\n\x14SERVICE_TYPE_NO_INFO\x10\x00\x12\x17\n\x13SERVICE_TYPE_DEALER\x10\x01\x12\x19\n\x15SERVICE_TYPE_RESELLER\x10\x02\x42(\n!systems.ajax.a911.grpc.company.v1P\x01\xba\x02\x00\x62\x06proto3'
  ,
  dependencies=[systems_dot_ajax_dot_logging_dot_proto_dot_log__marker__pb2.DESCRIPTOR,systems_dot_ajax_dot_logging_dot_proto_dot_formatting__options__pb2.DESCRIPTOR,])



_COMPANY_COMPANYTYPE = _descriptor.EnumDescriptor(
  name='CompanyType',
  full_name='Company.CompanyType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_COMPANY_TYPE_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSTALLATION_COMPANY_OR_INSTALLER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MONITORING_COMPANY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SECURITY_COMPANY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISTRIBUTOR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESELLER_OR_SUB_DISTRIBUTOR', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIRE_DETECTION_COMPANY', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CORPORATE_CLIENT', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM_INTEGRATOR_OR_SECURITY_CONSULTANT', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='END_USER', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1539,
  serialized_end=1834,
)
_sym_db.RegisterEnumDescriptor(_COMPANY_COMPANYTYPE)

_COMPANY_EMPLOYEESNUMBER = _descriptor.EnumDescriptor(
  name='EmployeesNumber',
  full_name='Company.EmployeesNumber',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_EMPLOYEES_NUMBER_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPLOYEES_NUMBER_UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPLOYEES_NUMBER_1', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPLOYEES_NUMBER_2_10', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPLOYEES_NUMBER_11_30', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPLOYEES_NUMBER_31_50', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPLOYEES_NUMBER_51_100', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPLOYEES_NUMBER_101_200', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPLOYEES_NUMBER_201_300', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPLOYEES_NUMBER_301_500', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPLOYEES_NUMBER_500_OR_MORE', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1837,
  serialized_end=2174,
)
_sym_db.RegisterEnumDescriptor(_COMPANY_EMPLOYEESNUMBER)

_COMPANY_MARKETPLACEVISIBILITYSTATUS = _descriptor.EnumDescriptor(
  name='MarketplaceVisibilityStatus',
  full_name='Company.MarketplaceVisibilityStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_VISIBLE_STATUS_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VISIBLE_IN_MARKET_PLACE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_VISIBLE_IN_MARKET_PLACE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2176,
  serialized_end=2295,
)
_sym_db.RegisterEnumDescriptor(_COMPANY_MARKETPLACEVISIBILITYSTATUS)

_COMPANY_PRIVACYOVERRIDEMANAGEMENTAUTHORIZATIONSTATUS = _descriptor.EnumDescriptor(
  name='PrivacyOverrideManagementAuthorizationStatus',
  full_name='Company.PrivacyOverrideManagementAuthorizationStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_AUTHORIZED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_UNAUTHORIZED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2298,
  serialized_end=2542,
)
_sym_db.RegisterEnumDescriptor(_COMPANY_PRIVACYOVERRIDEMANAGEMENTAUTHORIZATIONSTATUS)

_COMPANY_SERVICETYPE = _descriptor.EnumDescriptor(
  name='ServiceType',
  full_name='Company.ServiceType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SERVICE_TYPE_NO_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_TYPE_DEALER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_TYPE_RESELLER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2544,
  serialized_end=2635,
)
_sym_db.RegisterEnumDescriptor(_COMPANY_SERVICETYPE)


_COMPANY_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='Company.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='Company.PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='Company.PhoneNumber.country_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='Company.PhoneNumber.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1074,
  serialized_end=1161,
)

_COMPANY_EMAILADDRESS = _descriptor.Descriptor(
  name='EmailAddress',
  full_name='Company.EmailAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='Company.EmailAddress.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confirmed', full_name='Company.EmailAddress.confirmed', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=1163,
  serialized_end=1216,
)

_COMPANY_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='Company.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='country', full_name='Company.Address.country', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='Company.Address.state', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city', full_name='Company.Address.city', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zip_code', full_name='Company.Address.zip_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address_line1', full_name='Company.Address.address_line1', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address_line2', full_name='Company.Address.address_line2', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=1218,
  serialized_end=1337,
)

_COMPANY_PROVIDEDSERVICES = _descriptor.Descriptor(
  name='ProvidedServices',
  full_name='Company.ProvidedServices',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='installation', full_name='Company.ProvidedServices.installation', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monitoring', full_name='Company.ProvidedServices.monitoring', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reaction', full_name='Company.ProvidedServices.reaction', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=1339,
  serialized_end=1417,
)

_COMPANY_COMPANYLOGO_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Company.CompanyLogo.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resolution', full_name='Company.CompanyLogo.Image.resolution', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='Company.CompanyLogo.Image.url', index=1,
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
  ],
  serialized_start=1496,
  serialized_end=1536,
)

_COMPANY_COMPANYLOGO = _descriptor.Descriptor(
  name='CompanyLogo',
  full_name='Company.CompanyLogo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_id', full_name='Company.CompanyLogo.image_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='images', full_name='Company.CompanyLogo.images', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COMPANY_COMPANYLOGO_IMAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1419,
  serialized_end=1536,
)

_COMPANY = _descriptor.Descriptor(
  name='Company',
  full_name='Company',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Company.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='Company.version', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='Company.full_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='short_name', full_name='Company.short_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_logo', full_name='Company.company_logo', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registration_number', full_name='Company.registration_number', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='head_of_company', full_name='Company.head_of_company', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\370D\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provided_services', full_name='Company.provided_services', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_numbers', full_name='Company.phone_numbers', index=8,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email_addresses', full_name='Company.email_addresses', index=9,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='legal_address', full_name='Company.legal_address', index=10,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postal_address', full_name='Company.postal_address', index=11,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='review_comment', full_name='Company.review_comment', index=12,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_type', full_name='Company.company_type', index=13,
      number=25, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='employees_number', full_name='Company.employees_number', index=14,
      number=26, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='Company.country_code', index=15,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locations', full_name='Company.locations', index=16,
      number=28, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='technical_emails', full_name='Company.technical_emails', index=17,
      number=29, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_inquiries_emails', full_name='Company.customer_inquiries_emails', index=18,
      number=30, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='web_site_url', full_name='Company.web_site_url', index=19,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='synchronized', full_name='Company.synchronized', index=20,
      number=32, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='marketplace_visibility_status', full_name='Company.marketplace_visibility_status', index=21,
      number=33, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster_company_id', full_name='Company.cluster_company_id', index=22,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360D\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='privacy_override_management_authorization_status', full_name='Company.privacy_override_management_authorization_status', index=23,
      number=35, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COMPANY_PHONENUMBER, _COMPANY_EMAILADDRESS, _COMPANY_ADDRESS, _COMPANY_PROVIDEDSERVICES, _COMPANY_COMPANYLOGO, ],
  enum_types=[
    _COMPANY_COMPANYTYPE,
    _COMPANY_EMPLOYEESNUMBER,
    _COMPANY_MARKETPLACEVISIBILITYSTATUS,
    _COMPANY_PRIVACYOVERRIDEMANAGEMENTAUTHORIZATIONSTATUS,
    _COMPANY_SERVICETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=2635,
)

_COMPANY_PHONENUMBER.containing_type = _COMPANY
_COMPANY_EMAILADDRESS.containing_type = _COMPANY
_COMPANY_ADDRESS.containing_type = _COMPANY
_COMPANY_PROVIDEDSERVICES.containing_type = _COMPANY
_COMPANY_COMPANYLOGO_IMAGE.containing_type = _COMPANY_COMPANYLOGO
_COMPANY_COMPANYLOGO.fields_by_name['images'].message_type = _COMPANY_COMPANYLOGO_IMAGE
_COMPANY_COMPANYLOGO.containing_type = _COMPANY
_COMPANY.fields_by_name['company_logo'].message_type = _COMPANY_COMPANYLOGO
_COMPANY.fields_by_name['provided_services'].message_type = _COMPANY_PROVIDEDSERVICES
_COMPANY.fields_by_name['phone_numbers'].message_type = _COMPANY_PHONENUMBER
_COMPANY.fields_by_name['email_addresses'].message_type = _COMPANY_EMAILADDRESS
_COMPANY.fields_by_name['legal_address'].message_type = _COMPANY_ADDRESS
_COMPANY.fields_by_name['postal_address'].message_type = _COMPANY_ADDRESS
_COMPANY.fields_by_name['company_type'].enum_type = _COMPANY_COMPANYTYPE
_COMPANY.fields_by_name['employees_number'].enum_type = _COMPANY_EMPLOYEESNUMBER
_COMPANY.fields_by_name['technical_emails'].message_type = _COMPANY_EMAILADDRESS
_COMPANY.fields_by_name['customer_inquiries_emails'].message_type = _COMPANY_EMAILADDRESS
_COMPANY.fields_by_name['marketplace_visibility_status'].enum_type = _COMPANY_MARKETPLACEVISIBILITYSTATUS
_COMPANY.fields_by_name['privacy_override_management_authorization_status'].enum_type = _COMPANY_PRIVACYOVERRIDEMANAGEMENTAUTHORIZATIONSTATUS
_COMPANY_COMPANYTYPE.containing_type = _COMPANY
_COMPANY_EMPLOYEESNUMBER.containing_type = _COMPANY
_COMPANY_MARKETPLACEVISIBILITYSTATUS.containing_type = _COMPANY
_COMPANY_PRIVACYOVERRIDEMANAGEMENTAUTHORIZATIONSTATUS.containing_type = _COMPANY
_COMPANY_SERVICETYPE.containing_type = _COMPANY
DESCRIPTOR.message_types_by_name['Company'] = _COMPANY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Company = _reflection.GeneratedProtocolMessageType('Company', (_message.Message,), {

  'PhoneNumber' : _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), {
    'DESCRIPTOR' : _COMPANY_PHONENUMBER,
    '__module__' : 'v1.company.company_pb2'
    # @@protoc_insertion_point(class_scope:Company.PhoneNumber)
    })
  ,

  'EmailAddress' : _reflection.GeneratedProtocolMessageType('EmailAddress', (_message.Message,), {
    'DESCRIPTOR' : _COMPANY_EMAILADDRESS,
    '__module__' : 'v1.company.company_pb2'
    # @@protoc_insertion_point(class_scope:Company.EmailAddress)
    })
  ,

  'Address' : _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
    'DESCRIPTOR' : _COMPANY_ADDRESS,
    '__module__' : 'v1.company.company_pb2'
    # @@protoc_insertion_point(class_scope:Company.Address)
    })
  ,

  'ProvidedServices' : _reflection.GeneratedProtocolMessageType('ProvidedServices', (_message.Message,), {
    'DESCRIPTOR' : _COMPANY_PROVIDEDSERVICES,
    '__module__' : 'v1.company.company_pb2'
    # @@protoc_insertion_point(class_scope:Company.ProvidedServices)
    })
  ,

  'CompanyLogo' : _reflection.GeneratedProtocolMessageType('CompanyLogo', (_message.Message,), {

    'Image' : _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
      'DESCRIPTOR' : _COMPANY_COMPANYLOGO_IMAGE,
      '__module__' : 'v1.company.company_pb2'
      # @@protoc_insertion_point(class_scope:Company.CompanyLogo.Image)
      })
    ,
    'DESCRIPTOR' : _COMPANY_COMPANYLOGO,
    '__module__' : 'v1.company.company_pb2'
    # @@protoc_insertion_point(class_scope:Company.CompanyLogo)
    })
  ,
  'DESCRIPTOR' : _COMPANY,
  '__module__' : 'v1.company.company_pb2'
  # @@protoc_insertion_point(class_scope:Company)
  })
_sym_db.RegisterMessage(Company)
_sym_db.RegisterMessage(Company.PhoneNumber)
_sym_db.RegisterMessage(Company.EmailAddress)
_sym_db.RegisterMessage(Company.Address)
_sym_db.RegisterMessage(Company.ProvidedServices)
_sym_db.RegisterMessage(Company.CompanyLogo)
_sym_db.RegisterMessage(Company.CompanyLogo.Image)


DESCRIPTOR._options = None
_COMPANY_PHONENUMBER.fields_by_name['number']._options = None
_COMPANY_PHONENUMBER.fields_by_name['country_code']._options = None
_COMPANY_PHONENUMBER.fields_by_name['description']._options = None
_COMPANY_EMAILADDRESS.fields_by_name['email']._options = None
_COMPANY.fields_by_name['head_of_company']._options = None
_COMPANY.fields_by_name['cluster_company_id']._options = None
# @@protoc_insertion_point(module_scope)