from .hkMeshTexture import hkMeshTexture
from .common import any
from .enums import Format, FilterMode, TextureUsageType


class hkMemoryMeshTexture(hkMeshTexture):
    filename: str
    data: any
    format: Format
    hasMipMaps: bool
    filterMode: FilterMode
    usageHint: TextureUsageType
    textureCoordChannel: int
