from .hkReferencedObject import hkReferencedObject
from .hkxMesh import hkxMesh
from typing import List
from .common import get_array


class hkxSkinBinding(hkReferencedObject):
    mesh: any
    nodeNames: List[str]
    bindPose: List[any]
    initSkinTransform: any

    def __init__(self, infile):
        self.mesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.nodeNames = get_array(infile, str, 0)  # TYPE_ARRAY:TYPE_STRINGPTR
        self.bindPose = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4
        self.initSkinTransform = any(infile)  # TYPE_MATRIX4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} mesh={mesh}, nodeNames=[{nodeNames}], bindPose=[{bindPose}], initSkinTransform={initSkinTransform}>".format(**{
            "class_name": self.__class__.__name__,
            "mesh": self.mesh,
            "nodeNames": self.nodeNames,
            "bindPose": self.bindPose,
            "initSkinTransform": self.initSkinTransform,
        })
