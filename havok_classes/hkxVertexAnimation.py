from .hkReferencedObject import hkReferencedObject
import struct
from .hkxVertexBuffer import hkxVertexBuffer
from .common import any
from .hkxVertexAnimationUsageMap import hkxVertexAnimationUsageMap


class hkxVertexAnimation(hkReferencedObject):
    time: float
    vertData: hkxVertexBuffer
    vertexIndexMap: any
    componentMap: hkxVertexAnimationUsageMap

    def __init__(self, infile):
        self.time = struct.unpack('>f', infile.read(4))
        self.vertData = hkxVertexBuffer(infile)  # TYPE_STRUCT
        self.vertexIndexMap = any(infile)  # TYPE_ARRAY
        self.componentMap = hkxVertexAnimationUsageMap(infile)  # TYPE_ARRAY
