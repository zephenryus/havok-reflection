from .hkpBinaryAction import hkpBinaryAction
from .common import any
import struct


class hkpAngularDashpotAction(hkpBinaryAction):
    rotation: any
    strength: float
    damping: float

    def __init__(self, infile):
        self.rotation = any(infile)  # TYPE_QUATERNION
        self.strength = struct.unpack('>f', infile.read(4))
        self.damping = struct.unpack('>f', infile.read(4))
