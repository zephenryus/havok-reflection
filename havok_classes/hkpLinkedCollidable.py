from .hkpCollidable import hkpCollidable
from typing import List
from .common import get_array


class hkpLinkedCollidable(hkpCollidable):
    collisionEntries: List[any]

    def __init__(self, infile):
        self.collisionEntries = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_VOID

    def __repr__(self):
        return "<{class_name} collisionEntries=[{collisionEntries}]>".format(**{
            "class_name": self.__class__.__name__,
            "collisionEntries": self.collisionEntries,
        })
