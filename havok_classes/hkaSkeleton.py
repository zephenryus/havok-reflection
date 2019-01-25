from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkaBone import hkaBone
from .hkaSkeletonLocalFrameOnBone import hkaSkeletonLocalFrameOnBone
from .hkaSkeletonPartition import hkaSkeletonPartition


class hkaSkeleton(hkReferencedObject):
    name: str
    parentIndices: List[int]
    bones: List[hkaBone]
    referencePose: List[any]
    referenceFloats: List[float]
    floatSlots: List[str]
    localFrames: List[hkaSkeletonLocalFrameOnBone]
    partitions: List[hkaSkeletonPartition]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.parentIndices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16
        self.bones = get_array(infile, hkaBone, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.referencePose = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_QSTRANSFORM
        self.referenceFloats = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.floatSlots = get_array(infile, str, 0)  # TYPE_ARRAY:TYPE_STRINGPTR
        self.localFrames = get_array(infile, hkaSkeletonLocalFrameOnBone, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.partitions = get_array(infile, hkaSkeletonPartition, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} name=\"{name}\", parentIndices=[{parentIndices}], bones=[{bones}], referencePose=[{referencePose}], referenceFloats=[{referenceFloats}], floatSlots=[{floatSlots}], localFrames=[{localFrames}], partitions=[{partitions}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "parentIndices": self.parentIndices,
            "bones": self.bones,
            "referencePose": self.referencePose,
            "referenceFloats": self.referenceFloats,
            "floatSlots": self.floatSlots,
            "localFrames": self.localFrames,
            "partitions": self.partitions,
        })
