from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpSetupStabilizationAtom(hkpConstraintAtom):
    enabled: bool
    padding: int
    maxLinImpulse: float
    maxAngImpulse: float
    maxAngle: float

    def __init__(self, infile):
        self.enabled = struct.unpack('>?', infile.read(1))
        self.padding = struct.unpack('>B', infile.read(1))
        self.maxLinImpulse = struct.unpack('>f', infile.read(4))
        self.maxAngImpulse = struct.unpack('>f', infile.read(4))
        self.maxAngle = struct.unpack('>f', infile.read(4))
