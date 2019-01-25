from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpAngFrictionConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    firstFrictionAxis: int
    numFrictionAxes: int
    maxFrictionTorque: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.firstFrictionAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.numFrictionAxes = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.maxFrictionTorque = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} isEnabled={isEnabled}, firstFrictionAxis={firstFrictionAxis}, numFrictionAxes={numFrictionAxes}, maxFrictionTorque={maxFrictionTorque}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "isEnabled": self.isEnabled,
            "firstFrictionAxis": self.firstFrictionAxis,
            "numFrictionAxes": self.numFrictionAxes,
            "maxFrictionTorque": self.maxFrictionTorque,
            "padding": self.padding,
        })
