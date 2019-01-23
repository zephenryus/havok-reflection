from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclBonePlanesSetupObjectPerParticlePlane(object):
	transformName: any
	particles: hclVertexSelectionInput
	directionBoneSpace: any
	allowedDistance: hclVertexFloatInput
	stiffness: hclVertexFloatInput
