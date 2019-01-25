from .hkReferencedObject import hkReferencedObject


class hkLocalFrameGroup(hkReferencedObject):
    name: str

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
