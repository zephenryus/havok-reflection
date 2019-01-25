from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkpRemoveTerminalsMoppModifier(hkReferencedObject):
    removeInfo: List[int]
    tempShapesToRemove: any

    def __init__(self, infile):
        self.removeInfo = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.tempShapesToRemove = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} removeInfo=[{removeInfo}], tempShapesToRemove={tempShapesToRemove}>".format(**{
            "class_name": self.__class__.__name__,
            "removeInfo": self.removeInfo,
            "tempShapesToRemove": self.tempShapesToRemove,
        })
