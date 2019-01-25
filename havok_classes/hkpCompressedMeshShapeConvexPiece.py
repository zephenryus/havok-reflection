from .common import vector4, any
import struct


class hkpCompressedMeshShapeConvexPiece(object):
    offset: vector4
    vertices: any
    reference: int
    transformIndex: int

    def __init__(self, infile):
        self.offset = struct.unpack('>4f', infile.read(16))
        self.vertices = any(infile)  # TYPE_ARRAY
        self.reference = struct.unpack('>H', infile.read(2))
        self.transformIndex = struct.unpack('>H', infile.read(2))
