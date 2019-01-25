import struct
from .hkpRigidBody import hkpRigidBody
from .enums import Operation


class hkpTriggerVolumeEventInfo(object):
    sortValue: int
    body: any
    operation: Operation

    def __init__(self, infile):
        self.sortValue = struct.unpack('>Q', infile.read(8))  # TYPE_UINT64:TYPE_VOID
        self.body = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.operation = Operation(infile)  # TYPE_ENUM:TYPE_INT32

    def __repr__(self):
        return "<{class_name} sortValue={sortValue}, body={body}, operation={operation}>".format(**{
            "class_name": self.__class__.__name__,
            "sortValue": self.sortValue,
            "body": self.body,
            "operation": self.operation,
        })
