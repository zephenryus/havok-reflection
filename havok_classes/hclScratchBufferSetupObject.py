from .hclBufferSetupObject import hclBufferSetupObject
from .hclSetupMesh import hclSetupMesh
import struct


class hclScratchBufferSetupObject(hclBufferSetupObject):
    name: str
    setupMesh: any
    storeNormals: bool
    storeTangentsAndBiTangents: bool
    storeTriangles: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.setupMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.storeNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.storeTangentsAndBiTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.storeTriangles = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", setupMesh={setupMesh}, storeNormals={storeNormals}, storeTangentsAndBiTangents={storeTangentsAndBiTangents}, storeTriangles={storeTriangles}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "setupMesh": self.setupMesh,
            "storeNormals": self.storeNormals,
            "storeTangentsAndBiTangents": self.storeTangentsAndBiTangents,
            "storeTriangles": self.storeTriangles,
        })
