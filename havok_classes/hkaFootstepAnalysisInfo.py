from .hkReferencedObject import hkReferencedObject
from .common import any
import struct


class hkaFootstepAnalysisInfo(hkReferencedObject):
    name: any
    nameStrike: any
    nameLift: any
    nameLock: any
    nameUnlock: any
    minPos: any
    maxPos: any
    minVel: any
    maxVel: any
    allBonesDown: any
    anyBonesDown: any
    posTol: float
    velTol: float
    duration: float

    def __init__(self, infile):
        self.name = any(infile)  # TYPE_ARRAY
        self.nameStrike = any(infile)  # TYPE_ARRAY
        self.nameLift = any(infile)  # TYPE_ARRAY
        self.nameLock = any(infile)  # TYPE_ARRAY
        self.nameUnlock = any(infile)  # TYPE_ARRAY
        self.minPos = any(infile)  # TYPE_ARRAY
        self.maxPos = any(infile)  # TYPE_ARRAY
        self.minVel = any(infile)  # TYPE_ARRAY
        self.maxVel = any(infile)  # TYPE_ARRAY
        self.allBonesDown = any(infile)  # TYPE_ARRAY
        self.anyBonesDown = any(infile)  # TYPE_ARRAY
        self.posTol = struct.unpack('>f', infile.read(4))
        self.velTol = struct.unpack('>f', infile.read(4))
        self.duration = struct.unpack('>f', infile.read(4))
