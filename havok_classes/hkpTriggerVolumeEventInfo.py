import struct
from .hkpRigidBody import hkpRigidBody
from .enums import Operation


class hkpTriggerVolumeEventInfo(object):
    sortValue: int
    body: hkpRigidBody
    operation: Operation

    def __init__(self, infile):
        self.sortValue = struct.unpack('>Q', infile.read(8))
        self.body = hkpRigidBody(infile)  # TYPE_POINTER
        self.operation = Operation(infile)  # TYPE_ENUM
