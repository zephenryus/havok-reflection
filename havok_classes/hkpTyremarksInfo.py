from .hkReferencedObject import hkReferencedObject
from .hkpTyremarksWheel import hkpTyremarksWheel


class hkpTyremarksInfo(hkReferencedObject):
	minTyremarkEnergy: float
	maxTyremarkEnergy: float
	tyremarksWheel: hkpTyremarksWheel
