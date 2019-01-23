from .hkLocalFrame import hkLocalFrame
from .hkLocalFrame import hkLocalFrame
from .hkLocalFrame import hkLocalFrame
from .hkLocalFrameGroup import hkLocalFrameGroup


class hkSimpleLocalFrame(hkLocalFrame):
	transform: any
	children: hkLocalFrame
	parentFrame: hkLocalFrame
	group: hkLocalFrameGroup
	name: any
