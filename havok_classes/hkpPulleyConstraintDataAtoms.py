from .hkpSetLocalTranslationsConstraintAtom import hkpSetLocalTranslationsConstraintAtom
from .hkpPulleyConstraintAtom import hkpPulleyConstraintAtom


class hkpPulleyConstraintDataAtoms(object):
    translations: hkpSetLocalTranslationsConstraintAtom
    pulley: hkpPulleyConstraintAtom

    def __init__(self, infile):
        self.translations = hkpSetLocalTranslationsConstraintAtom(infile)  # TYPE_STRUCT
        self.pulley = hkpPulleyConstraintAtom(infile)  # TYPE_STRUCT
