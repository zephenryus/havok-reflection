from .common import any, vector4
import struct


class hkaiReferenceFrame(object):
    transform: any
    linearVelocity: vector4
    angularVelocity: vector4

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_TRANSFORM
        self.linearVelocity = struct.unpack('>4f', infile.read(16))
        self.angularVelocity = struct.unpack('>4f', infile.read(16))
