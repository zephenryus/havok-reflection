from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
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
    registrations: List[hkaiNavMeshClearanceCacheManagerRegistration]
    cacheInfos: List[hkaiNavMeshClearanceCacheManagerCacheInfo]
    defaultOption: DefaultCachingOption

    def __init__(self, infile):
        self.registrations = get_array(infile, hkaiNavMeshClearanceCacheManagerRegistration, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.cacheInfos = get_array(infile, hkaiNavMeshClearanceCacheManagerCacheInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.defaultOption = DefaultCachingOption(infile)  # TYPE_ENUM:TYPE_INT32

    def __repr__(self):
        return "<{class_name} registrations=[{registrations}], cacheInfos=[{cacheInfos}], defaultOption={defaultOption}>".format(**{
            "class_name": self.__class__.__name__,
            "registrations": self.registrations,
            "cacheInfos": self.cacheInfos,
            "defaultOption": self.defaultOption,
        })
