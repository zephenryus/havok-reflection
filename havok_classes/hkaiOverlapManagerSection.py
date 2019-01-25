from .common import any
import struct
from .hkaiOverlapManagerSectionGeneratorData import hkaiOverlapManagerSectionGeneratorData
from .hkSetIntFloatPair import hkSetIntFloatPair


class hkaiOverlapManagerSection(object):
    generatorDataMap: any
    numOriginalFaces: int
    generatorData: hkaiOverlapManagerSectionGeneratorData
    faceToGeneratorsMap: any
    facePriorities: hkSetIntFloatPair

    def __init__(self, infile):
        self.generatorDataMap = any(infile)  # TYPE_POINTER
        self.numOriginalFaces = struct.unpack('>i', infile.read(4))
        self.generatorData = hkaiOverlapManagerSectionGeneratorData(infile)  # TYPE_ARRAY
        self.faceToGeneratorsMap = any(infile)  # TYPE_ARRAY
        self.facePriorities = hkSetIntFloatPair(infile)  # TYPE_STRUCT
