from .hkpGenericConstraintDataSchemeConstraintInfo import hkpGenericConstraintDataSchemeConstraintInfo
from .hkpConstraintMotor import hkpConstraintMotor


class hkpGenericConstraintDataScheme(object):
	info: hkpGenericConstraintDataSchemeConstraintInfo
	data: any
	commands: any
	modifiers: any
	motors: hkpConstraintMotor
