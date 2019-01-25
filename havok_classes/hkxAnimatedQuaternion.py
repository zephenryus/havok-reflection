from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxAnimatedQuaternion(hkReferencedObject):
    quaternions: any

    def __init__(self, infile):
        self.quaternions = any(infile)  # TYPE_ARRAY
