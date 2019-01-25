import struct
from typing import List
from .common import get_array


class hkpCompressedMeshShapeChunk(object):
    offset: vector4
    vertices: List[int]
    indices: List[int]
    stripLengths: List[int]
    weldingInfo: List[int]
    materialInfo: int
    reference: int
    transformIndex: int

    def __init__(self, infile):
        self.offset = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.vertices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.indices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.stripLengths = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.weldingInfo = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.materialInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.reference = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.transformIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} offset={offset}, vertices=[{vertices}], indices=[{indices}], stripLengths=[{stripLengths}], weldingInfo=[{weldingInfo}], materialInfo={materialInfo}, reference={reference}, transformIndex={transformIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "offset": self.offset,
            "vertices": self.vertices,
            "indices": self.indices,
            "stripLengths": self.stripLengths,
            "weldingInfo": self.weldingInfo,
            "materialInfo": self.materialInfo,
            "reference": self.reference,
            "transformIndex": self.transformIndex,
        })
