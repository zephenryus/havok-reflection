import struct
from typing import List
from .common import get_array
from .hkaiOverlapManagerSectionGeneratorData import hkaiOverlapManagerSectionGeneratorData
from .hkSetIntFloatPair import hkSetIntFloatPair


class hkaiOverlapManagerSection(object):
    generatorDataMap: any
    numOriginalFaces: int
    generatorData: List[hkaiOverlapManagerSectionGeneratorData]
    faceToGeneratorsMap: List[any]
    facePriorities: hkSetIntFloatPair

    def __init__(self, infile):
        self.generatorDataMap = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.numOriginalFaces = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.generatorData = get_array(infile, hkaiOverlapManagerSectionGeneratorData, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.faceToGeneratorsMap = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.facePriorities = hkSetIntFloatPair(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} generatorDataMap={generatorDataMap}, numOriginalFaces={numOriginalFaces}, generatorData=[{generatorData}], faceToGeneratorsMap=[{faceToGeneratorsMap}], facePriorities={facePriorities}>".format(**{
            "class_name": self.__class__.__name__,
            "generatorDataMap": self.generatorDataMap,
            "numOriginalFaces": self.numOriginalFaces,
            "generatorData": self.generatorData,
            "faceToGeneratorsMap": self.faceToGeneratorsMap,
            "facePriorities": self.facePriorities,
        })
