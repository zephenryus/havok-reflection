from .hkReferencedObject import hkReferencedObject
import struct
from .hkaiVolume import hkaiVolume


class hkaiMaterialPainter(hkReferencedObject):
    material: int
    volume: hkaiVolume

    def __init__(self, infile):
        self.material = struct.unpack('>i', infile.read(4))
        self.volume = hkaiVolume(infile)  # TYPE_POINTER
