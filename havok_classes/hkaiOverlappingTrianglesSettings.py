from .enums import WalkableTriangleSettings


class hkaiOverlappingTrianglesSettings(object):
    coplanarityTolerance: float
    raycastLengthMultiplier: float
    walkableTriangleSettings: WalkableTriangleSettings
