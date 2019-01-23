from .hkBitField import hkBitField
from .hkBitField import hkBitField
from .hkBitField import hkBitField


class hclTransformSetUsageTransformTracker(object):
	read: hkBitField
	readBeforeWrite: hkBitField
	written: hkBitField
