from .hkaiAstarCostModifier import hkaiAstarCostModifier
import struct


class hkaiDefaultAstarCostModifier(hkaiAstarCostModifier):
    maxCostPenalty: float
    costMultiplierLookupTable: int

    def __init__(self, infile):
        self.maxCostPenalty = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.costMultiplierLookupTable = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID

    def __repr__(self):
        return "<{class_name} maxCostPenalty={maxCostPenalty}, costMultiplierLookupTable={costMultiplierLookupTable}>".format(**{
            "class_name": self.__class__.__name__,
            "maxCostPenalty": self.maxCostPenalty,
            "costMultiplierLookupTable": self.costMultiplierLookupTable,
        })
