from .hkReferencedObject import hkReferencedObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclTransformSetSetupObject import hclTransformSetSetupObject
import struct
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclBufferSetupObject import hclBufferSetupObject
from .hclSimClothSetupObjectTransferMotionSetupData import hclSimClothSetupObjectTransferMotionSetupData
from typing import List
from .common import get_array
from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimClothSetupObjectPerInstanceCollidable import hclSimClothSetupObjectPerInstanceCollidable


class hclSimClothSetupObject(hkReferencedObject):
    name: str
    simulationMesh: any
    collidableTransformSet: any
    gravity: vector4
    globalDampingPerSecond: float
    doNormals: bool
    specifyDensity: bool
    vertexDensity: hclVertexFloatInput
    rescaleMass: bool
    totalMass: float
    particleMass: hclVertexFloatInput
    particleRadius: hclVertexFloatInput
    particleFriction: hclVertexFloatInput
    fixedParticles: hclVertexSelectionInput
    enablePinchDetection: bool
    pinchDetectionEnabledParticles: hclVertexSelectionInput
    toAnimPeriod: float
    toSimPeriod: float
    drivePinchedParticlesToReferenceMesh: bool
    pinchReferenceBufferSetup: any
    collisionTolerance: float
    landscapeCollisionParticleSelection: hclVertexSelectionInput
    landscapeCollisionParticleRadius: float
    enableStuckParticleDetection: bool
    stuckParticlesStretchFactor: float
    enableLandscapePinchDetection: bool
    landscapePinchDetectionPriority: int
    landscapePinchDetectionRadius: float
    enableTransferMotion: bool
    transferMotionSetupData: hclSimClothSetupObjectTransferMotionSetupData
    constraintSetSetups: List[hclConstraintSetSetupObject]
    perInstanceCollidables: List[hclSimClothSetupObjectPerInstanceCollidable]
    orderMap: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simulationMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.collidableTransformSet = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.gravity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.globalDampingPerSecond = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.doNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.specifyDensity = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.vertexDensity = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.rescaleMass = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.totalMass = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.particleMass = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.particleRadius = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.particleFriction = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.fixedParticles = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.enablePinchDetection = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.pinchDetectionEnabledParticles = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.toAnimPeriod = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toSimPeriod = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.drivePinchedParticlesToReferenceMesh = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.pinchReferenceBufferSetup = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.collisionTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.landscapeCollisionParticleSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.landscapeCollisionParticleRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.enableStuckParticleDetection = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.stuckParticlesStretchFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.enableLandscapePinchDetection = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.landscapePinchDetectionPriority = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.landscapePinchDetectionRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.enableTransferMotion = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transferMotionSetupData = hclSimClothSetupObjectTransferMotionSetupData(infile)  # TYPE_STRUCT:TYPE_VOID
        self.constraintSetSetups = get_array(infile, hclConstraintSetSetupObject, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.perInstanceCollidables = get_array(infile, hclSimClothSetupObjectPerInstanceCollidable, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.orderMap = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simulationMesh={simulationMesh}, collidableTransformSet={collidableTransformSet}, gravity={gravity}, globalDampingPerSecond={globalDampingPerSecond}, doNormals={doNormals}, specifyDensity={specifyDensity}, vertexDensity={vertexDensity}, rescaleMass={rescaleMass}, totalMass={totalMass}, particleMass={particleMass}, particleRadius={particleRadius}, particleFriction={particleFriction}, fixedParticles={fixedParticles}, enablePinchDetection={enablePinchDetection}, pinchDetectionEnabledParticles={pinchDetectionEnabledParticles}, toAnimPeriod={toAnimPeriod}, toSimPeriod={toSimPeriod}, drivePinchedParticlesToReferenceMesh={drivePinchedParticlesToReferenceMesh}, pinchReferenceBufferSetup={pinchReferenceBufferSetup}, collisionTolerance={collisionTolerance}, landscapeCollisionParticleSelection={landscapeCollisionParticleSelection}, landscapeCollisionParticleRadius={landscapeCollisionParticleRadius}, enableStuckParticleDetection={enableStuckParticleDetection}, stuckParticlesStretchFactor={stuckParticlesStretchFactor}, enableLandscapePinchDetection={enableLandscapePinchDetection}, landscapePinchDetectionPriority={landscapePinchDetectionPriority}, landscapePinchDetectionRadius={landscapePinchDetectionRadius}, enableTransferMotion={enableTransferMotion}, transferMotionSetupData={transferMotionSetupData}, constraintSetSetups=[{constraintSetSetups}], perInstanceCollidables=[{perInstanceCollidables}], orderMap={orderMap}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simulationMesh": self.simulationMesh,
            "collidableTransformSet": self.collidableTransformSet,
            "gravity": self.gravity,
            "globalDampingPerSecond": self.globalDampingPerSecond,
            "doNormals": self.doNormals,
            "specifyDensity": self.specifyDensity,
            "vertexDensity": self.vertexDensity,
            "rescaleMass": self.rescaleMass,
            "totalMass": self.totalMass,
            "particleMass": self.particleMass,
            "particleRadius": self.particleRadius,
            "particleFriction": self.particleFriction,
            "fixedParticles": self.fixedParticles,
            "enablePinchDetection": self.enablePinchDetection,
            "pinchDetectionEnabledParticles": self.pinchDetectionEnabledParticles,
            "toAnimPeriod": self.toAnimPeriod,
            "toSimPeriod": self.toSimPeriod,
            "drivePinchedParticlesToReferenceMesh": self.drivePinchedParticlesToReferenceMesh,
            "pinchReferenceBufferSetup": self.pinchReferenceBufferSetup,
            "collisionTolerance": self.collisionTolerance,
            "landscapeCollisionParticleSelection": self.landscapeCollisionParticleSelection,
            "landscapeCollisionParticleRadius": self.landscapeCollisionParticleRadius,
            "enableStuckParticleDetection": self.enableStuckParticleDetection,
            "stuckParticlesStretchFactor": self.stuckParticlesStretchFactor,
            "enableLandscapePinchDetection": self.enableLandscapePinchDetection,
            "landscapePinchDetectionPriority": self.landscapePinchDetectionPriority,
            "landscapePinchDetectionRadius": self.landscapePinchDetectionRadius,
            "enableTransferMotion": self.enableTransferMotion,
            "transferMotionSetupData": self.transferMotionSetupData,
            "constraintSetSetups": self.constraintSetSetups,
            "perInstanceCollidables": self.perInstanceCollidables,
            "orderMap": self.orderMap,
        })
