import struct
from typing import List
from .common import get_array


class hkaiNavMeshCutterMeshInfo(object):
    originalNumFaces: int
    originalNumEdges: int
    originalNumVertices: int
    faceMapping: List[int]

    def __init__(self, infile):
        self.originalNumFaces = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.originalNumEdges = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.originalNumVertices = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.faceMapping = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32

    def __repr__(self):
        return "<{class_name} originalNumFaces={originalNumFaces}, originalNumEdges={originalNumEdges}, originalNumVertices={originalNumVertices}, faceMapping=[{faceMapping}]>".format(**{
            "class_name": self.__class__.__name__,
            "originalNumFaces": self.originalNumFaces,
            "originalNumEdges": self.originalNumEdges,
            "originalNumVertices": self.originalNumVertices,
            "faceMapping": self.faceMapping,
        })
