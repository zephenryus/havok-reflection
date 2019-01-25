from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping
import struct


class hkIndexedTransformSet(hkReferencedObject):
    matrices: List[any]
    inverseMatrices: List[any]
    matricesOrder: List[int]
    matricesNames: List[str]
    indexMappings: List[hkMeshBoneIndexMapping]
    allMatricesAreAffine: bool

    def __init__(self, infile):
        self.matrices = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4
        self.inverseMatrices = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4
        self.matricesOrder = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16
        self.matricesNames = get_array(infile, str, 0)  # TYPE_ARRAY:TYPE_STRINGPTR
        self.indexMappings = get_array(infile, hkMeshBoneIndexMapping, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.allMatricesAreAffine = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} matrices=[{matrices}], inverseMatrices=[{inverseMatrices}], matricesOrder=[{matricesOrder}], matricesNames=[{matricesNames}], indexMappings=[{indexMappings}], allMatricesAreAffine={allMatricesAreAffine}>".format(**{
            "class_name": self.__class__.__name__,
            "matrices": self.matrices,
            "inverseMatrices": self.inverseMatrices,
            "matricesOrder": self.matricesOrder,
            "matricesNames": self.matricesNames,
            "indexMappings": self.indexMappings,
            "allMatricesAreAffine": self.allMatricesAreAffine,
        })
