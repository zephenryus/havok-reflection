from .hkpConstraintChainData import hkpConstraintChainData
from .hkpBridgeAtoms import hkpBridgeAtoms
from typing import List
from .common import get_array
from .hkpPoweredChainDataConstraintInfo import hkpPoweredChainDataConstraintInfo
import struct


class hkpPoweredChainData(hkpConstraintChainData):
    atoms: hkpBridgeAtoms
    infos: List[hkpPoweredChainDataConstraintInfo]
    tau: float
    damping: float
    cfmLinAdd: float
    cfmLinMul: float
    cfmAngAdd: float
    cfmAngMul: float
    maxErrorDistance: float

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT:TYPE_VOID
        self.infos = get_array(infile, hkpPoweredChainDataConstraintInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.tau = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.damping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cfmLinAdd = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cfmLinMul = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cfmAngAdd = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cfmAngMul = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxErrorDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}, infos=[{infos}], tau={tau}, damping={damping}, cfmLinAdd={cfmLinAdd}, cfmLinMul={cfmLinMul}, cfmAngAdd={cfmAngAdd}, cfmAngMul={cfmAngMul}, maxErrorDistance={maxErrorDistance}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
            "infos": self.infos,
            "tau": self.tau,
            "damping": self.damping,
            "cfmLinAdd": self.cfmLinAdd,
            "cfmLinMul": self.cfmLinMul,
            "cfmAngAdd": self.cfmAngAdd,
            "cfmAngMul": self.cfmAngMul,
            "maxErrorDistance": self.maxErrorDistance,
        })
