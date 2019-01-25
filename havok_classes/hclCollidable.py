from .hkReferencedObject import hkReferencedObject
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
    shape: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.linearVelocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.angularVelocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.pinchDetectionEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.pinchDetectionPriority = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.pinchDetectionRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.shape = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} name=\"{name}\", transform={transform}, linearVelocity={linearVelocity}, angularVelocity={angularVelocity}, pinchDetectionEnabled={pinchDetectionEnabled}, pinchDetectionPriority={pinchDetectionPriority}, pinchDetectionRadius={pinchDetectionRadius}, shape={shape}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "transform": self.transform,
            "linearVelocity": self.linearVelocity,
            "angularVelocity": self.angularVelocity,
            "pinchDetectionEnabled": self.pinchDetectionEnabled,
            "pinchDetectionPriority": self.pinchDetectionPriority,
            "pinchDetectionRadius": self.pinchDetectionRadius,
            "shape": self.shape,
        })
