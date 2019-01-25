from .hkReferencedObject import hkReferencedObject
from .common import any


class hkpRejectChassisListener(hkReferencedObject):
    chassis: any

    def __init__(self, infile):
        self.chassis = any(infile)  # TYPE_POINTER
