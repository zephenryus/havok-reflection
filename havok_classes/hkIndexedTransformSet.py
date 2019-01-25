from .hkReferencedObject import hkReferencedObject
from .common import any
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping
import struct


class hkIndexedTransformSet(hkReferencedObject):
    matrices: any
    inverseMatrices: any
    matricesOrder: any
    matricesNames: any
    indexMappings: hkMeshBoneIndexMapping
    allMatricesAreAffine: bool

    def __init__(self, infile):
        self.matrices = any(infile)  # TYPE_ARRAY
        self.inverseMatrices = any(infile)  # TYPE_ARRAY
        self.matricesOrder = any(infile)  # TYPE_ARRAY
        self.matricesNames = any(infile)  # TYPE_ARRAY
        self.indexMappings = hkMeshBoneIndexMapping(infile)  # TYPE_ARRAY
        self.allMatricesAreAffine = struct.unpack('>?', infile.read(1))
