from .hclBufferDefinition import hclBufferDefinition


class hclShadowBufferDefinition(hclBufferDefinition):
	triangleIndices: any
	shadowPositions: bool
	shadowNormals: bool
	shadowTangents: bool
	shadowBiTangents: bool
