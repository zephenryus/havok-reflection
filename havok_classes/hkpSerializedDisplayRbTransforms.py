from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpSerializedDisplayRbTransformsDisplayTransformPair import hkpSerializedDisplayRbTransformsDisplayTransformPair


class hkpSerializedDisplayRbTransforms(hkReferencedObject):
    transforms: List[hkpSerializedDisplayRbTransformsDisplayTransformPair]

    def __init__(self, infile):
        self.transforms = get_array(infile, hkpSerializedDisplayRbTransformsDisplayTransformPair, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} transforms=[{transforms}]>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
        })
