from .hkpConstraintChainData import hkpConstraintChainData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpStiffSpringChainDataConstraintInfo import hkpStiffSpringChainDataConstraintInfo
import struct


class hkpStiffSpringChainData(hkpConstraintChainData):
    atoms: hkpBridgeAtoms
    infos: hkpStiffSpringChainDataConstraintInfo
    tau: float
    damping: float
    cfm: float

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT
        self.infos = hkpStiffSpringChainDataConstraintInfo(infile)  # TYPE_ARRAY
        self.tau = struct.unpack('>f', infile.read(4))
        self.damping = struct.unpack('>f', infile.read(4))
        self.cfm = struct.unpack('>f', infile.read(4))
