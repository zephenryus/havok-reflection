from .hkpShape import hkpShape


class hkpStaticCompoundShapeInstance(object):
	transform: any
	shape: hkpShape
	filterInfo: int
	childFilterInfoMask: int
	userData: int
