from .hkaParameterizedReferenceFrame import hkaParameterizedReferenceFrame
import struct


class hkaDirectionalReferenceFrame(hkaParameterizedReferenceFrame):
    movementDir: vector4

    def __init__(self, infile):
        self.movementDir = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} movementDir={movementDir}>".format(**{
            "class_name": self.__class__.__name__,
            "movementDir": self.movementDir,
        })
