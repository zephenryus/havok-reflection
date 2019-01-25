from .hkpExtendedMeshShapeSubpart import hkpExtendedMeshShapeSubpart
from typing import List
from .common import get_array
from .hkpConvexShape import hkpConvexShape
import struct


class hkpExtendedMeshShapeShapesSubpart(hkpExtendedMeshShapeSubpart):
    childShapes: List[hkpConvexShape]
    rotation: any
    translation: vector4

    def __init__(self, infile):
        self.childShapes = get_array(infile, hkpConvexShape, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.rotation = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.translation = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} childShapes=[{childShapes}], rotation={rotation}, translation={translation}>".format(**{
            "class_name": self.__class__.__name__,
            "childShapes": self.childShapes,
            "rotation": self.rotation,
            "translation": self.translation,
        })
