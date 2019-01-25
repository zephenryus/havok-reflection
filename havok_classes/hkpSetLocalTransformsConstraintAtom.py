from .hkpConstraintAtom import hkpConstraintAtom


class hkpSetLocalTransformsConstraintAtom(hkpConstraintAtom):
    transformA: any
    transformB: any

    def __init__(self, infile):
        self.transformA = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.transformB = any(infile)  # TYPE_TRANSFORM:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transformA={transformA}, transformB={transformB}>".format(**{
            "class_name": self.__class__.__name__,
            "transformA": self.transformA,
            "transformB": self.transformB,
        })
