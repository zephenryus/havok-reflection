from .hkReferencedObject import hkReferencedObject
from .hkpBreakableBodyController import hkpBreakableBodyController
from .hkpBreakableShape import hkpBreakableShape


class hkpBreakableBody(hkReferencedObject):
	controller: hkpBreakableBodyController
	breakableShape: hkpBreakableShape
	bodyTypeAndFlags: int
	constraintStrength: int
