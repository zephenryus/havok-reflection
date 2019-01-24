from .hclSetupMesh import hclSetupMesh
from .common import any
from .hclStorageSetupMeshSection import hclStorageSetupMeshSection
from .hclStorageSetupMeshVertexChannel import hclStorageSetupMeshVertexChannel
from .hclStorageSetupMeshEdgeChannel import hclStorageSetupMeshEdgeChannel
from .hclStorageSetupMeshTriangleChannel import hclStorageSetupMeshTriangleChannel
from .hclStorageSetupMeshBone import hclStorageSetupMeshBone


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
