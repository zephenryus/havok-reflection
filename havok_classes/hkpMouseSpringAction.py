from .hkpUnaryAction import hkpUnaryAction
from .common import vector4, any
import struct


class hkpMouseSpringAction(hkpUnaryAction):
    positionInRbLocal: vector4
    mousePositionInWorld: vector4
    springDamping: float
    springElasticity: float
    maxRelativeForce: float
    objectDamping: float
    shapeKey: int
    applyCallbacks: any

    def __init__(self, infile):
        self.positionInRbLocal = struct.unpack('>4f', infile.read(16))
        self.mousePositionInWorld = struct.unpack('>4f', infile.read(16))
        self.springDamping = struct.unpack('>f', infile.read(4))
        self.springElasticity = struct.unpack('>f', infile.read(4))
        self.maxRelativeForce = struct.unpack('>f', infile.read(4))
        self.objectDamping = struct.unpack('>f', infile.read(4))
        self.shapeKey = struct.unpack('>I', infile.read(4))
        self.applyCallbacks = any(infile)  # TYPE_ARRAY
