from .hkReferencedObject import hkReferencedObject
import struct
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

    def __init__(self, infile):
        self.modeller = struct.unpack('>s', infile.read(0))
        self.asset = struct.unpack('>s', infile.read(0))
        self.sceneLength = struct.unpack('>f', infile.read(4))
        self.numFrames = struct.unpack('>I', infile.read(4))
        self.rootNode = hkxNode(infile)  # TYPE_POINTER
        self.selectionSets = hkxNodeSelectionSet(infile)  # TYPE_ARRAY
        self.cameras = hkxCamera(infile)  # TYPE_ARRAY
        self.lights = hkxLight(infile)  # TYPE_ARRAY
        self.meshes = hkxMesh(infile)  # TYPE_ARRAY
        self.materials = hkxMaterial(infile)  # TYPE_ARRAY
        self.inplaceTextures = hkxTextureInplace(infile)  # TYPE_ARRAY
        self.externalTextures = hkxTextureFile(infile)  # TYPE_ARRAY
        self.skinBindings = hkxSkinBinding(infile)  # TYPE_ARRAY
        self.splines = hkxSpline(infile)  # TYPE_ARRAY
        self.appliedTransform = any(infile)  # TYPE_MATRIX3
