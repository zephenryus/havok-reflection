from .hkpGenericConstraintDataSchemeConstraintInfo import hkpGenericConstraintDataSchemeConstraintInfo
from typing import List
from .common import get_array
from .hkpConstraintMotor import hkpConstraintMotor


class hkpGenericConstraintDataScheme(object):
    info: hkpGenericConstraintDataSchemeConstraintInfo
    data: List[vector4]
    commands: List[int]
    modifiers: List[any]
    motors: List[hkpConstraintMotor]

    def __init__(self, infile):
        self.info = hkpGenericConstraintDataSchemeConstraintInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.data = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.commands = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.modifiers = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.motors = get_array(infile, hkpConstraintMotor, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} info={info}, data=[{data}], commands=[{commands}], modifiers=[{modifiers}], motors=[{motors}]>".format(**{
            "class_name": self.__class__.__name__,
            "info": self.info,
            "data": self.data,
            "commands": self.commands,
            "modifiers": self.modifiers,
            "motors": self.motors,
        })
