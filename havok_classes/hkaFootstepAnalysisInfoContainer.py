from .hkReferencedObject import hkReferencedObject
from .hkaFootstepAnalysisInfo import hkaFootstepAnalysisInfo


class hkaFootstepAnalysisInfoContainer(hkReferencedObject):
    previewInfo: hkaFootstepAnalysisInfo

    def __init__(self, infile):
        self.previewInfo = hkaFootstepAnalysisInfo(infile)  # TYPE_ARRAY
