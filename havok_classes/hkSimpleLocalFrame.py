from .hkLocalFrame import hkLocalFrame
from typing import List
from .common import get_array
from .hkLocalFrameGroup import hkLocalFrameGroup


class hkSimpleLocalFrame(hkLocalFrame):
    transform: any
    children: List[hkLocalFrame]
    parentFrame: any
    group: any
    name: str

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.children = get_array(infile, hkLocalFrame, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.parentFrame = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.group = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transform={transform}, children=[{children}], parentFrame={parentFrame}, group={group}, name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "transform": self.transform,
            "children": self.children,
            "parentFrame": self.parentFrame,
            "group": self.group,
            "name": self.name,
        })
