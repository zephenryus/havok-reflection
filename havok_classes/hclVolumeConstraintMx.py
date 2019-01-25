from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclVolumeConstraintMxFrameBatchData import hclVolumeConstraintMxFrameBatchData
from .hclVolumeConstraintMxFrameSingleData import hclVolumeConstraintMxFrameSingleData
from .hclVolumeConstraintMxApplyBatchData import hclVolumeConstraintMxApplyBatchData
from .hclVolumeConstraintMxApplySingleData import hclVolumeConstraintMxApplySingleData


class hclVolumeConstraintMx(hclConstraintSet):
    frameBatchDatas: List[hclVolumeConstraintMxFrameBatchData]
    frameSingleDatas: List[hclVolumeConstraintMxFrameSingleData]
    applyBatchDatas: List[hclVolumeConstraintMxApplyBatchData]
    applySingleDatas: List[hclVolumeConstraintMxApplySingleData]

    def __init__(self, infile):
        self.frameBatchDatas = get_array(infile, hclVolumeConstraintMxFrameBatchData, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.frameSingleDatas = get_array(infile, hclVolumeConstraintMxFrameSingleData, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.applyBatchDatas = get_array(infile, hclVolumeConstraintMxApplyBatchData, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.applySingleDatas = get_array(infile, hclVolumeConstraintMxApplySingleData, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} frameBatchDatas=[{frameBatchDatas}], frameSingleDatas=[{frameSingleDatas}], applyBatchDatas=[{applyBatchDatas}], applySingleDatas=[{applySingleDatas}]>".format(**{
            "class_name": self.__class__.__name__,
            "frameBatchDatas": self.frameBatchDatas,
            "frameSingleDatas": self.frameSingleDatas,
            "applyBatchDatas": self.applyBatchDatas,
            "applySingleDatas": self.applySingleDatas,
        })
