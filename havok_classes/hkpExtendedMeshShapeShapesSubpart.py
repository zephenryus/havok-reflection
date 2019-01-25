from .hkpExtendedMeshShapeSubpart import hkpExtendedMeshShapeSubpart
from .hkpConvexShape import hkpConvexShape
from .common import any, vector4
import struct


class hkpExtendedMeshShapeShapesSubpart(hkpExtendedMeshShapeSubpart):
    childShapes: hkpConvexShape
    rotation: any
    translation: vector4

    def __init__(self, infile):
        self.childShapes = hkpConvexShape(infile)  # TYPE_ARRAY
        self.rotation = any(infile)  # TYPE_QUATERNION
        self.translation = struct.unpack('>4f', infile.read(16))
