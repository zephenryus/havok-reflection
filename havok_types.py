from typing import List

from havok_classes.common import vector4


class type_base(object):
    python_type: type
    struct_char: str
    struct_size: int
    reflection_type: str

    def __init__(self, python_type: type, struct_char: str, struct_size: int, reflection_type: str):
        self.python_type = python_type
        self.struct_char = struct_char
        self.struct_size = struct_size
        self.reflection_type = reflection_type


havok_types = {
    'TYPE_ARRAY': type_base(List, '', 0, 'TYPE_ARRAY'),
    'TYPE_BOOL': type_base(bool, '?', 1, 'TYPE_BOOL'),
    'TYPE_CHAR': type_base(str, 'c', 1, 'TYPE_CHAR'),
    'TYPE_CSTRING': type_base(str, '', 0, 'TYPE_CSTRING'),
    'TYPE_ENUM': type_base(enumerate, '', 0, 'TYPE_ENUM'),
    'TYPE_FLAGS': type_base(any, '', 0, 'TYPE_FLAGS'),
    'TYPE_HALF': type_base(int, 'h', 2, 'TYPE_HALF'),
    'TYPE_INT16': type_base(int, 'h', 2, 'TYPE_INT16'),
    'TYPE_INT32': type_base(int, 'i', 4, 'TYPE_INT32'),
    'TYPE_INT64': type_base(int, 'q', 8, 'TYPE_INT64'),
    'TYPE_INT8': type_base(int, 'b', 1, 'TYPE_INT8'),
    'TYPE_MATRIX3': type_base(any, '', 0, 'TYPE_MATRIX3'),
    'TYPE_MATRIX4': type_base(any, '', 0, 'TYPE_MATRIX4'),
    'TYPE_POINTER': type_base(any, '', 0, 'TYPE_POINTER'),
    'TYPE_QSTRANSFORM': type_base(any, '', 0, 'TYPE_QSTRANSFORM'),
    'TYPE_QUATERNION': type_base(any, '', 0, 'TYPE_QUATERNION'),
    'TYPE_REAL': type_base(float, 'f', 4, 'TYPE_REAL'),
    'TYPE_ROTATION': type_base(any, '', 0, 'TYPE_ROTATION'),
    'TYPE_SIMPLEARRAY': type_base(any, '', 0, 'TYPE_SIMPLEARRAY'),
    'TYPE_STRINGPTR': type_base(str, 's', 0, 'TYPE_STRINGPTR'),
    'TYPE_STRUCT': type_base(any, '', 0, 'TYPE_STRUCT'),
    'TYPE_TRANSFORM': type_base(any, '', 0, 'TYPE_TRANSFORM'),
    'TYPE_UINT16': type_base(int, 'H', 2, 'TYPE_UINT16'),
    'TYPE_UINT32': type_base(int, 'I', 4, 'TYPE_UINT32'),
    'TYPE_UINT64': type_base(int, 'Q', 8, 'TYPE_UINT64'),
    'TYPE_UINT8': type_base(int, 'B', 1, 'TYPE_UINT8'),
    'TYPE_ULONG': type_base(int, 'L', 8, 'TYPE_ULONG'),
    'TYPE_VARIANT': type_base(any, '', 0, 'TYPE_VARIANT'),
    'TYPE_VECTOR4': type_base(vector4, '4f', 16, 'TYPE_VECTOR4'),
    'TYPE_VOID': type_base(any, '', 0, 'TYPE_VOID'),
}