from .common import any
from .hkaiOverlapManagerSectionGeneratorData import hkaiOverlapManagerSectionGeneratorData
from .hkSetIntFloatPair import hkSetIntFloatPair


class hkaiOverlapManagerSection(object):
    generatorDataMap: any
    numOriginalFaces: int
    generatorData: hkaiOverlapManagerSectionGeneratorData
    faceToGeneratorsMap: any
    facePriorities: hkSetIntFloatPair
