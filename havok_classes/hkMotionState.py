from .common import any, vector4
import struct
from .hkUFloat8 import hkUFloat8


class hkMotionState(object):
    transform: any
    sweptTransform: vector4
    deltaAngle: vector4
    objectRadius: float
    linearDamping: int
    angularDamping: int
    timeFactor: int
    maxLinearVelocity: hkUFloat8
    maxAngularVelocity: hkUFloat8
    deactivationClass: int

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_TRANSFORM
        self.sweptTransform = struct.unpack('>4f', infile.read(16))
        self.deltaAngle = struct.unpack('>4f', infile.read(16))
        self.objectRadius = struct.unpack('>f', infile.read(4))
        self.linearDamping = struct.unpack('>h', infile.read(2))
        self.angularDamping = struct.unpack('>h', infile.read(2))
        self.timeFactor = struct.unpack('>h', infile.read(2))
        self.maxLinearVelocity = hkUFloat8(infile)  # TYPE_STRUCT
        self.maxAngularVelocity = hkUFloat8(infile)  # TYPE_STRUCT
        self.deactivationClass = struct.unpack('>B', infile.read(1))
