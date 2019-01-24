from .hkReferencedObject import hkReferencedObject
from .hkaiSilhouetteGeneratorSectionContext import hkaiSilhouetteGeneratorSectionContext
from .common import any


class hkaiOverlapManagerSectionGeneratorData(hkReferencedObject):
    context: hkaiSilhouetteGeneratorSectionContext
    overlappedFaces: any
