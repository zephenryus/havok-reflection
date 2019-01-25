from .hkReferencedObject import hkReferencedObject
from .hclSimClothDataOverridableSimulationInfo import hclSimClothDataOverridableSimulationInfo
from .hclSimClothDataParticleData import hclSimClothDataParticleData
from .common import any
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
    particleDatas: hclSimClothDataParticleData
    fixedParticles: any
    triangleIndices: any
    triangleFlips: any
    totalMass: float
    collidableTransformMap: hclSimClothDataCollidableTransformMap
    perInstanceCollidables: hclCollidable
    staticConstraintSets: hclConstraintSet
    antiPinchConstraintSets: hclConstraintSet
    simClothPoses: hclSimClothPose
    actions: hclAction
    staticCollisionMasks: any
    perParticlePinchDetectionEnabledFlags: any
    collidablePinchingDatas: hclSimClothDataCollidablePinchingData
    minPinchedParticleIndex: int
    maxPinchedParticleIndex: int
    maxCollisionPairs: int
    maxParticleRadius: float
    landscapeCollisionData: hclSimClothDataLandscapeCollisionData
    numLandscapeCollidableParticles: int
    doNormals: bool
    transferMotionData: hclSimClothDataTransferMotionData

    def __init__(self, infile):
        self.simulationInfo = hclSimClothDataOverridableSimulationInfo(infile)  # TYPE_STRUCT
        self.name = struct.unpack('>s', infile.read(0))
        self.particleDatas = hclSimClothDataParticleData(infile)  # TYPE_ARRAY
        self.fixedParticles = any(infile)  # TYPE_ARRAY
        self.triangleIndices = any(infile)  # TYPE_ARRAY
        self.triangleFlips = any(infile)  # TYPE_ARRAY
        self.totalMass = struct.unpack('>f', infile.read(4))
        self.collidableTransformMap = hclSimClothDataCollidableTransformMap(infile)  # TYPE_STRUCT
        self.perInstanceCollidables = hclCollidable(infile)  # TYPE_ARRAY
        self.staticConstraintSets = hclConstraintSet(infile)  # TYPE_ARRAY
        self.antiPinchConstraintSets = hclConstraintSet(infile)  # TYPE_ARRAY
        self.simClothPoses = hclSimClothPose(infile)  # TYPE_ARRAY
        self.actions = hclAction(infile)  # TYPE_ARRAY
        self.staticCollisionMasks = any(infile)  # TYPE_ARRAY
        self.perParticlePinchDetectionEnabledFlags = any(infile)  # TYPE_ARRAY
        self.collidablePinchingDatas = hclSimClothDataCollidablePinchingData(infile)  # TYPE_ARRAY
        self.minPinchedParticleIndex = struct.unpack('>H', infile.read(2))
        self.maxPinchedParticleIndex = struct.unpack('>H', infile.read(2))
        self.maxCollisionPairs = struct.unpack('>I', infile.read(4))
        self.maxParticleRadius = struct.unpack('>f', infile.read(4))
        self.landscapeCollisionData = hclSimClothDataLandscapeCollisionData(infile)  # TYPE_STRUCT
        self.numLandscapeCollidableParticles = struct.unpack('>I', infile.read(4))
        self.doNormals = struct.unpack('>?', infile.read(1))
        self.transferMotionData = hclSimClothDataTransferMotionData(infile)  # TYPE_STRUCT
