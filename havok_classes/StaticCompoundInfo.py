import struct
from typing import List
from .common import get_array
from .ActorInfo import ActorInfo
from .ShapeInfo import ShapeInfo


class StaticCompoundInfo(object):
    Offset: int
    ActorInfo: List[ActorInfo]
    ShapeInfo: List[ShapeInfo]

    def __init__(self, infile):
        self.Offset = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.ActorInfo = get_array(infile, ActorInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.ShapeInfo = get_array(infile, ShapeInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} Offset={Offset}, ActorInfo=[{ActorInfo}], ShapeInfo=[{ShapeInfo}]>".format(**{
            "class_name": self.__class__.__name__,
            "Offset": self.Offset,
            "ActorInfo": self.ActorInfo,
            "ShapeInfo": self.ShapeInfo,
        })
