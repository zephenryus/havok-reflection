from .hkpSetLocalRotationsConstraintAtom import hkpSetLocalRotationsConstraintAtom
from .hkpAngConstraintAtom import hkpAngConstraintAtom


class hkpRotationalConstraintDataAtoms(object):
    rotations: hkpSetLocalRotationsConstraintAtom
    ang: hkpAngConstraintAtom

    def __init__(self, infile):
        self.rotations = hkpSetLocalRotationsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ang = hkpAngConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rotations={rotations}, ang={ang}>".format(**{
            "class_name": self.__class__.__name__,
            "rotations": self.rotations,
            "ang": self.ang,
        })
