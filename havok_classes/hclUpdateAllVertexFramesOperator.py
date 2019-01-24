from .hclOperator import hclOperator
from .common import any


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
