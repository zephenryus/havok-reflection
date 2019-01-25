from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpModifierConstraintAtom(hkpConstraintAtom):
    modifierAtomSize: int
    childSize: int
    child: hkpConstraintAtom
    pad: int

    def __init__(self, infile):
        self.modifierAtomSize = struct.unpack('>H', infile.read(2))
        self.childSize = struct.unpack('>H', infile.read(2))
        self.child = hkpConstraintAtom(infile)  # TYPE_POINTER
        self.pad = struct.unpack('>I', infile.read(4))
