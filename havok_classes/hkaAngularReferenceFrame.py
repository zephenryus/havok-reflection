from .hkaParameterizedReferenceFrame import hkaParameterizedReferenceFrame
import struct


class hkaAngularReferenceFrame(hkaParameterizedReferenceFrame):
    topAngle: float
    radius: float

    def __init__(self, infile):
        self.topAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} topAngle={topAngle}, radius={radius}>".format(**{
            "class_name": self.__class__.__name__,
            "topAngle": self.topAngle,
            "radius": self.radius,
        })
