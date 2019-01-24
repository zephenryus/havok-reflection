from .hkaiSilhouetteReferenceFrame import hkaiSilhouetteReferenceFrame


class hkaiSilhouetteGenerationParameters(object):
    extraExpansion: float
    bevelThreshold: float
    maxSilhouetteSize: float
    simplify2dConvexHullThreshold: float
    referenceFrame: hkaiSilhouetteReferenceFrame
