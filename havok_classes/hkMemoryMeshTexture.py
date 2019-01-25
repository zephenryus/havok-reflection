from .hkMeshTexture import hkMeshTexture
from typing import List
from .common import get_array
from .enums import Format, FilterMode, TextureUsageType
import struct


class hkMemoryMeshTexture(hkMeshTexture):
    filename: str
    data: List[int]
    format: Format
    hasMipMaps: bool
    filterMode: FilterMode
    usageHint: TextureUsageType
    textureCoordChannel: int

    def __init__(self, infile):
        self.filename = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.data = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.format = Format(infile)  # TYPE_ENUM:TYPE_INT8
        self.hasMipMaps = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.filterMode = FilterMode(infile)  # TYPE_ENUM:TYPE_INT8
        self.usageHint = TextureUsageType(infile)  # TYPE_ENUM:TYPE_INT8
        self.textureCoordChannel = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} filename=\"{filename}\", data=[{data}], format={format}, hasMipMaps={hasMipMaps}, filterMode={filterMode}, usageHint={usageHint}, textureCoordChannel={textureCoordChannel}>".format(**{
            "class_name": self.__class__.__name__,
            "filename": self.filename,
            "data": self.data,
            "format": self.format,
            "hasMipMaps": self.hasMipMaps,
            "filterMode": self.filterMode,
            "usageHint": self.usageHint,
            "textureCoordChannel": self.textureCoordChannel,
        })
