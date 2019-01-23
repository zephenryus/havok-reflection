from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclBonePlanesSetupObjectPerParticleAngle(object):
	transformName: any
	particlesMaxAngle: hclVertexSelectionInput
	particlesMinAngle: hclVertexSelectionInput
	originBoneSpace: any
	axisBoneSpace: any
	minAngle: hclVertexFloatInput
	maxAngle: hclVertexFloatInput
	stiffness: hclVertexFloatInput
