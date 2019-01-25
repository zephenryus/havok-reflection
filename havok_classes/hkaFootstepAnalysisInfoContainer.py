from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkaFootstepAnalysisInfo import hkaFootstepAnalysisInfo


class hkaFootstepAnalysisInfoContainer(hkReferencedObject):
    previewInfo: List[hkaFootstepAnalysisInfo]

    def __init__(self, infile):
        self.previewInfo = get_array(infile, hkaFootstepAnalysisInfo, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} previewInfo=[{previewInfo}]>".format(**{
            "class_name": self.__class__.__name__,
            "previewInfo": self.previewInfo,
        })
