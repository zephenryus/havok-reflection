from .hclBufferDefinition import hclBufferDefinition


class hclStaticShadowBufferDefinition(hclBufferDefinition):
	staticPositions: any
	staticNormals: any
	staticTangents: any
	staticBiTangents: any
	triangleIndices: any
