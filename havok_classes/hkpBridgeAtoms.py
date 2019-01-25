from .hkpBridgeConstraintAtom import hkpBridgeConstraintAtom


class hkpBridgeAtoms(object):
    bridgeAtom: hkpBridgeConstraintAtom

    def __init__(self, infile):
        self.bridgeAtom = hkpBridgeConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} bridgeAtom={bridgeAtom}>".format(**{
            "class_name": self.__class__.__name__,
            "bridgeAtom": self.bridgeAtom,
        })
