from .hkReferencedObject import hkReferencedObject
from .hkxVertexBuffer import hkxVertexBuffer
from typing import List
from .common import get_array
from .hkxIndexBuffer import hkxIndexBuffer
from .hkxMaterial import hkxMaterial
from .hkxVertexAnimation import hkxVertexAnimation
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping


class hkxMeshSection(hkReferencedObject):
    vertexBuffer: any
    indexBuffers: List[hkxIndexBuffer]
    material: any
    userChannels: List[hkReferencedObject]
    vertexAnimations: List[hkxVertexAnimation]
    linearKeyFrameHints: List[float]
    boneMatrixMap: List[hkMeshBoneIndexMapping]

    def __init__(self, infile):
        self.vertexBuffer = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.indexBuffers = get_array(infile, hkxIndexBuffer, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.material = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.userChannels = get_array(infile, hkReferencedObject, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.vertexAnimations = get_array(infile, hkxVertexAnimation, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.linearKeyFrameHints = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.boneMatrixMap = get_array(infile, hkMeshBoneIndexMapping, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} vertexBuffer={vertexBuffer}, indexBuffers=[{indexBuffers}], material={material}, userChannels=[{userChannels}], vertexAnimations=[{vertexAnimations}], linearKeyFrameHints=[{linearKeyFrameHints}], boneMatrixMap=[{boneMatrixMap}]>".format(**{
            "class_name": self.__class__.__name__,
            "vertexBuffer": self.vertexBuffer,
            "indexBuffers": self.indexBuffers,
            "material": self.material,
            "userChannels": self.userChannels,
            "vertexAnimations": self.vertexAnimations,
            "linearKeyFrameHints": self.linearKeyFrameHints,
            "boneMatrixMap": self.boneMatrixMap,
        })
