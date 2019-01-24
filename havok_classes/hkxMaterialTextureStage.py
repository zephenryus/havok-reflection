from .hkReferencedObject import hkReferencedObject
from .enums import TextureType


class hkxMaterialTextureStage(object):
    texture: hkReferencedObject
    usageHint: TextureType
    tcoordChannel: int
