from .hkClass import hkClass
from .hkClassEnum import hkClassEnum
from .hkClassMember import hkClassMember
from .hkCustomAttributes import hkCustomAttributes


class hkClass(object):
	name: any
	parent: hkClass
	objectSize: int
	numImplementedInterfaces: int
	declaredEnums: hkClassEnum
	declaredMembers: hkClassMember
	defaults: any
	attributes: hkCustomAttributes
	flags: any
	describedVersion: int
