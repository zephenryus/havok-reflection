from .hclOperator import hclOperator
from .hclUpdateSomeVertexFramesOperatorTriangle import hclUpdateSomeVertexFramesOperatorTriangle
from .common import any
import struct


class hclUpdateSomeVertexFramesOperator(hclOperator):
    involvedTriangles: hclUpdateSomeVertexFramesOperatorTriangle
    involvedVertices: any
    selectionVertexToInvolvedVertex: any
    involvedVertexToNormalID: any
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
        self.involvedTriangles = hclUpdateSomeVertexFramesOperatorTriangle(infile)  # TYPE_ARRAY
        self.involvedVertices = any(infile)  # TYPE_ARRAY
        self.selectionVertexToInvolvedVertex = any(infile)  # TYPE_ARRAY
        self.involvedVertexToNormalID = any(infile)  # TYPE_ARRAY
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
