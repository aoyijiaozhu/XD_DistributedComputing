# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: studentinfo.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11studentinfo.proto\x12\x0bstudentinfo\"G\n\x0eStudentRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\x0e\n\x06\x63lass_\x18\x04 \x01(\t\" \n\x12StudentByIDRequest\x12\n\n\x02id\x18\x01 \x01(\t\"$\n\x14StudentByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\"\n\x0fStudentResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"A\n\x10StudentsResponse\x12-\n\x08students\x18\x01 \x03(\x0b\x32\x1b.studentinfo.StudentRequest2\xbc\x02\n\x0bStudentInfo\x12\x42\n\x03\x41\x64\x64\x12\x1b.studentinfo.StudentRequest\x1a\x1c.studentinfo.StudentResponse\"\x00\x12K\n\tQueryByID\x12\x1f.studentinfo.StudentByIDRequest\x1a\x1b.studentinfo.StudentRequest\"\x00\x12Q\n\x0bQueryByName\x12!.studentinfo.StudentByNameRequest\x1a\x1d.studentinfo.StudentsResponse\"\x00\x12I\n\x06\x44\x65lete\x12\x1f.studentinfo.StudentByIDRequest\x1a\x1c.studentinfo.StudentResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'studentinfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_STUDENTREQUEST']._serialized_start=34
  _globals['_STUDENTREQUEST']._serialized_end=105
  _globals['_STUDENTBYIDREQUEST']._serialized_start=107
  _globals['_STUDENTBYIDREQUEST']._serialized_end=139
  _globals['_STUDENTBYNAMEREQUEST']._serialized_start=141
  _globals['_STUDENTBYNAMEREQUEST']._serialized_end=177
  _globals['_STUDENTRESPONSE']._serialized_start=179
  _globals['_STUDENTRESPONSE']._serialized_end=213
  _globals['_STUDENTSRESPONSE']._serialized_start=215
  _globals['_STUDENTSRESPONSE']._serialized_end=280
  _globals['_STUDENTINFO']._serialized_start=283
  _globals['_STUDENTINFO']._serialized_end=599
# @@protoc_insertion_point(module_scope)
