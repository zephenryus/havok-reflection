from .hkReferencedObject import hkReferencedObject


class hkxTextureFile(hkReferencedObject):
    filename: str
    name: str
    originalFilename: str

    def __init__(self, infile):
        self.filename = struct.unpack('>s', infile.read(0))
        self.name = struct.unpack('>s', infile.read(0))
        self.originalFilename = struct.unpack('>s', infile.read(0))
