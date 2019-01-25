from .hclCollidable import hclCollidable
from .hclVertexSelectionInput import hclVertexSelectionInput
import struct


class hclSimClothSetupObjectPerInstanceCollidable(object):
    collidable: any
    collidingParticles: hclVertexSelectionInput
    drivingBoneName: str
    pinchDetectionEnabled: bool
    pinchDetectionPriority: int
    pinchDetectionRadius: float

    def __init__(self, infile):
        self.collidable = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.collidingParticles = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.drivingBoneName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.pinchDetectionEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.pinchDetectionPriority = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.pinchDetectionRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} collidable={collidable}, collidingParticles={collidingParticles}, drivingBoneName=\"{drivingBoneName}\", pinchDetectionEnabled={pinchDetectionEnabled}, pinchDetectionPriority={pinchDetectionPriority}, pinchDetectionRadius={pinchDetectionRadius}>".format(**{
            "class_name": self.__class__.__name__,
            "collidable": self.collidable,
            "collidingParticles": self.collidingParticles,
            "drivingBoneName": self.drivingBoneName,
            "pinchDetectionEnabled": self.pinchDetectionEnabled,
            "pinchDetectionPriority": self.pinchDetectionPriority,
            "pinchDetectionRadius": self.pinchDetectionRadius,
        })
