from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclVolumeConstraintFrameData import hclVolumeConstraintFrameData
from .hclVolumeConstraintApplyData import hclVolumeConstraintApplyData


class hclVolumeConstraint(hclConstraintSet):
    frameDatas: List[hclVolumeConstraintFrameData]
    applyDatas: List[hclVolumeConstraintApplyData]

    def __init__(self, infile):
        self.frameDatas = get_array(infile, hclVolumeConstraintFrameData, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.applyDatas = get_array(infile, hclVolumeConstraintApplyData, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} frameDatas=[{frameDatas}], applyDatas=[{applyDatas}]>".format(**{
            "class_name": self.__class__.__name__,
            "frameDatas": self.frameDatas,
            "applyDatas": self.applyDatas,
        })
