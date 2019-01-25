from .hclConstraintSet import hclConstraintSet
from .hclVolumeConstraintFrameData import hclVolumeConstraintFrameData
from .hclVolumeConstraintApplyData import hclVolumeConstraintApplyData


class hclVolumeConstraint(hclConstraintSet):
    frameDatas: hclVolumeConstraintFrameData
    applyDatas: hclVolumeConstraintApplyData

    def __init__(self, infile):
        self.frameDatas = hclVolumeConstraintFrameData(infile)  # TYPE_ARRAY
        self.applyDatas = hclVolumeConstraintApplyData(infile)  # TYPE_ARRAY
