from .hkpConstraintData import hkpConstraintData


class hkpWrappedConstraintData(hkpConstraintData):
    constraintData: any

    def __init__(self, infile):
        self.constraintData = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} constraintData={constraintData}>".format(**{
            "class_name": self.__class__.__name__,
            "constraintData": self.constraintData,
        })
