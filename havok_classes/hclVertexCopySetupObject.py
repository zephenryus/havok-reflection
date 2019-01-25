from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
import struct


class hclVertexCopySetupObject(hclOperatorSetupObject):
    name: str
    inputBufferSetupObject: any
    outputBufferSetupObject: any
    copyNormals: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.inputBufferSetupObject = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.outputBufferSetupObject = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.copyNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", inputBufferSetupObject={inputBufferSetupObject}, outputBufferSetupObject={outputBufferSetupObject}, copyNormals={copyNormals}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "inputBufferSetupObject": self.inputBufferSetupObject,
            "outputBufferSetupObject": self.outputBufferSetupObject,
            "copyNormals": self.copyNormals,
        })
