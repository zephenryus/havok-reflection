from .hkReferencedObject import hkReferencedObject
from .hclCollidable import hclCollidable
from .hclClothData import hclClothData


class hclClothContainer(hkReferencedObject):
    collidables: hclCollidable
    clothDatas: hclClothData

    def __init__(self, infile):
        self.collidables = hclCollidable(infile)  # TYPE_ARRAY
        self.clothDatas = hclClothData(infile)  # TYPE_ARRAY
