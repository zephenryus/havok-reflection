from .hkxAttributeHolder import hkxAttributeHolder
from enum import Enum
from typing import List
from .common import get_array
from .hkxMaterialTextureStage import hkxMaterialTextureStage
import struct
from .hkxMaterial import hkxMaterial
from .hkReferencedObject import hkReferencedObject
from .enums import UVMappingAlgorithm, Transparency
from .hkxMaterialProperty import hkxMaterialProperty


class TextureType(Enum):
    TEX_UNKNOWN = 0
    TEX_DIFFUSE = 1
    TEX_REFLECTION = 2
    TEX_BUMP = 3
    TEX_NORMAL = 4
    TEX_DISPLACEMENT = 5
    TEX_SPECULAR = 6
    TEX_SPECULARANDGLOSS = 7
    TEX_OPACITY = 8
    TEX_EMISSIVE = 9
    TEX_REFRACTION = 10
    TEX_GLOSS = 11
    TEX_DOMINANTS = 12
    TEX_NOTEXPORTED = 13


class PropertyKey(Enum):
    PROPERTY_MTL_TYPE_BLEND = 1
    PROPERTY_MTL_UV_ID_STAGE0 = 256
    PROPERTY_MTL_UV_ID_STAGE1 = 257
    PROPERTY_MTL_UV_ID_STAGE2 = 258
    PROPERTY_MTL_UV_ID_STAGE3 = 259
    PROPERTY_MTL_UV_ID_STAGE4 = 260
    PROPERTY_MTL_UV_ID_STAGE5 = 261
    PROPERTY_MTL_UV_ID_STAGE6 = 262
    PROPERTY_MTL_UV_ID_STAGE7 = 263
    PROPERTY_MTL_UV_ID_STAGE8 = 264
    PROPERTY_MTL_UV_ID_STAGE9 = 265
    PROPERTY_MTL_UV_ID_STAGE10 = 266
    PROPERTY_MTL_UV_ID_STAGE11 = 267
    PROPERTY_MTL_UV_ID_STAGE12 = 268
    PROPERTY_MTL_UV_ID_STAGE13 = 269
    PROPERTY_MTL_UV_ID_STAGE14 = 270
    PROPERTY_MTL_UV_ID_STAGE15 = 271
    PROPERTY_MTL_UV_ID_STAGE_MAX = 272


class UVMappingAlgorithm(Enum):
    UVMA_SRT = 0
    UVMA_TRS = 1
    UVMA_3DSMAX_STYLE = 2
    UVMA_MAYA_STYLE = 3


class Transparency(Enum):
    transp_none = 0
    transp_alpha = 2
    transp_additive = 3
    transp_colorkey = 4
    transp_subtractive = 9


class hkxMaterial(hkxAttributeHolder):
    name: str
    stages: List[hkxMaterialTextureStage]
    diffuseColor: vector4
    ambientColor: vector4
    specularColor: vector4
    emissiveColor: vector4
    subMaterials: List[hkxMaterial]
    extraData: any
    uvMapScale: float
    uvMapOffset: float
    uvMapRotation: float
    uvMapAlgorithm: UVMappingAlgorithm
    specularMultiplier: float
    specularExponent: float
    transparency: Transparency
    userData: int
    properties: List[hkxMaterialProperty]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.stages = get_array(infile, hkxMaterialTextureStage, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.diffuseColor = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.ambientColor = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.specularColor = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.emissiveColor = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.subMaterials = get_array(infile, hkxMaterial, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.extraData = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.uvMapScale = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.uvMapOffset = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.uvMapRotation = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.uvMapAlgorithm = UVMappingAlgorithm(infile)  # TYPE_ENUM:TYPE_UINT32
        self.specularMultiplier = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.specularExponent = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.transparency = Transparency(infile)  # TYPE_ENUM:TYPE_UINT8
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.properties = get_array(infile, hkxMaterialProperty, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} name=\"{name}\", stages=[{stages}], diffuseColor={diffuseColor}, ambientColor={ambientColor}, specularColor={specularColor}, emissiveColor={emissiveColor}, subMaterials=[{subMaterials}], extraData={extraData}, uvMapScale={uvMapScale}, uvMapOffset={uvMapOffset}, uvMapRotation={uvMapRotation}, uvMapAlgorithm={uvMapAlgorithm}, specularMultiplier={specularMultiplier}, specularExponent={specularExponent}, transparency={transparency}, userData={userData}, properties=[{properties}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "stages": self.stages,
            "diffuseColor": self.diffuseColor,
            "ambientColor": self.ambientColor,
            "specularColor": self.specularColor,
            "emissiveColor": self.emissiveColor,
            "subMaterials": self.subMaterials,
            "extraData": self.extraData,
            "uvMapScale": self.uvMapScale,
            "uvMapOffset": self.uvMapOffset,
            "uvMapRotation": self.uvMapRotation,
            "uvMapAlgorithm": self.uvMapAlgorithm,
            "specularMultiplier": self.specularMultiplier,
            "specularExponent": self.specularExponent,
            "transparency": self.transparency,
            "userData": self.userData,
            "properties": self.properties,
        })
