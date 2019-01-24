from .hkpConstraintAtom import hkpConstraintAtom
from .common import vector4


class hkpSetLocalTranslationsConstraintAtom(hkpConstraintAtom):
    translationA: vector4
    translationB: vector4
