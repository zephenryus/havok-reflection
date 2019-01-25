from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hclCollidable import hclCollidable
from .hclClothData import hclClothData


class hclClothContainer(hkReferencedObject):
    collidables: List[hclCollidable]
    clothDatas: List[hclClothData]

    def __init__(self, infile):
        self.collidables = get_array(infile, hclCollidable, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.clothDatas = get_array(infile, hclClothData, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} collidables=[{collidables}], clothDatas=[{clothDatas}]>".format(**{
            "class_name": self.__class__.__name__,
            "collidables": self.collidables,
            "clothDatas": self.clothDatas,
        })
