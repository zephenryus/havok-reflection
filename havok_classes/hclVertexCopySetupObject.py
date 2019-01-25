from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
import struct


class hclVertexCopySetupObject(hclOperatorSetupObject):
    name: str
    inputBufferSetupObject: hclBufferSetupObject
    outputBufferSetupObject: hclBufferSetupObject
    copyNormals: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.inputBufferSetupObject = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.outputBufferSetupObject = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.copyNormals = struct.unpack('>?', infile.read(1))
