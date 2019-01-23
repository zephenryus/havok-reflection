from .hkpShape import hkpShape
from .hkpCdBody import hkpCdBody


class hkpCdBody(object):
	shape: hkpShape
	shapeKey: int
	motion: any
	parent: hkpCdBody
