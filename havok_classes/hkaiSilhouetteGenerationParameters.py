import struct
from .hkaiSilhouetteReferenceFrame import hkaiSilhouetteReferenceFrame


class hkaiSilhouetteGenerationParameters(object):
    extraExpansion: float
    bevelThreshold: float
    maxSilhouetteSize: float
    simplify2dConvexHullThreshold: float
    referenceFrame: hkaiSilhouetteReferenceFrame

    def __init__(self, infile):
        self.extraExpansion = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bevelThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxSilhouetteSize = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.simplify2dConvexHullThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.referenceFrame = hkaiSilhouetteReferenceFrame(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} extraExpansion={extraExpansion}, bevelThreshold={bevelThreshold}, maxSilhouetteSize={maxSilhouetteSize}, simplify2dConvexHullThreshold={simplify2dConvexHullThreshold}, referenceFrame={referenceFrame}>".format(**{
            "class_name": self.__class__.__name__,
            "extraExpansion": self.extraExpansion,
            "bevelThreshold": self.bevelThreshold,
            "maxSilhouetteSize": self.maxSilhouetteSize,
            "simplify2dConvexHullThreshold": self.simplify2dConvexHullThreshold,
            "referenceFrame": self.referenceFrame,
        })
