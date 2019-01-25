from .hkReferencedObject import hkReferencedObject
from .hkaiSilhouetteGeneratorSectionContext import hkaiSilhouetteGeneratorSectionContext
from .common import any


class hkaiOverlapManagerSectionGeneratorData(hkReferencedObject):
    context: hkaiSilhouetteGeneratorSectionContext
    overlappedFaces: any

    def __init__(self, infile):
        self.context = hkaiSilhouetteGeneratorSectionContext(infile)  # TYPE_STRUCT
        self.overlappedFaces = any(infile)  # TYPE_ARRAY
