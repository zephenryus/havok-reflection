from .hkReferencedObject import hkReferencedObject
from .hkxMaterialShader import hkxMaterialShader


class hkxMaterialShaderSet(hkReferencedObject):
    shaders: hkxMaterialShader

    def __init__(self, infile):
        self.shaders = hkxMaterialShader(infile)  # TYPE_ARRAY
