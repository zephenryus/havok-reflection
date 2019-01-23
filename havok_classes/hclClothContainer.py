from .hkReferencedObject import hkReferencedObject
from .hclCollidable import hclCollidable
from .hclClothData import hclClothData


class hclClothContainer(hkReferencedObject):
	collidables: hclCollidable
	clothDatas: hclClothData
