from .hkpBroadPhaseHandle import hkpBroadPhaseHandle
import struct


class hkpTypedBroadPhaseHandle(hkpBroadPhaseHandle):
    type: int
    ownerOffset: int
    objectQualityType: int
    collisionFilterInfo: int

    def __init__(self, infile):
        self.type = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.ownerOffset = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.objectQualityType = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.collisionFilterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} type={type}, ownerOffset={ownerOffset}, objectQualityType={objectQualityType}, collisionFilterInfo={collisionFilterInfo}>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
            "ownerOffset": self.ownerOffset,
            "objectQualityType": self.objectQualityType,
            "collisionFilterInfo": self.collisionFilterInfo,
        })
