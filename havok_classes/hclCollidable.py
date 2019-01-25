from .hkReferencedObject import hkReferencedObject
from .common import any, vector4
import struct
from .hclShape import hclShape


class hclCollidable(hkReferencedObject):
    name: str
    transform: any
    linearVelocity: vector4
    angularVelocity: vector4
    pinchDetectionEnabled: bool
    pinchDetectionPriority: int
    pinchDetectionRadius: float
    shape: hclShape

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.transform = any(infile)  # TYPE_TRANSFORM
        self.linearVelocity = struct.unpack('>4f', infile.read(16))
        self.angularVelocity = struct.unpack('>4f', infile.read(16))
        self.pinchDetectionEnabled = struct.unpack('>?', infile.read(1))
        self.pinchDetectionPriority = struct.unpack('>b', infile.read(1))
        self.pinchDetectionRadius = struct.unpack('>f', infile.read(4))
        self.shape = hclShape(infile)  # TYPE_POINTER
