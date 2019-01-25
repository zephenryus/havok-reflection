from .hkaParameterizedReferenceFrame import hkaParameterizedReferenceFrame
import struct


class hkaAngularReferenceFrame(hkaParameterizedReferenceFrame):
    topAngle: float
    radius: float

    def __init__(self, infile):
        self.topAngle = struct.unpack('>f', infile.read(4))
        self.radius = struct.unpack('>f', infile.read(4))
