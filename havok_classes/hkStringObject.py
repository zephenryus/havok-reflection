from .hkReferencedObject import hkReferencedObject


class hkStringObject(hkReferencedObject):
    string: str

    def __init__(self, infile):
        self.string = struct.unpack('>s', infile.read(0))
