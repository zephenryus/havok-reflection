from .hclVertexSelectionInput import hclVertexSelectionInput
from .common import vector4
import struct
from .hclVertexFloatInput import hclVertexFloatInput


class hclBonePlanesSetupObjectPerParticlePlane(object):
    transformName: str
    particles: hclVertexSelectionInput
    directionBoneSpace: vector4
    allowedDistance: hclVertexFloatInput
    stiffness: hclVertexFloatInput

    def __init__(self, infile):
        self.transformName = struct.unpack('>s', infile.read(0))
        self.particles = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.directionBoneSpace = struct.unpack('>4f', infile.read(16))
        self.allowedDistance = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT
