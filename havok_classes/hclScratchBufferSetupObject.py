from .hclBufferSetupObject import hclBufferSetupObject
from .hclSetupMesh import hclSetupMesh


class hclScratchBufferSetupObject(hclBufferSetupObject):
    name: str
    setupMesh: hclSetupMesh
    storeNormals: bool
    storeTangentsAndBiTangents: bool
    storeTriangles: bool
