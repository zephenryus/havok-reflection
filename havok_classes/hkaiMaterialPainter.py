from .hkReferencedObject import hkReferencedObject
import struct
from .hkaiVolume import hkaiVolume


class hkaiMaterialPainter(hkReferencedObject):
    material: int
    volume: any

    def __init__(self, infile):
        self.material = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.volume = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} material={material}, volume={volume}>".format(**{
            "class_name": self.__class__.__name__,
            "material": self.material,
            "volume": self.volume,
        })
