from .common import vector4


class hkSkinnedMeshShapePart(object):
    startVertex: int
    numVertices: int
    startIndex: int
    numIndices: int
    boneSetId: int
    meshSectionIndex: int
    boundingSphere: vector4
