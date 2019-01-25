from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
import struct


class hclUpdateVertexFramesSetupObject(hclOperatorSetupObject):
    name: str
    buffer: any
    vertexSelection: hclVertexSelectionInput
    updateNormals: bool
    updateTangents: bool
    updateBiTangents: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.buffer = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.updateNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.updateTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.updateBiTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", buffer={buffer}, vertexSelection={vertexSelection}, updateNormals={updateNormals}, updateTangents={updateTangents}, updateBiTangents={updateBiTangents}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "buffer": self.buffer,
            "vertexSelection": self.vertexSelection,
            "updateNormals": self.updateNormals,
            "updateTangents": self.updateTangents,
            "updateBiTangents": self.updateBiTangents,
        })
