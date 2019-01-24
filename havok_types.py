from havok_classes.common import vector4


class type_base(object):
    python_type: type
    struct_char: str

    def __init__(self, python_type: type, struct_char: str):
        self.python_type = python_type
        self.struct_char = struct_char


havok_types = {
    'TYPE_ARRAY': type_base(any, ''),
    'TYPE_BOOL': type_base(bool, '?'),
    'TYPE_CHAR': type_base(str, 'c'),
    'TYPE_CSTRING': type_base(str, ''),
    'TYPE_ENUM': type_base(enumerate, ''),
    'TYPE_FLAGS': type_base(any, ''),
    'TYPE_HALF': type_base(int, 'h'),
    'TYPE_INT16': type_base(int, 'h'),
    'TYPE_INT32': type_base(int, 'i'),
    'TYPE_INT64': type_base(int, 'q'),
    'TYPE_INT8': type_base(int, 'b'),
    'TYPE_MATRIX3': type_base(any, ''),
    'TYPE_MATRIX4': type_base(any, ''),
    'TYPE_POINTER': type_base(any, ''),
    'TYPE_QSTRANSFORM': type_base(any, ''),
    'TYPE_QUATERNION': type_base(any, ''),
    'TYPE_REAL': type_base(float, 'f'),
    'TYPE_ROTATION': type_base(any, ''),
    'TYPE_SIMPLEARRAY': type_base(any, ''),
    'TYPE_STRINGPTR': type_base(str, 's'),
    'TYPE_STRUCT': type_base(any, ''),
    'TYPE_TRANSFORM': type_base(any, ''),
    'TYPE_UINT16': type_base(int, 'H'),
    'TYPE_UINT32': type_base(int, 'I'),
    'TYPE_UINT64': type_base(int, 'Q'),
    'TYPE_UINT8': type_base(int, 'B'),
    'TYPE_ULONG': type_base(int, 'L'),
    'TYPE_VARIANT': type_base(any, ''),
    'TYPE_VECTOR4': type_base(vector4, '4f'),
    'TYPE_VOID': type_base(any, '')
}