from .hclVertexSelectionInput import hclVertexSelectionInput
from .common import vector4
import struct
from .hclVertexFloatInput import hclVertexFloatInput


class hclBonePlanesSetupObjectGlobalPlane(object):
    transformName: str
    particles: hclVertexSelectionInput
    planeEquationBoneSpace: vector4
    allowedPenetration: hclVertexFloatInput
    stiffness: hclVertexFloatInput

    def __init__(self, infile):
        self.transformName = struct.unpack('>s', infile.read(0))
        self.particles = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.planeEquationBoneSpace = struct.unpack('>4f', infile.read(16))
        self.allowedPenetration = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT
