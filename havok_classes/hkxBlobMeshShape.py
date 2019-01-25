from .hkMeshShape import hkMeshShape
from .hkxBlob import hkxBlob


class hkxBlobMeshShape(hkMeshShape):
    blob: hkxBlob
    name: str

    def __init__(self, infile):
        self.blob = hkxBlob(infile)  # TYPE_STRUCT
        self.name = struct.unpack('>s', infile.read(0))
