from .hkReferencedObject import hkReferencedObject
from .common import any
from .hclClothStateBufferAccess import hclClothStateBufferAccess
from .hclClothStateTransformSetAccess import hclClothStateTransformSetAccess


class hclClothState(hkReferencedObject):
    name: str
    operators: any
    usedBuffers: hclClothStateBufferAccess
    usedTransformSets: hclClothStateTransformSetAccess
    usedSimCloths: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.operators = any(infile)  # TYPE_ARRAY
        self.usedBuffers = hclClothStateBufferAccess(infile)  # TYPE_ARRAY
        self.usedTransformSets = hclClothStateTransformSetAccess(infile)  # TYPE_ARRAY
        self.usedSimCloths = any(infile)  # TYPE_ARRAY
