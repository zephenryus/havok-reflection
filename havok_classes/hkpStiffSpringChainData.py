from .hkpConstraintChainData import hkpConstraintChainData
from .hkpBridgeAtoms import hkpBridgeAtoms
from typing import List
from .common import get_array
from .hkpStiffSpringChainDataConstraintInfo import hkpStiffSpringChainDataConstraintInfo
import struct


class hkpStiffSpringChainData(hkpConstraintChainData):
    atoms: hkpBridgeAtoms
    infos: List[hkpStiffSpringChainDataConstraintInfo]
    tau: float
    damping: float
    cfm: float

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT:TYPE_VOID
        self.infos = get_array(infile, hkpStiffSpringChainDataConstraintInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.tau = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.damping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cfm = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}, infos=[{infos}], tau={tau}, damping={damping}, cfm={cfm}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
            "infos": self.infos,
            "tau": self.tau,
            "damping": self.damping,
            "cfm": self.cfm,
        })
