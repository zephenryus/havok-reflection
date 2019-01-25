from .hkpSetLocalTranslationsConstraintAtom import hkpSetLocalTranslationsConstraintAtom
from .hkpPulleyConstraintAtom import hkpPulleyConstraintAtom


class hkpPulleyConstraintDataAtoms(object):
    translations: hkpSetLocalTranslationsConstraintAtom
    pulley: hkpPulleyConstraintAtom

    def __init__(self, infile):
        self.translations = hkpSetLocalTranslationsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.pulley = hkpPulleyConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} translations={translations}, pulley={pulley}>".format(**{
            "class_name": self.__class__.__name__,
            "translations": self.translations,
            "pulley": self.pulley,
        })
