from .hkReferencedObject import hkReferencedObject
from .enums import TextureType
import struct


class hkxMaterialTextureStage(object):
    texture: hkReferencedObject
    usageHint: TextureType
    tcoordChannel: int

    def __init__(self, infile):
        self.texture = hkReferencedObject(infile)  # TYPE_POINTER
        self.usageHint = TextureType(infile)  # TYPE_ENUM
        self.tcoordChannel = struct.unpack('>i', infile.read(4))
