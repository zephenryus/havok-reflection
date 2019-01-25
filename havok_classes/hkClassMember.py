from enum import Enum
from .hkClass import hkClass
from .hkClassEnum import hkClassEnum
from .enums import Type
import struct
from .hkCustomAttributes import hkCustomAttributes


class Type(Enum):
    TYPE_VOID = 0
    TYPE_BOOL = 1
    TYPE_CHAR = 2
    TYPE_INT8 = 3
    TYPE_UINT8 = 4
    TYPE_INT16 = 5
    TYPE_UINT16 = 6
    TYPE_INT32 = 7
    TYPE_UINT32 = 8
    TYPE_INT64 = 9
    TYPE_UINT64 = 10
    TYPE_REAL = 11
    TYPE_VECTOR4 = 12
    TYPE_QUATERNION = 13
    TYPE_MATRIX3 = 14
    TYPE_ROTATION = 15
    TYPE_QSTRANSFORM = 16
    TYPE_MATRIX4 = 17
    TYPE_TRANSFORM = 18
    TYPE_ZERO = 19
    TYPE_POINTER = 20
    TYPE_FUNCTIONPOINTER = 21
    TYPE_ARRAY = 22
    TYPE_INPLACEARRAY = 23
    TYPE_ENUM = 24
    TYPE_STRUCT = 25
    TYPE_SIMPLEARRAY = 26
    TYPE_HOMOGENEOUSARRAY = 27
    TYPE_VARIANT = 28
    TYPE_CSTRING = 29
    TYPE_ULONG = 30
    TYPE_FLAGS = 31
    TYPE_HALF = 32
    TYPE_STRINGPTR = 33
    TYPE_RELARRAY = 34
    TYPE_MAX = 35


class FlagValues(Enum):
    FLAGS_NONE = 0
    ALIGN_8 = 128
    ALIGN_16 = 256
    NOT_OWNED = 512
    SERIALIZE_IGNORED = 1024
    ALIGN_32 = 2048
    ALIGN_REAL = 256


class DeprecatedFlagValues(Enum):
    DEPRECATED_SIZE_8 = 8
    DEPRECATED_ENUM_8 = 8
    DEPRECATED_SIZE_16 = 16
    DEPRECATED_ENUM_16 = 16
    DEPRECATED_SIZE_32 = 32
    DEPRECATED_ENUM_32 = 32


class hkClassMember(object):
    name: str
    class: any
    enum: any
    type: Type
    subtype: Type
    cArraySize: int
    flags: any
    offset: int
    attributes: any

    def __init__(self, infile):
        self.name = str(infile)  # TYPE_CSTRING:TYPE_VOID
        self.class = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.enum = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.type = Type(infile)  # TYPE_ENUM:TYPE_UINT8
        self.subtype = Type(infile)  # TYPE_ENUM:TYPE_UINT8
        self.cArraySize = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT16
        self.offset = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.attributes = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} name=\"{name}\", class={class}, enum={enum}, type={type}, subtype={subtype}, cArraySize={cArraySize}, flags={flags}, offset={offset}, attributes={attributes}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "class": self.class,
            "enum": self.enum,
            "type": self.type,
            "subtype": self.subtype,
            "cArraySize": self.cArraySize,
            "flags": self.flags,
            "offset": self.offset,
            "attributes": self.attributes,
        })
