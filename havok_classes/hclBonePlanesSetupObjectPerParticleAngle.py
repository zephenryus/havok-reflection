from .hclVertexSelectionInput import hclVertexSelectionInput
from .common import vector4
from .hclVertexFloatInput import hclVertexFloatInput


class hclBonePlanesSetupObjectPerParticleAngle(object):
    transformName: str
    particlesMaxAngle: hclVertexSelectionInput
    particlesMinAngle: hclVertexSelectionInput
    originBoneSpace: vector4
    axisBoneSpace: vector4
    minAngle: hclVertexFloatInput
    maxAngle: hclVertexFloatInput
    stiffness: hclVertexFloatInput
