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
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.sweptTransform = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.deltaAngle = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.objectRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.linearDamping = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.angularDamping = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.timeFactor = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.maxLinearVelocity = hkUFloat8(infile)  # TYPE_STRUCT:TYPE_VOID
        self.maxAngularVelocity = hkUFloat8(infile)  # TYPE_STRUCT:TYPE_VOID
        self.deactivationClass = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transform={transform}, sweptTransform={sweptTransform}, deltaAngle={deltaAngle}, objectRadius={objectRadius}, linearDamping={linearDamping}, angularDamping={angularDamping}, timeFactor={timeFactor}, maxLinearVelocity={maxLinearVelocity}, maxAngularVelocity={maxAngularVelocity}, deactivationClass={deactivationClass}>".format(**{
            "class_name": self.__class__.__name__,
            "transform": self.transform,
            "sweptTransform": self.sweptTransform,
            "deltaAngle": self.deltaAngle,
            "objectRadius": self.objectRadius,
            "linearDamping": self.linearDamping,
            "angularDamping": self.angularDamping,
            "timeFactor": self.timeFactor,
            "maxLinearVelocity": self.maxLinearVelocity,
            "maxAngularVelocity": self.maxAngularVelocity,
            "deactivationClass": self.deactivationClass,
        })
