from .hkReferencedObject import hkReferencedObject
from .enums import TextureType
import struct


class hkxMaterialTextureStage(object):
    texture: any
    usageHint: TextureType
    tcoordChannel: int

    def __init__(self, infile):
        self.texture = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.usageHint = TextureType(infile)  # TYPE_ENUM:TYPE_INT32
        self.tcoordChannel = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} texture={texture}, usageHint={usageHint}, tcoordChannel={tcoordChannel}>".format(**{
            "class_name": self.__class__.__name__,
            "texture": self.texture,
            "usageHint": self.usageHint,
            "tcoordChannel": self.tcoordChannel,
        })
