from .hkReferencedObject import hkReferencedObject
from .hkpLinkedCollidable import hkpLinkedCollidable
from .hkMultiThreadCheck import hkMultiThreadCheck
from .hkSimpleProperty import hkSimpleProperty


class hkpWorldObject(hkReferencedObject):
	world: any
	userData: int
	collidable: hkpLinkedCollidable
	multiThreadCheck: hkMultiThreadCheck
	name: any
	properties: hkSimpleProperty
