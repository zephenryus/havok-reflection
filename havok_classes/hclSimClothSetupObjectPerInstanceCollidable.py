from .hclCollidable import hclCollidable
from .hclVertexSelectionInput import hclVertexSelectionInput
import struct


class hclSimClothSetupObjectPerInstanceCollidable(object):
    collidable: hclCollidable
    collidingParticles: hclVertexSelectionInput
    drivingBoneName: str
    pinchDetectionEnabled: bool
    pinchDetectionPriority: int
    pinchDetectionRadius: float

    def __init__(self, infile):
        self.collidable = hclCollidable(infile)  # TYPE_POINTER
        self.collidingParticles = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.drivingBoneName = struct.unpack('>s', infile.read(0))
        self.pinchDetectionEnabled = struct.unpack('>?', infile.read(1))
        self.pinchDetectionPriority = struct.unpack('>b', infile.read(1))
        self.pinchDetectionRadius = struct.unpack('>f', infile.read(4))
