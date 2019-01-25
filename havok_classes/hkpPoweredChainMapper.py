from .hkReferencedObject import hkReferencedObject
from .hkpPoweredChainMapperLinkInfo import hkpPoweredChainMapperLinkInfo
from .hkpPoweredChainMapperTarget import hkpPoweredChainMapperTarget
from .hkpConstraintChainInstance import hkpConstraintChainInstance


class hkpPoweredChainMapper(hkReferencedObject):
    links: hkpPoweredChainMapperLinkInfo
    targets: hkpPoweredChainMapperTarget
    chains: hkpConstraintChainInstance

    def __init__(self, infile):
        self.links = hkpPoweredChainMapperLinkInfo(infile)  # TYPE_ARRAY
        self.targets = hkpPoweredChainMapperTarget(infile)  # TYPE_ARRAY
        self.chains = hkpConstraintChainInstance(infile)  # TYPE_ARRAY
