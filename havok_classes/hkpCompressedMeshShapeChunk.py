from .common import vector4, any
import struct


class hkpCompressedMeshShapeChunk(object):
    offset: vector4
    vertices: any
    indices: any
    stripLengths: any
    weldingInfo: any
    materialInfo: int
    reference: int
    transformIndex: int

    def __init__(self, infile):
        self.offset = struct.unpack('>4f', infile.read(16))
        self.vertices = any(infile)  # TYPE_ARRAY
        self.indices = any(infile)  # TYPE_ARRAY
        self.stripLengths = any(infile)  # TYPE_ARRAY
        self.weldingInfo = any(infile)  # TYPE_ARRAY
        self.materialInfo = struct.unpack('>I', infile.read(4))
        self.reference = struct.unpack('>H', infile.read(2))
        self.transformIndex = struct.unpack('>H', infile.read(2))
