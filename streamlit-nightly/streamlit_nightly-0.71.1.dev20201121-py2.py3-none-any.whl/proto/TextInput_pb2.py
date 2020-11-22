# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/TextInput.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/TextInput.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fstreamlit/proto/TextInput.proto\"\x8c\x01\n\tTextInput\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\t\x12\x1d\n\x04type\x18\x04 \x01(\x0e\x32\x0f.TextInput.Type\x12\x11\n\tmax_chars\x18\x05 \x01(\r\"!\n\x04Type\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08PASSWORD\x10\x01\x62\x06proto3')
)



_TEXTINPUT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='TextInput.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSWORD', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=143,
  serialized_end=176,
)
_sym_db.RegisterEnumDescriptor(_TEXTINPUT_TYPE)


_TEXTINPUT = _descriptor.Descriptor(
  name='TextInput',
  full_name='TextInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='TextInput.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='TextInput.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='TextInput.default', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='TextInput.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_chars', full_name='TextInput.max_chars', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TEXTINPUT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=176,
)

_TEXTINPUT.fields_by_name['type'].enum_type = _TEXTINPUT_TYPE
_TEXTINPUT_TYPE.containing_type = _TEXTINPUT
DESCRIPTOR.message_types_by_name['TextInput'] = _TEXTINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextInput = _reflection.GeneratedProtocolMessageType('TextInput', (_message.Message,), dict(
  DESCRIPTOR = _TEXTINPUT,
  __module__ = 'streamlit.proto.TextInput_pb2'
  # @@protoc_insertion_point(class_scope:TextInput)
  ))
_sym_db.RegisterMessage(TextInput)


# @@protoc_insertion_point(module_scope)
