from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .hclBonePlanesSetupObjectPerParticlePlane import hclBonePlanesSetupObjectPerParticlePlane
from .hclBonePlanesSetupObjectGlobalPlane import hclBonePlanesSetupObjectGlobalPlane
from .hclBonePlanesSetupObjectPerParticleAngle import hclBonePlanesSetupObjectPerParticleAngle


class hclBonePlanesSetupObject(hclConstraintSetSetupObject):
	name: any
	simulationMesh: hclSimulationSetupMesh
	transformSetSetup: hclTransformSetSetupObject
	perParticlePlanes: hclBonePlanesSetupObjectPerParticlePlane
	globalPlanes: hclBonePlanesSetupObjectGlobalPlane
	perParticleAngle: hclBonePlanesSetupObjectPerParticleAngle
	angleSpecifiedInDegrees: bool