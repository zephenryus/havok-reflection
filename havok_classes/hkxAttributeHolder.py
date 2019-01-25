from .hkReferencedObject import hkReferencedObject
from .hkxAttributeGroup import hkxAttributeGroup


class hkxAttributeHolder(hkReferencedObject):
    attributeGroups: hkxAttributeGroup

    def __init__(self, infile):
        self.attributeGroups = hkxAttributeGroup(infile)  # TYPE_ARRAY
