from .hkaAnimatedReferenceFrame import hkaAnimatedReferenceFrame
from .common import vector4, any
import struct


class hkaDefaultAnimatedReferenceFrame(hkaAnimatedReferenceFrame):
    up: vector4
    forward: vector4
    duration: float
    referenceFrameSamples: any

    def __init__(self, infile):
        self.up = struct.unpack('>4f', infile.read(16))
        self.forward = struct.unpack('>4f', infile.read(16))
        self.duration = struct.unpack('>f', infile.read(4))
        self.referenceFrameSamples = any(infile)  # TYPE_ARRAY
