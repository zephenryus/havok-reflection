from .hkReferencedObject import hkReferencedObject
from .hclSimClothDataOverridableSimulationInfo import hclSimClothDataOverridableSimulationInfo
from typing import List
from .common import get_array
from .hclSimClothDataParticleData import hclSimClothDataParticleData
import struct
from .hclSimClothDataCollidableTransformMap import hclSimClothDataCollidableTransformMap
from .hclCollidable import hclCollidable
from .hclConstraintSet import hclConstraintSet
from .hclSimClothPose import hclSimClothPose
from .hclAction import hclAction
from .hclSimClothDataCollidablePinchingData import hclSimClothDataCollidablePinchingData
from .hclSimClothDataLandscapeCollisionData import hclSimClothDataLandscapeCollisionData
from .hclSimClothDataTransferMotionData import hclSimClothDataTransferMotionData


class hclSimClothData(hkReferencedObject):
    simulationInfo: hclSimClothDataOverridableSimulationInfo
    name: str
    particleDatas: List[hclSimClothDataParticleData]
    fixedParticles: List[int]
    triangleIndices: List[int]
    triangleFlips: List[int]
    totalMass: float
    collidableTransformMap: hclSimClothDataCollidableTransformMap
    perInstanceCollidables: List[hclCollidable]
    staticConstraintSets: List[hclConstraintSet]
    antiPinchConstraintSets: List[hclConstraintSet]
    simClothPoses: List[hclSimClothPose]
    actions: List[hclAction]
    staticCollisionMasks: List[int]
    perParticlePinchDetectionEnabledFlags: List[bool]
    collidablePinchingDatas: List[hclSimClothDataCollidablePinchingData]
    minPinchedParticleIndex: int
    maxPinchedParticleIndex: int
    maxCollisionPairs: int
    maxParticleRadius: float
    landscapeCollisionData: hclSimClothDataLandscapeCollisionData
    numLandscapeCollidableParticles: int
    doNormals: bool
    transferMotionData: hclSimClothDataTransferMotionData

    def __init__(self, infile):
        self.simulationInfo = hclSimClothDataOverridableSimulationInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.particleDatas = get_array(infile, hclSimClothDataParticleData, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.fixedParticles = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.triangleIndices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.triangleFlips = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.totalMass = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.collidableTransformMap = hclSimClothDataCollidableTransformMap(infile)  # TYPE_STRUCT:TYPE_VOID
        self.perInstanceCollidables = get_array(infile, hclCollidable, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.staticConstraintSets = get_array(infile, hclConstraintSet, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.antiPinchConstraintSets = get_array(infile, hclConstraintSet, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.simClothPoses = get_array(infile, hclSimClothPose, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.actions = get_array(infile, hclAction, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.staticCollisionMasks = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.perParticlePinchDetectionEnabledFlags = get_array(infile, bool, 1)  # TYPE_ARRAY:TYPE_BOOL
        self.collidablePinchingDatas = get_array(infile, hclSimClothDataCollidablePinchingData, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.minPinchedParticleIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.maxPinchedParticleIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.maxCollisionPairs = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.maxParticleRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.landscapeCollisionData = hclSimClothDataLandscapeCollisionData(infile)  # TYPE_STRUCT:TYPE_VOID
        self.numLandscapeCollidableParticles = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.doNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transferMotionData = hclSimClothDataTransferMotionData(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} simulationInfo={simulationInfo}, name=\"{name}\", particleDatas=[{particleDatas}], fixedParticles=[{fixedParticles}], triangleIndices=[{triangleIndices}], triangleFlips=[{triangleFlips}], totalMass={totalMass}, collidableTransformMap={collidableTransformMap}, perInstanceCollidables=[{perInstanceCollidables}], staticConstraintSets=[{staticConstraintSets}], antiPinchConstraintSets=[{antiPinchConstraintSets}], simClothPoses=[{simClothPoses}], actions=[{actions}], staticCollisionMasks=[{staticCollisionMasks}], perParticlePinchDetectionEnabledFlags=[{perParticlePinchDetectionEnabledFlags}], collidablePinchingDatas=[{collidablePinchingDatas}], minPinchedParticleIndex={minPinchedParticleIndex}, maxPinchedParticleIndex={maxPinchedParticleIndex}, maxCollisionPairs={maxCollisionPairs}, maxParticleRadius={maxParticleRadius}, landscapeCollisionData={landscapeCollisionData}, numLandscapeCollidableParticles={numLandscapeCollidableParticles}, doNormals={doNormals}, transferMotionData={transferMotionData}>".format(**{
            "class_name": self.__class__.__name__,
            "simulationInfo": self.simulationInfo,
            "name": self.name,
            "particleDatas": self.particleDatas,
            "fixedParticles": self.fixedParticles,
            "triangleIndices": self.triangleIndices,
            "triangleFlips": self.triangleFlips,
            "totalMass": self.totalMass,
            "collidableTransformMap": self.collidableTransformMap,
            "perInstanceCollidables": self.perInstanceCollidables,
            "staticConstraintSets": self.staticConstraintSets,
            "antiPinchConstraintSets": self.antiPinchConstraintSets,
            "simClothPoses": self.simClothPoses,
            "actions": self.actions,
            "staticCollisionMasks": self.staticCollisionMasks,
            "perParticlePinchDetectionEnabledFlags": self.perParticlePinchDetectionEnabledFlags,
            "collidablePinchingDatas": self.collidablePinchingDatas,
            "minPinchedParticleIndex": self.minPinchedParticleIndex,
            "maxPinchedParticleIndex": self.maxPinchedParticleIndex,
            "maxCollisionPairs": self.maxCollisionPairs,
            "maxParticleRadius": self.maxParticleRadius,
            "landscapeCollisionData": self.landscapeCollisionData,
            "numLandscapeCollidableParticles": self.numLandscapeCollidableParticles,
            "doNormals": self.doNormals,
            "transferMotionData": self.transferMotionData,
        })
