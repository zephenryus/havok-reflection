from .hclSetupMesh import hclSetupMesh
from .hkxNode import hkxNode
from .common import any
from .hkxMesh import hkxMesh
from .hkxSkinBinding import hkxSkinBinding
from .hclSceneDataSetupMeshSection import hclSceneDataSetupMeshSection


class hclSceneDataSetupMesh(hclSetupMesh):
    node: hkxNode
    worldFromMesh: any
    mesh: hkxMesh
    skinBinding: hkxSkinBinding
    vertexChannels: any
    triangleChannels: any
    edgeChannels: any
    meshBufferInterfaces: hclSceneDataSetupMeshSection
