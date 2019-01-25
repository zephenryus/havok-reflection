from .hkpBridgeConstraintAtom import hkpBridgeConstraintAtom


class hkpBridgeAtoms(object):
    bridgeAtom: hkpBridgeConstraintAtom

    def __init__(self, infile):
        self.bridgeAtom = hkpBridgeConstraintAtom(infile)  # TYPE_STRUCT
