from .hkpConstraintChainData import hkpConstraintChainData
from .hkpBridgeAtoms import hkpBridgeAtoms
from typing import List
from .common import get_array
from .hkpBallSocketChainDataConstraintInfo import hkpBallSocketChainDataConstraintInfo
import struct


class hkpBallSocketChainData(hkpConstraintChainData):
    atoms: hkpBridgeAtoms
    infos: List[hkpBallSocketChainDataConstraintInfo]
    link0PivotBVelocity: vector4
    tau: float
    damping: float
    cfm: float
    maxErrorDistance: float
    inertiaPerMeter: float
    useStabilizedCode: bool

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT:TYPE_VOID
        self.infos = get_array(infile, hkpBallSocketChainDataConstraintInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.link0PivotBVelocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.tau = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.damping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cfm = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxErrorDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.inertiaPerMeter = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.useStabilizedCode = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}, infos=[{infos}], link0PivotBVelocity={link0PivotBVelocity}, tau={tau}, damping={damping}, cfm={cfm}, maxErrorDistance={maxErrorDistance}, inertiaPerMeter={inertiaPerMeter}, useStabilizedCode={useStabilizedCode}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
            "infos": self.infos,
            "link0PivotBVelocity": self.link0PivotBVelocity,
            "tau": self.tau,
            "damping": self.damping,
            "cfm": self.cfm,
            "maxErrorDistance": self.maxErrorDistance,
            "inertiaPerMeter": self.inertiaPerMeter,
            "useStabilizedCode": self.useStabilizedCode,
        })
