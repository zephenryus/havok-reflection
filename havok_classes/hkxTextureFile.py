from .hkReferencedObject import hkReferencedObject


class hkxTextureFile(hkReferencedObject):
    filename: str
    name: str
    originalFilename: str

    def __init__(self, infile):
        self.filename = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.originalFilename = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} filename=\"{filename}\", name=\"{name}\", originalFilename=\"{originalFilename}\">".format(**{
            "class_name": self.__class__.__name__,
            "filename": self.filename,
            "name": self.name,
            "originalFilename": self.originalFilename,
        })
