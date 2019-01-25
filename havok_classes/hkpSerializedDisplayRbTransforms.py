from .hkReferencedObject import hkReferencedObject
from .hkpSerializedDisplayRbTransformsDisplayTransformPair import hkpSerializedDisplayRbTransformsDisplayTransformPair


class hkpSerializedDisplayRbTransforms(hkReferencedObject):
    transforms: hkpSerializedDisplayRbTransformsDisplayTransformPair

    def __init__(self, infile):
        self.transforms = hkpSerializedDisplayRbTransformsDisplayTransformPair(infile)  # TYPE_ARRAY
