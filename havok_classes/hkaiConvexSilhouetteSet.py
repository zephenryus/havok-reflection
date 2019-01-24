from .hkReferencedObject import hkReferencedObject
from .common import any, vector4
from .hkQTransform import hkQTransform


class hkaiConvexSilhouetteSet(hkReferencedObject):
    vertexPool: any
    silhouetteOffsets: any
    cachedTransform: hkQTransform
    cachedUp: vector4
