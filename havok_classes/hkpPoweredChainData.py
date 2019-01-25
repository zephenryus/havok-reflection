from .hkpConstraintChainData import hkpConstraintChainData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpPoweredChainDataConstraintInfo import hkpPoweredChainDataConstraintInfo
import struct


class hkpPoweredChainData(hkpConstraintChainData):
    atoms: hkpBridgeAtoms
    infos: hkpPoweredChainDataConstraintInfo
    tau: float
    damping: float
    cfmLinAdd: float
    cfmLinMul: float
    cfmAngAdd: float
    cfmAngMul: float
    maxErrorDistance: float

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT
        self.infos = hkpPoweredChainDataConstraintInfo(infile)  # TYPE_ARRAY
        self.tau = struct.unpack('>f', infile.read(4))
        self.damping = struct.unpack('>f', infile.read(4))
        self.cfmLinAdd = struct.unpack('>f', infile.read(4))
        self.cfmLinMul = struct.unpack('>f', infile.read(4))
        self.cfmAngAdd = struct.unpack('>f', infile.read(4))
        self.cfmAngMul = struct.unpack('>f', infile.read(4))
        self.maxErrorDistance = struct.unpack('>f', infile.read(4))
