from .hkpGenericConstraintDataSchemeConstraintInfo import hkpGenericConstraintDataSchemeConstraintInfo
from .common import any
from .hkpConstraintMotor import hkpConstraintMotor


class hkpGenericConstraintDataScheme(object):
    info: hkpGenericConstraintDataSchemeConstraintInfo
    data: any
    commands: any
    modifiers: any
    motors: hkpConstraintMotor

    def __init__(self, infile):
        self.info = hkpGenericConstraintDataSchemeConstraintInfo(infile)  # TYPE_STRUCT
        self.data = any(infile)  # TYPE_ARRAY
        self.commands = any(infile)  # TYPE_ARRAY
        self.modifiers = any(infile)  # TYPE_ARRAY
        self.motors = hkpConstraintMotor(infile)  # TYPE_ARRAY
