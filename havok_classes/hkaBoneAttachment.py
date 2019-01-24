from .hkReferencedObject import hkReferencedObject
from .common import any


class hkaBoneAttachment(hkReferencedObject):
    originalSkeletonName: str
    boneFromAttachment: any
    attachment: hkReferencedObject
    name: str
    boneIndex: int
