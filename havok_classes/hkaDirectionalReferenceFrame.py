from .hkaParameterizedReferenceFrame import hkaParameterizedReferenceFrame
from .common import vector4
import struct


class hkaDirectionalReferenceFrame(hkaParameterizedReferenceFrame):
    movementDir: vector4

    def __init__(self, infile):
        self.movementDir = struct.unpack('>4f', infile.read(16))
