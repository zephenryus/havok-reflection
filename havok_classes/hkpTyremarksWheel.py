from .hkReferencedObject import hkReferencedObject
import struct
from typing import List
from .common import get_array
from .hkpTyremarkPoint import hkpTyremarkPoint


class hkpTyremarksWheel(hkReferencedObject):
    currentPosition: int
    numPoints: int
    tyremarkPoints: List[hkpTyremarkPoint]

    def __init__(self, infile):
        self.currentPosition = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numPoints = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.tyremarkPoints = get_array(infile, hkpTyremarkPoint, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} currentPosition={currentPosition}, numPoints={numPoints}, tyremarkPoints=[{tyremarkPoints}]>".format(**{
            "class_name": self.__class__.__name__,
            "currentPosition": self.currentPosition,
            "numPoints": self.numPoints,
            "tyremarkPoints": self.tyremarkPoints,
        })
