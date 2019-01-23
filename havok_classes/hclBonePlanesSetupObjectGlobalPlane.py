from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclBonePlanesSetupObjectGlobalPlane(object):
	transformName: any
	particles: hclVertexSelectionInput
	planeEquationBoneSpace: any
	allowedPenetration: hclVertexFloatInput
	stiffness: hclVertexFloatInput
