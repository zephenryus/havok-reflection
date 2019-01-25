from .hkReferencedObject import hkReferencedObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .common import vector4, any
import struct
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclBufferSetupObject import hclBufferSetupObject
from .hclSimClothSetupObjectTransferMotionSetupData import hclSimClothSetupObjectTransferMotionSetupData
from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimClothSetupObjectPerInstanceCollidable import hclSimClothSetupObjectPerInstanceCollidable


class hclSimClothSetupObject(hkReferencedObject):
    name: str
    simulationMesh: hclSimulationSetupMesh
    collidableTransformSet: hclTransformSetSetupObject
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
    pinchReferenceBufferSetup: hclBufferSetupObject
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
    constraintSetSetups: hclConstraintSetSetupObject
    perInstanceCollidables: hclSimClothSetupObjectPerInstanceCollidable
    orderMap: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simulationMesh = hclSimulationSetupMesh(infile)  # TYPE_POINTER
        self.collidableTransformSet = hclTransformSetSetupObject(infile)  # TYPE_POINTER
        self.gravity = struct.unpack('>4f', infile.read(16))
        self.globalDampingPerSecond = struct.unpack('>f', infile.read(4))
        self.doNormals = struct.unpack('>?', infile.read(1))
        self.specifyDensity = struct.unpack('>?', infile.read(1))
        self.vertexDensity = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.rescaleMass = struct.unpack('>?', infile.read(1))
        self.totalMass = struct.unpack('>f', infile.read(4))
        self.particleMass = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.particleRadius = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.particleFriction = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.fixedParticles = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.enablePinchDetection = struct.unpack('>?', infile.read(1))
        self.pinchDetectionEnabledParticles = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.toAnimPeriod = struct.unpack('>f', infile.read(4))
        self.toSimPeriod = struct.unpack('>f', infile.read(4))
        self.drivePinchedParticlesToReferenceMesh = struct.unpack('>?', infile.read(1))
        self.pinchReferenceBufferSetup = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.collisionTolerance = struct.unpack('>f', infile.read(4))
        self.landscapeCollisionParticleSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.landscapeCollisionParticleRadius = struct.unpack('>f', infile.read(4))
        self.enableStuckParticleDetection = struct.unpack('>?', infile.read(1))
        self.stuckParticlesStretchFactor = struct.unpack('>f', infile.read(4))
        self.enableLandscapePinchDetection = struct.unpack('>?', infile.read(1))
        self.landscapePinchDetectionPriority = struct.unpack('>b', infile.read(1))
        self.landscapePinchDetectionRadius = struct.unpack('>f', infile.read(4))
        self.enableTransferMotion = struct.unpack('>?', infile.read(1))
        self.transferMotionSetupData = hclSimClothSetupObjectTransferMotionSetupData(infile)  # TYPE_STRUCT
        self.constraintSetSetups = hclConstraintSetSetupObject(infile)  # TYPE_ARRAY
        self.perInstanceCollidables = hclSimClothSetupObjectPerInstanceCollidable(infile)  # TYPE_ARRAY
        self.orderMap = any(infile)  # TYPE_POINTER
