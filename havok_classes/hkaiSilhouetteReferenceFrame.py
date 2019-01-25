from .common import vector4
import struct


class hkaiSilhouetteReferenceFrame(object):
    up: vector4
    referenceAxis: vector4
    orthogonalAxis: vector4

    def __init__(self, infile):
        self.up = struct.unpack('>4f', infile.read(16))
        self.referenceAxis = struct.unpack('>4f', infile.read(16))
        self.orthogonalAxis = struct.unpack('>4f', infile.read(16))
