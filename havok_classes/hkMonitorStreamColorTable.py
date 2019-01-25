from .hkReferencedObject import hkReferencedObject
from .hkMonitorStreamColorTableColorPair import hkMonitorStreamColorTableColorPair
import struct


class hkMonitorStreamColorTable(hkReferencedObject):
    colorPairs: hkMonitorStreamColorTableColorPair
    defaultColor: int

    def __init__(self, infile):
        self.colorPairs = hkMonitorStreamColorTableColorPair(infile)  # TYPE_ARRAY
        self.defaultColor = struct.unpack('>I', infile.read(4))
