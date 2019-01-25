from .hkpConstraintAtom import hkpConstraintAtom


class hkpSetLocalRotationsConstraintAtom(hkpConstraintAtom):
    rotationA: any
    rotationB: any

    def __init__(self, infile):
        self.rotationA = any(infile)  # TYPE_ROTATION:TYPE_VOID
        self.rotationB = any(infile)  # TYPE_ROTATION:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rotationA={rotationA}, rotationB={rotationB}>".format(**{
            "class_name": self.__class__.__name__,
            "rotationA": self.rotationA,
            "rotationB": self.rotationB,
        })
