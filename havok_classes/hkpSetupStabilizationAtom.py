from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpSetupStabilizationAtom(hkpConstraintAtom):
    enabled: bool
    padding: int
    maxLinImpulse: float
    maxAngImpulse: float
    maxAngle: float

    def __init__(self, infile):
        self.enabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.maxLinImpulse = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxAngImpulse = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} enabled={enabled}, padding={padding}, maxLinImpulse={maxLinImpulse}, maxAngImpulse={maxAngImpulse}, maxAngle={maxAngle}>".format(**{
            "class_name": self.__class__.__name__,
            "enabled": self.enabled,
            "padding": self.padding,
            "maxLinImpulse": self.maxLinImpulse,
            "maxAngImpulse": self.maxAngImpulse,
            "maxAngle": self.maxAngle,
        })
