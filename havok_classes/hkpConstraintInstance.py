from .hkReferencedObject import hkReferencedObject
from .hkpConstraintData import hkpConstraintData
from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
from .hkpEntity import hkpEntity
from .hkpConstraintInstanceSmallArraySerializeOverrideType import hkpConstraintInstanceSmallArraySerializeOverrideType


class hkpConstraintInstance(hkReferencedObject):
	owner: any
	data: hkpConstraintData
	constraintModifiers: hkpModifierConstraintAtom
	entities: hkpEntity
	priority: any
	wantRuntime: bool
	destructionRemapInfo: any
	listeners: hkpConstraintInstanceSmallArraySerializeOverrideType
	name: any
	userData: int
	internal: any
	uid: int
