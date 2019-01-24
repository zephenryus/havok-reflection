from .hkReferencedObject import hkReferencedObject
from .hkxNode import hkxNode
from .hkxNodeSelectionSet import hkxNodeSelectionSet
from .hkxCamera import hkxCamera
from .hkxLight import hkxLight
from .hkxMesh import hkxMesh
from .hkxMaterial import hkxMaterial
from .hkxTextureInplace import hkxTextureInplace
from .hkxTextureFile import hkxTextureFile
from .hkxSkinBinding import hkxSkinBinding
from .hkxSpline import hkxSpline
from .common import any


class hkxScene(hkReferencedObject):
    modeller: str
    asset: str
    sceneLength: float
    numFrames: int
    rootNode: hkxNode
    selectionSets: hkxNodeSelectionSet
    cameras: hkxCamera
    lights: hkxLight
    meshes: hkxMesh
    materials: hkxMaterial
    inplaceTextures: hkxTextureInplace
    externalTextures: hkxTextureFile
    skinBindings: hkxSkinBinding
    splines: hkxSpline
    appliedTransform: any
