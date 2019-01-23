from .hclBufferSetupObject import hclBufferSetupObject
from .hclSetupMesh import hclSetupMesh


class hclScratchBufferSetupObject(hclBufferSetupObject):
	name: any
	setupMesh: hclSetupMesh
	storeNormals: bool
	storeTangentsAndBiTangents: bool
	storeTriangles: bool
