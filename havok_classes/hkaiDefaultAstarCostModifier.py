from .hkaiAstarCostModifier import hkaiAstarCostModifier
import struct


class hkaiDefaultAstarCostModifier(hkaiAstarCostModifier):
    maxCostPenalty: float
    costMultiplierLookupTable: int

    def __init__(self, infile):
        self.maxCostPenalty = struct.unpack('>f', infile.read(4))
        self.costMultiplierLookupTable = struct.unpack('>h', infile.read(2))
