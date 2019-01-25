import struct
from .common import any


class hkaiNavMeshCutterMeshInfo(object):
    originalNumFaces: int
    originalNumEdges: int
    originalNumVertices: int
    faceMapping: any

    def __init__(self, infile):
        self.originalNumFaces = struct.unpack('>i', infile.read(4))
        self.originalNumEdges = struct.unpack('>i', infile.read(4))
        self.originalNumVertices = struct.unpack('>i', infile.read(4))
        self.faceMapping = any(infile)  # TYPE_ARRAY
