import struct
from .hkaiSilhouetteReferenceFrame import hkaiSilhouetteReferenceFrame


class hkaiSilhouetteGenerationParameters(object):
    extraExpansion: float
    bevelThreshold: float
    maxSilhouetteSize: float
    simplify2dConvexHullThreshold: float
    referenceFrame: hkaiSilhouetteReferenceFrame

    def __init__(self, infile):
        self.extraExpansion = struct.unpack('>f', infile.read(4))
        self.bevelThreshold = struct.unpack('>f', infile.read(4))
        self.maxSilhouetteSize = struct.unpack('>f', infile.read(4))
        self.simplify2dConvexHullThreshold = struct.unpack('>f', infile.read(4))
        self.referenceFrame = hkaiSilhouetteReferenceFrame(infile)  # TYPE_STRUCT
