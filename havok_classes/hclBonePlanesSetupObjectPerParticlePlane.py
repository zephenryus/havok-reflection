from .hclVertexSelectionInput import hclVertexSelectionInput
from .common import vector4
from .hclVertexFloatInput import hclVertexFloatInput


class hclBonePlanesSetupObjectPerParticlePlane(object):
    transformName: str
    particles: hclVertexSelectionInput
    directionBoneSpace: vector4
    allowedDistance: hclVertexFloatInput
    stiffness: hclVertexFloatInput
