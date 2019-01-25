from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkxAnimatedQuaternion(hkReferencedObject):
    quaternions: List[float]

    def __init__(self, infile):
        self.quaternions = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL

    def __repr__(self):
        return "<{class_name} quaternions=[{quaternions}]>".format(**{
            "class_name": self.__class__.__name__,
            "quaternions": self.quaternions,
        })
