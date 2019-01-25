from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkxAttributeGroup import hkxAttributeGroup


class hkxAttributeHolder(hkReferencedObject):
    attributeGroups: List[hkxAttributeGroup]

    def __init__(self, infile):
        self.attributeGroups = get_array(infile, hkxAttributeGroup, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} attributeGroups=[{attributeGroups}]>".format(**{
            "class_name": self.__class__.__name__,
            "attributeGroups": self.attributeGroups,
        })
