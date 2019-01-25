from .hkMeshShape import hkMeshShape
from .hkxBlob import hkxBlob


class hkxBlobMeshShape(hkMeshShape):
    blob: hkxBlob
    name: str

    def __init__(self, infile):
        self.blob = hkxBlob(infile)  # TYPE_STRUCT:TYPE_VOID
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} blob={blob}, name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "blob": self.blob,
            "name": self.name,
        })
