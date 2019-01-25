import struct
from .enums import WalkableTriangleSettings


class hkaiOverlappingTrianglesSettings(object):
    coplanarityTolerance: float
    raycastLengthMultiplier: float
    walkableTriangleSettings: WalkableTriangleSettings

    def __init__(self, infile):
        self.coplanarityTolerance = struct.unpack('>f', infile.read(4))
        self.raycastLengthMultiplier = struct.unpack('>f', infile.read(4))
        self.walkableTriangleSettings = WalkableTriangleSettings(infile)  # TYPE_ENUM
