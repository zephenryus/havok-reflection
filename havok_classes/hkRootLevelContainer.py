from typing import List
from .common import get_array
from .hkRootLevelContainerNamedVariant import hkRootLevelContainerNamedVariant


class hkRootLevelContainer(object):
    namedVariants: List[hkRootLevelContainerNamedVariant]

    def __init__(self, infile):
        self.namedVariants = get_array(infile, hkRootLevelContainerNamedVariant, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} namedVariants=[{namedVariants}]>".format(**{
            "class_name": self.__class__.__name__,
            "namedVariants": self.namedVariants,
        })
