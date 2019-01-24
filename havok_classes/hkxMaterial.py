from .hkxAttributeHolder import hkxAttributeHolder
from enum import Enum
from .hkxMaterialTextureStage import hkxMaterialTextureStage
from .common import vector4
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
    stages: hkxMaterialTextureStage
    diffuseColor: vector4
    ambientColor: vector4
    specularColor: vector4
    emissiveColor: vector4
    subMaterials: hkxMaterial
    extraData: hkReferencedObject
    uvMapScale: float
    uvMapOffset: float
    uvMapRotation: float
    uvMapAlgorithm: UVMappingAlgorithm
    specularMultiplier: float
    specularExponent: float
    transparency: Transparency
    userData: int
    properties: hkxMaterialProperty
