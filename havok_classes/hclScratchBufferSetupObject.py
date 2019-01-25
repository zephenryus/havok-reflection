from .hclBufferSetupObject import hclBufferSetupObject
from .hclSetupMesh import hclSetupMesh
import struct


class hclScratchBufferSetupObject(hclBufferSetupObject):
    name: str
    setupMesh: hclSetupMesh
    storeNormals: bool
    storeTangentsAndBiTangents: bool
    storeTriangles: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.setupMesh = hclSetupMesh(infile)  # TYPE_POINTER
        self.storeNormals = struct.unpack('>?', infile.read(1))
        self.storeTangentsAndBiTangents = struct.unpack('>?', infile.read(1))
        self.storeTriangles = struct.unpack('>?', infile.read(1))
