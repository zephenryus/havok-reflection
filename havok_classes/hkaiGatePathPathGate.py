import struct
from .hkaiGatePathUtilGate import hkaiGatePathUtilGate


class hkaiGatePathPathGate(object):
    crossingPoint: vector4
    gate: hkaiGatePathUtilGate
    boundarySegments: any
    cellKey: int

    def __init__(self, infile):
        self.crossingPoint = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.gate = hkaiGatePathUtilGate(infile)  # TYPE_STRUCT:TYPE_VOID
        self.boundarySegments = any(infile)  # TYPE_FLAGS:TYPE_UINT8
        self.cellKey = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} crossingPoint={crossingPoint}, gate={gate}, boundarySegments={boundarySegments}, cellKey={cellKey}>".format(**{
            "class_name": self.__class__.__name__,
            "crossingPoint": self.crossingPoint,
            "gate": self.gate,
            "boundarySegments": self.boundarySegments,
            "cellKey": self.cellKey,
        })
