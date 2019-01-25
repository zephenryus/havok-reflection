from .hkReferencedObject import hkReferencedObject
import struct
from .common import any
from .hkaiAvoidanceSolverSphereObstacle import hkaiAvoidanceSolverSphereObstacle
from .hkaiAvoidanceSolverBoundaryObstacle import hkaiAvoidanceSolverBoundaryObstacle


class hkaiObstacleGenerator(hkReferencedObject):
    useSpheres: bool
    useBoundaries: bool
    clipBoundaries: bool
    transform: any
    spheres: hkaiAvoidanceSolverSphereObstacle
    boundaries: hkaiAvoidanceSolverBoundaryObstacle
    userData: int

    def __init__(self, infile):
        self.useSpheres = struct.unpack('>?', infile.read(1))
        self.useBoundaries = struct.unpack('>?', infile.read(1))
        self.clipBoundaries = struct.unpack('>?', infile.read(1))
        self.transform = any(infile)  # TYPE_TRANSFORM
        self.spheres = hkaiAvoidanceSolverSphereObstacle(infile)  # TYPE_ARRAY
        self.boundaries = hkaiAvoidanceSolverBoundaryObstacle(infile)  # TYPE_ARRAY
        self.userData = struct.unpack('>L', infile.read(8))
