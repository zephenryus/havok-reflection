from .hkReferencedObject import hkReferencedObject
from .hkaiSilhouetteGeneratorSectionContext import hkaiSilhouetteGeneratorSectionContext
from typing import List
from .common import get_array


class hkaiOverlapManagerSectionGeneratorData(hkReferencedObject):
    context: hkaiSilhouetteGeneratorSectionContext
    overlappedFaces: List[int]

    def __init__(self, infile):
        self.context = hkaiSilhouetteGeneratorSectionContext(infile)  # TYPE_STRUCT:TYPE_VOID
        self.overlappedFaces = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32

    def __repr__(self):
        return "<{class_name} context={context}, overlappedFaces=[{overlappedFaces}]>".format(**{
            "class_name": self.__class__.__name__,
            "context": self.context,
            "overlappedFaces": self.overlappedFaces,
        })
