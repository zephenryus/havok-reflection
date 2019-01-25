from .hclAction import hclAction
from .common import vector4
import struct


class hclSimpleWindAction(hclAction):
    windDirection: vector4
    windMinSpeed: float
    windMaxSpeed: float
    windFrequency: float
    maximumDrag: float
    airVelocity: vector4
    currentTime: float

    def __init__(self, infile):
        self.windDirection = struct.unpack('>4f', infile.read(16))
        self.windMinSpeed = struct.unpack('>f', infile.read(4))
        self.windMaxSpeed = struct.unpack('>f', infile.read(4))
        self.windFrequency = struct.unpack('>f', infile.read(4))
        self.maximumDrag = struct.unpack('>f', infile.read(4))
        self.airVelocity = struct.unpack('>4f', infile.read(16))
        self.currentTime = struct.unpack('>f', infile.read(4))
