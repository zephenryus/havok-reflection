from .hkReferencedObject import hkReferencedObject
import struct
from .hkpTyremarkPoint import hkpTyremarkPoint


class hkpTyremarksWheel(hkReferencedObject):
    currentPosition: int
    numPoints: int
    tyremarkPoints: hkpTyremarkPoint

    def __init__(self, infile):
        self.currentPosition = struct.unpack('>i', infile.read(4))
        self.numPoints = struct.unpack('>i', infile.read(4))
        self.tyremarkPoints = hkpTyremarkPoint(infile)  # TYPE_ARRAY
