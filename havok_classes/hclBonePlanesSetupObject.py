from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .hclBonePlanesSetupObjectPerParticlePlane import hclBonePlanesSetupObjectPerParticlePlane
from .hclBonePlanesSetupObjectGlobalPlane import hclBonePlanesSetupObjectGlobalPlane
from .hclBonePlanesSetupObjectPerParticleAngle import hclBonePlanesSetupObjectPerParticleAngle
import struct


class hclBonePlanesSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: hclSimulationSetupMesh
    transformSetSetup: hclTransformSetSetupObject
    perParticlePlanes: hclBonePlanesSetupObjectPerParticlePlane
    globalPlanes: hclBonePlanesSetupObjectGlobalPlane
    perParticleAngle: hclBonePlanesSetupObjectPerParticleAngle
    angleSpecifiedInDegrees: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simulationMesh = hclSimulationSetupMesh(infile)  # TYPE_POINTER
        self.transformSetSetup = hclTransformSetSetupObject(infile)  # TYPE_POINTER
        self.perParticlePlanes = hclBonePlanesSetupObjectPerParticlePlane(infile)  # TYPE_ARRAY
        self.globalPlanes = hclBonePlanesSetupObjectGlobalPlane(infile)  # TYPE_ARRAY
        self.perParticleAngle = hclBonePlanesSetupObjectPerParticleAngle(infile)  # TYPE_ARRAY
        self.angleSpecifiedInDegrees = struct.unpack('>?', infile.read(1))
