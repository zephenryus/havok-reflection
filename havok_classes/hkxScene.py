from .hkReferencedObject import hkReferencedObject
import struct
from .hkxNode import hkxNode
from typing import List
from .common import get_array
from .hkxNodeSelectionSet import hkxNodeSelectionSet
from .hkxCamera import hkxCamera
from .hkxLight import hkxLight
from .hkxMesh import hkxMesh
from .hkxMaterial import hkxMaterial
from .hkxTextureInplace import hkxTextureInplace
from .hkxTextureFile import hkxTextureFile
from .hkxSkinBinding import hkxSkinBinding
from .hkxSpline import hkxSpline


class hkxScene(hkReferencedObject):
    modeller: str
    asset: str
    sceneLength: float
    numFrames: int
    rootNode: any
    selectionSets: List[hkxNodeSelectionSet]
    cameras: List[hkxCamera]
    lights: List[hkxLight]
    meshes: List[hkxMesh]
    materials: List[hkxMaterial]
    inplaceTextures: List[hkxTextureInplace]
    externalTextures: List[hkxTextureFile]
    skinBindings: List[hkxSkinBinding]
    splines: List[hkxSpline]
    appliedTransform: any

    def __init__(self, infile):
        self.modeller = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.asset = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.sceneLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numFrames = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.rootNode = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.selectionSets = get_array(infile, hkxNodeSelectionSet, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.cameras = get_array(infile, hkxCamera, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.lights = get_array(infile, hkxLight, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.meshes = get_array(infile, hkxMesh, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.materials = get_array(infile, hkxMaterial, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.inplaceTextures = get_array(infile, hkxTextureInplace, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.externalTextures = get_array(infile, hkxTextureFile, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.skinBindings = get_array(infile, hkxSkinBinding, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.splines = get_array(infile, hkxSpline, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.appliedTransform = any(infile)  # TYPE_MATRIX3:TYPE_VOID

    def __repr__(self):
        return "<{class_name} modeller=\"{modeller}\", asset=\"{asset}\", sceneLength={sceneLength}, numFrames={numFrames}, rootNode={rootNode}, selectionSets=[{selectionSets}], cameras=[{cameras}], lights=[{lights}], meshes=[{meshes}], materials=[{materials}], inplaceTextures=[{inplaceTextures}], externalTextures=[{externalTextures}], skinBindings=[{skinBindings}], splines=[{splines}], appliedTransform={appliedTransform}>".format(**{
            "class_name": self.__class__.__name__,
            "modeller": self.modeller,
            "asset": self.asset,
            "sceneLength": self.sceneLength,
            "numFrames": self.numFrames,
            "rootNode": self.rootNode,
            "selectionSets": self.selectionSets,
            "cameras": self.cameras,
            "lights": self.lights,
            "meshes": self.meshes,
            "materials": self.materials,
            "inplaceTextures": self.inplaceTextures,
            "externalTextures": self.externalTextures,
            "skinBindings": self.skinBindings,
            "splines": self.splines,
            "appliedTransform": self.appliedTransform,
        })
