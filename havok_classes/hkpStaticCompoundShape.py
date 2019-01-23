from .hkpBvTreeShape import hkpBvTreeShape
from .hkpStaticCompoundShapeInstance import hkpStaticCompoundShapeInstance
from .hkpShapeKeyTable import hkpShapeKeyTable
from .hkcdStaticTreeDefaultTreeStorage6 import hkcdStaticTreeDefaultTreeStorage6


class hkpStaticCompoundShape(hkpBvTreeShape):
	numBitsForChildShapeKey: int
	referencePolicy: int
	childShapeKeyMask: int
	instances: hkpStaticCompoundShapeInstance
	instanceExtraInfos: any
	disabledLargeShapeKeyTable: hkpShapeKeyTable
	tree: hkcdStaticTreeDefaultTreeStorage6
