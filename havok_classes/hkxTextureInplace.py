from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxTextureInplace(hkReferencedObject):
    fileType: str
    data: any
    name: str
    originalFilename: str
