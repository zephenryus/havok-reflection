from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkaiAvoidancePairPropertiesPairData import hkaiAvoidancePairPropertiesPairData


class hkaiAvoidancePairProperties(hkReferencedObject):
    avoidancePairDataMap: List[hkaiAvoidancePairPropertiesPairData]

    def __init__(self, infile):
        self.avoidancePairDataMap = get_array(infile, hkaiAvoidancePairPropertiesPairData, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} avoidancePairDataMap=[{avoidancePairDataMap}]>".format(**{
            "class_name": self.__class__.__name__,
            "avoidancePairDataMap": self.avoidancePairDataMap,
        })
