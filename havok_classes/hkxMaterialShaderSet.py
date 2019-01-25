from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkxMaterialShader import hkxMaterialShader


class hkxMaterialShaderSet(hkReferencedObject):
    shaders: List[hkxMaterialShader]

    def __init__(self, infile):
        self.shaders = get_array(infile, hkxMaterialShader, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} shaders=[{shaders}]>".format(**{
            "class_name": self.__class__.__name__,
            "shaders": self.shaders,
        })
