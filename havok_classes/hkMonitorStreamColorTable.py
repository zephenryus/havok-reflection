from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkMonitorStreamColorTableColorPair import hkMonitorStreamColorTableColorPair
import struct


class hkMonitorStreamColorTable(hkReferencedObject):
    colorPairs: List[hkMonitorStreamColorTableColorPair]
    defaultColor: int

    def __init__(self, infile):
        self.colorPairs = get_array(infile, hkMonitorStreamColorTableColorPair, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.defaultColor = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} colorPairs=[{colorPairs}], defaultColor={defaultColor}>".format(**{
            "class_name": self.__class__.__name__,
            "colorPairs": self.colorPairs,
            "defaultColor": self.defaultColor,
        })
