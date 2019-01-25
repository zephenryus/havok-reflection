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

    def __init__(self, infile):
        self.vertexBuffer = hkxVertexBuffer(infile)  # TYPE_POINTER
        self.indexBuffers = hkxIndexBuffer(infile)  # TYPE_ARRAY
        self.material = hkxMaterial(infile)  # TYPE_POINTER
        self.userChannels = hkReferencedObject(infile)  # TYPE_ARRAY
        self.vertexAnimations = hkxVertexAnimation(infile)  # TYPE_ARRAY
        self.linearKeyFrameHints = any(infile)  # TYPE_ARRAY
        self.boneMatrixMap = hkMeshBoneIndexMapping(infile)  # TYPE_ARRAY
