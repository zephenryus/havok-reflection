from .hkReferencedObject import hkReferencedObject
from .hkxVertexBuffer import hkxVertexBuffer
from .hkxIndexBuffer import hkxIndexBuffer
from .hkxMaterial import hkxMaterial
from .hkxVertexAnimation import hkxVertexAnimation
from .common import any
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping


class hkxMeshSection(hkReferencedObject):
    vertexBuffer: hkxVertexBuffer
    indexBuffers: hkxIndexBuffer
    material: hkxMaterial
    userChannels: hkReferencedObject
    vertexAnimations: hkxVertexAnimation
    linearKeyFrameHints: any
    boneMatrixMap: hkMeshBoneIndexMapping
