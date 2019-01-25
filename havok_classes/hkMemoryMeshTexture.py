from .hkMeshTexture import hkMeshTexture
from .common import any
from .enums import Format, FilterMode, TextureUsageType
import struct


class hkMemoryMeshTexture(hkMeshTexture):
    filename: str
    data: any
    format: Format
    hasMipMaps: bool
    filterMode: FilterMode
    usageHint: TextureUsageType
    textureCoordChannel: int

    def __init__(self, infile):
        self.filename = struct.unpack('>s', infile.read(0))
        self.data = any(infile)  # TYPE_ARRAY
        self.format = Format(infile)  # TYPE_ENUM
        self.hasMipMaps = struct.unpack('>?', infile.read(1))
        self.filterMode = FilterMode(infile)  # TYPE_ENUM
        self.usageHint = TextureUsageType(infile)  # TYPE_ENUM
        self.textureCoordChannel = struct.unpack('>i', infile.read(4))
