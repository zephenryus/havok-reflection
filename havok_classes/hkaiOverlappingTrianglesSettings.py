import struct
from .enums import WalkableTriangleSettings


class hkaiOverlappingTrianglesSettings(object):
    coplanarityTolerance: float
    raycastLengthMultiplier: float
    walkableTriangleSettings: WalkableTriangleSettings

    def __init__(self, infile):
        self.coplanarityTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.raycastLengthMultiplier = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.walkableTriangleSettings = WalkableTriangleSettings(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} coplanarityTolerance={coplanarityTolerance}, raycastLengthMultiplier={raycastLengthMultiplier}, walkableTriangleSettings={walkableTriangleSettings}>".format(**{
            "class_name": self.__class__.__name__,
            "coplanarityTolerance": self.coplanarityTolerance,
            "raycastLengthMultiplier": self.raycastLengthMultiplier,
            "walkableTriangleSettings": self.walkableTriangleSettings,
        })
