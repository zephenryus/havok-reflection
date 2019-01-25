from .hkReferencedObject import hkReferencedObject
from .common import any
import struct


class hkpAction(hkReferencedObject):
    world: any
    island: any
    userData: int
    name: str

    def __init__(self, infile):
        self.world = any(infile)  # TYPE_POINTER
        self.island = any(infile)  # TYPE_POINTER
        self.userData = struct.unpack('>L', infile.read(8))
        self.name = struct.unpack('>s', infile.read(0))
