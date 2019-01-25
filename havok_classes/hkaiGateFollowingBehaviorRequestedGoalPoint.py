from .common import vector4
import struct


class hkaiGateFollowingBehaviorRequestedGoalPoint(object):
    position: vector4
    sectionId: int

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))
        self.sectionId = struct.unpack('>i', infile.read(4))
