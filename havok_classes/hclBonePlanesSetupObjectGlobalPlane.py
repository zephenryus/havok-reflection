from .hclVertexSelectionInput import hclVertexSelectionInput
from .common import vector4
from .hclVertexFloatInput import hclVertexFloatInput


class hclBonePlanesSetupObjectGlobalPlane(object):
    transformName: str
    particles: hclVertexSelectionInput
    planeEquationBoneSpace: vector4
    allowedPenetration: hclVertexFloatInput
    stiffness: hclVertexFloatInput
