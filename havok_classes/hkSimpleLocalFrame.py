from .hkLocalFrame import hkLocalFrame
from .common import any
from .hkLocalFrameGroup import hkLocalFrameGroup


class hkSimpleLocalFrame(hkLocalFrame):
    transform: any
    children: hkLocalFrame
    parentFrame: hkLocalFrame
    group: hkLocalFrameGroup
    name: str

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_TRANSFORM
        self.children = hkLocalFrame(infile)  # TYPE_ARRAY
        self.parentFrame = hkLocalFrame(infile)  # TYPE_POINTER
        self.group = hkLocalFrameGroup(infile)  # TYPE_POINTER
        self.name = struct.unpack('>s', infile.read(0))
