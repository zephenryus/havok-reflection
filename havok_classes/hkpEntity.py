from .hkpWorldObject import hkpWorldObject
from .hkpMaterial import hkpMaterial
from .hkpEntitySmallArraySerializeOverrideType import hkpEntitySmallArraySerializeOverrideType
from .hkpConstraintInstance import hkpConstraintInstance
from .hkpEntitySpuCollisionCallback import hkpEntitySpuCollisionCallback
from .hkpMaxSizeMotion import hkpMaxSizeMotion
from .hkpEntitySmallArraySerializeOverrideType import hkpEntitySmallArraySerializeOverrideType
from .hkpEntitySmallArraySerializeOverrideType import hkpEntitySmallArraySerializeOverrideType
from .hkLocalFrame import hkLocalFrame
from .hkpEntityExtendedListeners import hkpEntityExtendedListeners


class hkpEntity(hkpWorldObject):
	material: hkpMaterial
	limitContactImpulseUtilAndFlag: any
	damageMultiplier: float
	breakableBody: any
	solverData: int
	storageIndex: int
	contactPointCallbackDelay: int
	constraintsMaster: hkpEntitySmallArraySerializeOverrideType
	constraintsSlave: hkpConstraintInstance
	constraintRuntime: any
	simulationIsland: any
	autoRemoveLevel: int
	numShapeKeysInContactPointProperties: int
	responseModifierFlags: int
	uid: int
	spuCollisionCallback: hkpEntitySpuCollisionCallback
	motion: hkpMaxSizeMotion
	contactListeners: hkpEntitySmallArraySerializeOverrideType
	actions: hkpEntitySmallArraySerializeOverrideType
	localFrame: hkLocalFrame
	extendedListeners: hkpEntityExtendedListeners
	npData: int
