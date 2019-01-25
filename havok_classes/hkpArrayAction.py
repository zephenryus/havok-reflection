from .hkpAction import hkpAction
from typing import List
from .common import get_array
from .hkpEntity import hkpEntity


class hkpArrayAction(hkpAction):
    entities: List[hkpEntity]

    def __init__(self, infile):
        self.entities = get_array(infile, hkpEntity, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} entities=[{entities}]>".format(**{
            "class_name": self.__class__.__name__,
            "entities": self.entities,
        })
