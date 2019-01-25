from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
import struct


class hclBlendSetupObject(hclOperatorSetupObject):
    name: str
    A: any
    B: any
    C: any
    vertexSelection: hclVertexSelectionInput
    blendWeights: hclVertexFloatInput
    mapToScurve: bool
    blendNormals: bool
    blendTangents: bool
    blendBitangents: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.A = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.B = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.C = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.blendWeights = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.mapToScurve = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.blendNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.blendTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.blendBitangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", A={A}, B={B}, C={C}, vertexSelection={vertexSelection}, blendWeights={blendWeights}, mapToScurve={mapToScurve}, blendNormals={blendNormals}, blendTangents={blendTangents}, blendBitangents={blendBitangents}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "A": self.A,
            "B": self.B,
            "C": self.C,
            "vertexSelection": self.vertexSelection,
            "blendWeights": self.blendWeights,
            "mapToScurve": self.mapToScurve,
            "blendNormals": self.blendNormals,
            "blendTangents": self.blendTangents,
            "blendBitangents": self.blendBitangents,
        })
