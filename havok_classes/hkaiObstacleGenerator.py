from .hkReferencedObject import hkReferencedObject
import struct
from typing import List
from .common import get_array
from .hkaiAvoidanceSolverSphereObstacle import hkaiAvoidanceSolverSphereObstacle
from .hkaiAvoidanceSolverBoundaryObstacle import hkaiAvoidanceSolverBoundaryObstacle


class hkaiObstacleGenerator(hkReferencedObject):
    useSpheres: bool
    useBoundaries: bool
    clipBoundaries: bool
    transform: any
    spheres: List[hkaiAvoidanceSolverSphereObstacle]
    boundaries: List[hkaiAvoidanceSolverBoundaryObstacle]
    userData: int

    def __init__(self, infile):
        self.useSpheres = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.useBoundaries = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.clipBoundaries = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.spheres = get_array(infile, hkaiAvoidanceSolverSphereObstacle, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.boundaries = get_array(infile, hkaiAvoidanceSolverBoundaryObstacle, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} useSpheres={useSpheres}, useBoundaries={useBoundaries}, clipBoundaries={clipBoundaries}, transform={transform}, spheres=[{spheres}], boundaries=[{boundaries}], userData={userData}>".format(**{
            "class_name": self.__class__.__name__,
            "useSpheres": self.useSpheres,
            "useBoundaries": self.useBoundaries,
            "clipBoundaries": self.clipBoundaries,
            "transform": self.transform,
            "spheres": self.spheres,
            "boundaries": self.boundaries,
            "userData": self.userData,
        })
