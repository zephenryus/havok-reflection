from .hclOperator import hclOperator
from .common import any
import struct


class hclUpdateAllVertexFramesOperator(hclOperator):
    vertToNormalID: any
    triangleFlips: any
    referenceVertices: any
    tangentEdgeCosAngle: any
    tangentEdgeSinAngle: any
    biTangentFlip: any
    bufferIdx: int
    numUniqueNormalIDs: int
    updateNormals: bool
    updateTangents: bool
    updateBiTangents: bool

    def __init__(self, infile):
        self.vertToNormalID = any(infile)  # TYPE_ARRAY
        self.triangleFlips = any(infile)  # TYPE_ARRAY
        self.referenceVertices = any(infile)  # TYPE_ARRAY
        self.tangentEdgeCosAngle = any(infile)  # TYPE_ARRAY
        self.tangentEdgeSinAngle = any(infile)  # TYPE_ARRAY
        self.biTangentFlip = any(infile)  # TYPE_ARRAY
        self.bufferIdx = struct.unpack('>I', infile.read(4))
        self.numUniqueNormalIDs = struct.unpack('>I', infile.read(4))
        self.updateNormals = struct.unpack('>?', infile.read(1))
        self.updateTangents = struct.unpack('>?', infile.read(1))
        self.updateBiTangents = struct.unpack('>?', infile.read(1))
