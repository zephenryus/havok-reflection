from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiNavMeshClearanceCacheManagerRegistration import hkaiNavMeshClearanceCacheManagerRegistration
from .hkaiNavMeshClearanceCacheManagerCacheInfo import hkaiNavMeshClearanceCacheManagerCacheInfo
from .enums import DefaultCachingOption


class CachingOption(Enum):
    CACHE = 0
    USE_UNFILTERED = 1
    DO_NOT_CACHE = 2
    NOT_SET = 4294967295


class DefaultCachingOption(Enum):
    DCO_WARN_AND_TREAT_AS_UNFILTERED = 0
    DCO_TREAT_AS_UNFILTERED = 1
    DCO_DO_NOT_CACHE = 2
    DCO_ASSERT = 3


class hkaiNavMeshClearanceCacheManager(hkReferencedObject):
    registrations: hkaiNavMeshClearanceCacheManagerRegistration
    cacheInfos: hkaiNavMeshClearanceCacheManagerCacheInfo
    defaultOption: DefaultCachingOption

    def __init__(self, infile):
        self.registrations = hkaiNavMeshClearanceCacheManagerRegistration(infile)  # TYPE_ARRAY
        self.cacheInfos = hkaiNavMeshClearanceCacheManagerCacheInfo(infile)  # TYPE_ARRAY
        self.defaultOption = DefaultCachingOption(infile)  # TYPE_ENUM
