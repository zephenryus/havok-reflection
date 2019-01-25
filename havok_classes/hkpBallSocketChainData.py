from .hkpConstraintChainData import hkpConstraintChainData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpBallSocketChainDataConstraintInfo import hkpBallSocketChainDataConstraintInfo
from .common import vector4
import struct


class hkpBallSocketChainData(hkpConstraintChainData):
    atoms: hkpBridgeAtoms
    infos: hkpBallSocketChainDataConstraintInfo
    link0PivotBVelocity: vector4
    tau: float
    damping: float
    cfm: float
    maxErrorDistance: float
    inertiaPerMeter: float
    useStabilizedCode: bool

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT
        self.infos = hkpBallSocketChainDataConstraintInfo(infile)  # TYPE_ARRAY
        self.link0PivotBVelocity = struct.unpack('>4f', infile.read(16))
        self.tau = struct.unpack('>f', infile.read(4))
        self.damping = struct.unpack('>f', infile.read(4))
        self.cfm = struct.unpack('>f', infile.read(4))
        self.maxErrorDistance = struct.unpack('>f', infile.read(4))
        self.inertiaPerMeter = struct.unpack('>f', infile.read(4))
        self.useStabilizedCode = struct.unpack('>?', infile.read(1))
