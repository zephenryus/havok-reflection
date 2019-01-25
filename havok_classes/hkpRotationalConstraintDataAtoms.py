from .hkpSetLocalRotationsConstraintAtom import hkpSetLocalRotationsConstraintAtom
from .hkpAngConstraintAtom import hkpAngConstraintAtom


class hkpRotationalConstraintDataAtoms(object):
    rotations: hkpSetLocalRotationsConstraintAtom
    ang: hkpAngConstraintAtom

    def __init__(self, infile):
        self.rotations = hkpSetLocalRotationsConstraintAtom(infile)  # TYPE_STRUCT
        self.ang = hkpAngConstraintAtom(infile)  # TYPE_STRUCT
