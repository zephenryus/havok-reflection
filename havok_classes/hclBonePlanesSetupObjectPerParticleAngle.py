from .hclVertexSelectionInput import hclVertexSelectionInput
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
        self.transformName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.particlesMaxAngle = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.particlesMinAngle = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.originBoneSpace = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.axisBoneSpace = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.minAngle = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.maxAngle = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transformName=\"{transformName}\", particlesMaxAngle={particlesMaxAngle}, particlesMinAngle={particlesMinAngle}, originBoneSpace={originBoneSpace}, axisBoneSpace={axisBoneSpace}, minAngle={minAngle}, maxAngle={maxAngle}, stiffness={stiffness}>".format(**{
            "class_name": self.__class__.__name__,
            "transformName": self.transformName,
            "particlesMaxAngle": self.particlesMaxAngle,
            "particlesMinAngle": self.particlesMinAngle,
            "originBoneSpace": self.originBoneSpace,
            "axisBoneSpace": self.axisBoneSpace,
            "minAngle": self.minAngle,
            "maxAngle": self.maxAngle,
            "stiffness": self.stiffness,
        })
