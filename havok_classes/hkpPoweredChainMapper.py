from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpPoweredChainMapperLinkInfo import hkpPoweredChainMapperLinkInfo
from .hkpPoweredChainMapperTarget import hkpPoweredChainMapperTarget
from .hkpConstraintChainInstance import hkpConstraintChainInstance


class hkpPoweredChainMapper(hkReferencedObject):
    links: List[hkpPoweredChainMapperLinkInfo]
    targets: List[hkpPoweredChainMapperTarget]
    chains: List[hkpConstraintChainInstance]

    def __init__(self, infile):
        self.links = get_array(infile, hkpPoweredChainMapperLinkInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.targets = get_array(infile, hkpPoweredChainMapperTarget, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.chains = get_array(infile, hkpConstraintChainInstance, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} links=[{links}], targets=[{targets}], chains=[{chains}]>".format(**{
            "class_name": self.__class__.__name__,
            "links": self.links,
            "targets": self.targets,
            "chains": self.chains,
        })
