from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpModifierConstraintAtom(hkpConstraintAtom):
    modifierAtomSize: int
    childSize: int
    child: any
    pad: int

    def __init__(self, infile):
        self.modifierAtomSize = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.childSize = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.child = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.pad = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} modifierAtomSize={modifierAtomSize}, childSize={childSize}, child={child}, pad={pad}>".format(**{
            "class_name": self.__class__.__name__,
            "modifierAtomSize": self.modifierAtomSize,
            "childSize": self.childSize,
            "child": self.child,
            "pad": self.pad,
        })
