from .hkaiNavMeshGenerationSnapshot import hkaiNavMeshGenerationSnapshot
from .hkaiSplitGenerationUtilsSettings import hkaiSplitGenerationUtilsSettings


class hkaiSplitGenerationSnapshot(object):
    generationSnapshot: hkaiNavMeshGenerationSnapshot
    splitSettings: hkaiSplitGenerationUtilsSettings

    def __init__(self, infile):
        self.generationSnapshot = hkaiNavMeshGenerationSnapshot(infile)  # TYPE_STRUCT
        self.splitSettings = hkaiSplitGenerationUtilsSettings(infile)  # TYPE_STRUCT
