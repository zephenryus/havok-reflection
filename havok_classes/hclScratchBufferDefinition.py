from .hclBufferDefinition import hclBufferDefinition


class hclScratchBufferDefinition(hclBufferDefinition):
	triangleIndices: any
	storeNormals: bool
	storeTangentsAndBiTangents: bool
