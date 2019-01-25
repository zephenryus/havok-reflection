from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
import struct


class hkaFootstepAnalysisInfo(hkReferencedObject):
    name: List[str]
    nameStrike: List[str]
    nameLift: List[str]
    nameLock: List[str]
    nameUnlock: List[str]
    minPos: List[float]
    maxPos: List[float]
    minVel: List[float]
    maxVel: List[float]
    allBonesDown: List[float]
    anyBonesDown: List[float]
    posTol: float
    velTol: float
    duration: float

    def __init__(self, infile):
        self.name = get_array(infile, str, 1)  # TYPE_ARRAY:TYPE_CHAR
        self.nameStrike = get_array(infile, str, 1)  # TYPE_ARRAY:TYPE_CHAR
        self.nameLift = get_array(infile, str, 1)  # TYPE_ARRAY:TYPE_CHAR
        self.nameLock = get_array(infile, str, 1)  # TYPE_ARRAY:TYPE_CHAR
        self.nameUnlock = get_array(infile, str, 1)  # TYPE_ARRAY:TYPE_CHAR
        self.minPos = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.maxPos = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.minVel = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.maxVel = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.allBonesDown = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.anyBonesDown = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.posTol = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.velTol = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.duration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=[{name}], nameStrike=[{nameStrike}], nameLift=[{nameLift}], nameLock=[{nameLock}], nameUnlock=[{nameUnlock}], minPos=[{minPos}], maxPos=[{maxPos}], minVel=[{minVel}], maxVel=[{maxVel}], allBonesDown=[{allBonesDown}], anyBonesDown=[{anyBonesDown}], posTol={posTol}, velTol={velTol}, duration={duration}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "nameStrike": self.nameStrike,
            "nameLift": self.nameLift,
            "nameLock": self.nameLock,
            "nameUnlock": self.nameUnlock,
            "minPos": self.minPos,
            "maxPos": self.maxPos,
            "minVel": self.minVel,
            "maxVel": self.maxVel,
            "allBonesDown": self.allBonesDown,
            "anyBonesDown": self.anyBonesDown,
            "posTol": self.posTol,
            "velTol": self.velTol,
            "duration": self.duration,
        })
