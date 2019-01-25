from .hkReferencedObject import hkReferencedObject
import struct
from .hkxVertexBuffer import hkxVertexBuffer
from typing import List
from .common import get_array
from .hkxVertexAnimationUsageMap import hkxVertexAnimationUsageMap


class hkxVertexAnimation(hkReferencedObject):
    time: float
    vertData: hkxVertexBuffer
    vertexIndexMap: List[int]
    componentMap: List[hkxVertexAnimationUsageMap]

    def __init__(self, infile):
        self.time = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.vertData = hkxVertexBuffer(infile)  # TYPE_STRUCT:TYPE_VOID
        self.vertexIndexMap = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.componentMap = get_array(infile, hkxVertexAnimationUsageMap, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} time={time}, vertData={vertData}, vertexIndexMap=[{vertexIndexMap}], componentMap=[{componentMap}]>".format(**{
            "class_name": self.__class__.__name__,
            "time": self.time,
            "vertData": self.vertData,
            "vertexIndexMap": self.vertexIndexMap,
            "componentMap": self.componentMap,
        })
