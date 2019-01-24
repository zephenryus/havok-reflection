from .hkReferencedObject import hkReferencedObject
from .hkpPoweredChainMapperLinkInfo import hkpPoweredChainMapperLinkInfo
from .hkpPoweredChainMapperTarget import hkpPoweredChainMapperTarget
from .hkpConstraintChainInstance import hkpConstraintChainInstance


class hkpPoweredChainMapper(hkReferencedObject):
    links: hkpPoweredChainMapperLinkInfo
    targets: hkpPoweredChainMapperTarget
    chains: hkpConstraintChainInstance
