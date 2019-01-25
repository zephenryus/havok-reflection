from .hkaAnimation import hkaAnimation
from typing import List
from .common import get_array


class hkaInterleavedUncompressedAnimation(hkaAnimation):
    transforms: List[any]
    floats: List[float]

    def __init__(self, infile):
        self.transforms = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_QSTRANSFORM
        self.floats = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL

    def __repr__(self):
        return "<{class_name} transforms=[{transforms}], floats=[{floats}]>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "floats": self.floats,
        })
