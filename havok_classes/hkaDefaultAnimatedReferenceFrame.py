from .hkaAnimatedReferenceFrame import hkaAnimatedReferenceFrame
import struct
from typing import List
from .common import get_array


class hkaDefaultAnimatedReferenceFrame(hkaAnimatedReferenceFrame):
    up: vector4
    forward: vector4
    duration: float
    referenceFrameSamples: List[vector4]

    def __init__(self, infile):
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.forward = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.duration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.referenceFrameSamples = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4

    def __repr__(self):
        return "<{class_name} up={up}, forward={forward}, duration={duration}, referenceFrameSamples=[{referenceFrameSamples}]>".format(**{
            "class_name": self.__class__.__name__,
            "up": self.up,
            "forward": self.forward,
            "duration": self.duration,
            "referenceFrameSamples": self.referenceFrameSamples,
        })
