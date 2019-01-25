from .hkReferencedObject import hkReferencedObject
from .common import any


class hclSimClothPose(hkReferencedObject):
    name: str
    positions: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.positions = any(infile)  # TYPE_ARRAY
