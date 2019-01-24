from .hkLocalFrame import hkLocalFrame
from .common import any
from .hkLocalFrameGroup import hkLocalFrameGroup


class hkSimpleLocalFrame(hkLocalFrame):
    transform: any
    children: hkLocalFrame
    parentFrame: hkLocalFrame
    group: hkLocalFrameGroup
    name: str
