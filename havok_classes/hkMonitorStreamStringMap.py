from typing import List
from .common import get_array
from .hkMonitorStreamStringMapStringMap import hkMonitorStreamStringMapStringMap


class hkMonitorStreamStringMap(object):
    map: List[hkMonitorStreamStringMapStringMap]

    def __init__(self, infile):
        self.map = get_array(infile, hkMonitorStreamStringMapStringMap, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} map=[{map}]>".format(**{
            "class_name": self.__class__.__name__,
            "map": self.map,
        })
