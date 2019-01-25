from .hkpConstraintData import hkpConstraintData


class hkpWrappedConstraintData(hkpConstraintData):
    constraintData: hkpConstraintData

    def __init__(self, infile):
        self.constraintData = hkpConstraintData(infile)  # TYPE_POINTER
