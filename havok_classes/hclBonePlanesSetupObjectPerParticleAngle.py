from .hclVertexSelectionInput import hclVertexSelectionInput
from .common import vector4
import struct
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

    def __init__(self, infile):
        self.transformName = struct.unpack('>s', infile.read(0))
        self.particlesMaxAngle = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.particlesMinAngle = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.originBoneSpace = struct.unpack('>4f', infile.read(16))
        self.axisBoneSpace = struct.unpack('>4f', infile.read(16))
        self.minAngle = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.maxAngle = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT
