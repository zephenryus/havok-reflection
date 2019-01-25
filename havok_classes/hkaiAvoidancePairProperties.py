from .hkReferencedObject import hkReferencedObject
from .hkaiAvoidancePairPropertiesPairData import hkaiAvoidancePairPropertiesPairData


class hkaiAvoidancePairProperties(hkReferencedObject):
    avoidancePairDataMap: hkaiAvoidancePairPropertiesPairData

    def __init__(self, infile):
        self.avoidancePairDataMap = hkaiAvoidancePairPropertiesPairData(infile)  # TYPE_ARRAY
