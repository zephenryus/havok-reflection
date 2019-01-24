from .hkReferencedObject import hkReferencedObject
from .hclSimClothDataOverridableSimulationInfo import hclSimClothDataOverridableSimulationInfo
from .hclSimClothDataParticleData import hclSimClothDataParticleData
from .common import any
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
