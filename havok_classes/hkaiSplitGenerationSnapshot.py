from .hkaiNavMeshGenerationSnapshot import hkaiNavMeshGenerationSnapshot
from .hkaiSplitGenerationUtilsSettings import hkaiSplitGenerationUtilsSettings


class hkaiSplitGenerationSnapshot(object):
    generationSnapshot: hkaiNavMeshGenerationSnapshot
    splitSettings: hkaiSplitGenerationUtilsSettings

    def __init__(self, infile):
        self.generationSnapshot = hkaiNavMeshGenerationSnapshot(infile)  # TYPE_STRUCT:TYPE_VOID
        self.splitSettings = hkaiSplitGenerationUtilsSettings(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} generationSnapshot={generationSnapshot}, splitSettings={splitSettings}>".format(**{
            "class_name": self.__class__.__name__,
            "generationSnapshot": self.generationSnapshot,
            "splitSettings": self.splitSettings,
        })
