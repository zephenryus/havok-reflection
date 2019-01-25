from .hclSetupMesh import hclSetupMesh
from .common import any
from .hclStorageSetupMeshSection import hclStorageSetupMeshSection
from .hclStorageSetupMeshVertexChannel import hclStorageSetupMeshVertexChannel
from .hclStorageSetupMeshEdgeChannel import hclStorageSetupMeshEdgeChannel
from .hclStorageSetupMeshTriangleChannel import hclStorageSetupMeshTriangleChannel
from .hclStorageSetupMeshBone import hclStorageSetupMeshBone
import struct


class hclStorageSetupMesh(hclSetupMesh):
    name: str
    worldFromMesh: any
    sections: hclStorageSetupMeshSection
    vertexChannels: hclStorageSetupMeshVertexChannel
    edgeChannels: hclStorageSetupMeshEdgeChannel
    triangleChannels: hclStorageSetupMeshTriangleChannel
    bones: hclStorageSetupMeshBone
    isSkinned: bool
    stringPool: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.worldFromMesh = any(infile)  # TYPE_MATRIX4
        self.sections = hclStorageSetupMeshSection(infile)  # TYPE_ARRAY
        self.vertexChannels = hclStorageSetupMeshVertexChannel(infile)  # TYPE_ARRAY
        self.edgeChannels = hclStorageSetupMeshEdgeChannel(infile)  # TYPE_ARRAY
        self.triangleChannels = hclStorageSetupMeshTriangleChannel(infile)  # TYPE_ARRAY
        self.bones = hclStorageSetupMeshBone(infile)  # TYPE_ARRAY
        self.isSkinned = struct.unpack('>?', infile.read(1))
        self.stringPool = any(infile)  # TYPE_POINTER
