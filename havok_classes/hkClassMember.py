from .hkClass import hkClass
from .hkClassEnum import hkClassEnum
from .hkCustomAttributes import hkCustomAttributes


class hkClassMember(object):
	name: any
	class: hkClass
	enum: hkClassEnum
	type: any
	subtype: any
	cArraySize: int
	flags: any
	offset: int
	attributes: hkCustomAttributes
