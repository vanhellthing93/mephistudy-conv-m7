# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: task.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'task.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntask.proto\x12\x04task\"H\n\x11\x43reateTaskRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\"T\n\x0cTaskResponse\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\"!\n\x0eGetTaskRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t2}\n\x0bTaskService\x12\x39\n\nCreateTask\x12\x17.task.CreateTaskRequest\x1a\x12.task.TaskResponse\x12\x33\n\x07GetTask\x12\x14.task.GetTaskRequest\x1a\x12.task.TaskResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATETASKREQUEST']._serialized_start=20
  _globals['_CREATETASKREQUEST']._serialized_end=92
  _globals['_TASKRESPONSE']._serialized_start=94
  _globals['_TASKRESPONSE']._serialized_end=178
  _globals['_GETTASKREQUEST']._serialized_start=180
  _globals['_GETTASKREQUEST']._serialized_end=213
  _globals['_TASKSERVICE']._serialized_start=215
  _globals['_TASKSERVICE']._serialized_end=340
# @@protoc_insertion_point(module_scope)
