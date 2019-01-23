from .hkMeshTexture import hkMeshTexture


class hkMemoryMeshTexture(hkMeshTexture):
	filename: any
	data: any
	format: any
	hasMipMaps: bool
	filterMode: any
	usageHint: any
	textureCoordChannel: int
