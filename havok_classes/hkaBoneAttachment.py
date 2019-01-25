from .hkReferencedObject import hkReferencedObject
from .common import any
import struct


class hkaBoneAttachment(hkReferencedObject):
    originalSkeletonName: str
    boneFromAttachment: any
    attachment: hkReferencedObject
    name: str
    boneIndex: int

    def __init__(self, infile):
        self.originalSkeletonName = struct.unpack('>s', infile.read(0))
        self.boneFromAttachment = any(infile)  # TYPE_MATRIX4
        self.attachment = hkReferencedObject(infile)  # TYPE_POINTER
        self.name = struct.unpack('>s', infile.read(0))
        self.boneIndex = struct.unpack('>h', infile.read(2))
