from .hclConstraintSet import hclConstraintSet
from .hclVolumeConstraintMxFrameBatchData import hclVolumeConstraintMxFrameBatchData
from .hclVolumeConstraintMxFrameSingleData import hclVolumeConstraintMxFrameSingleData
from .hclVolumeConstraintMxApplyBatchData import hclVolumeConstraintMxApplyBatchData
from .hclVolumeConstraintMxApplySingleData import hclVolumeConstraintMxApplySingleData


class hclVolumeConstraintMx(hclConstraintSet):
    frameBatchDatas: hclVolumeConstraintMxFrameBatchData
    frameSingleDatas: hclVolumeConstraintMxFrameSingleData
    applyBatchDatas: hclVolumeConstraintMxApplyBatchData
    applySingleDatas: hclVolumeConstraintMxApplySingleData

    def __init__(self, infile):
        self.frameBatchDatas = hclVolumeConstraintMxFrameBatchData(infile)  # TYPE_ARRAY
        self.frameSingleDatas = hclVolumeConstraintMxFrameSingleData(infile)  # TYPE_ARRAY
        self.applyBatchDatas = hclVolumeConstraintMxApplyBatchData(infile)  # TYPE_ARRAY
        self.applySingleDatas = hclVolumeConstraintMxApplySingleData(infile)  # TYPE_ARRAY
