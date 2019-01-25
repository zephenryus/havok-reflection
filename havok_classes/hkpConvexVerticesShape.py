from .hkpConvexShape import hkpConvexShape
from .common import vector4, any
import struct
from .hkpConvexVerticesConnectivity import hkpConvexVerticesConnectivity


class hkpConvexVerticesShape(hkpConvexShape):
    aabbHalfExtents: vector4
    aabbCenter: vector4
    rotatedVertices: any
    numVertices: int
    useSpuBuffer: bool
    planeEquations: any
    connectivity: hkpConvexVerticesConnectivity

    def __init__(self, infile):
        self.aabbHalfExtents = struct.unpack('>4f', infile.read(16))
        self.aabbCenter = struct.unpack('>4f', infile.read(16))
        self.rotatedVertices = any(infile)  # TYPE_ARRAY
        self.numVertices = struct.unpack('>i', infile.read(4))
        self.useSpuBuffer = struct.unpack('>?', infile.read(1))
        self.planeEquations = any(infile)  # TYPE_ARRAY
        self.connectivity = hkpConvexVerticesConnectivity(infile)  # TYPE_POINTER
