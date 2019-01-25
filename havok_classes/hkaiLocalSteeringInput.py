from .common import vector4, any
import struct


class hkaiLocalSteeringInput(object):
    currentPosition: vector4
    currentForward: vector4
    currentUp: vector4
    currentVelocity: vector4
    desiredVelocity: vector4
    localGoalPlane: vector4
    distToLocalGoal: float
    character: any
    referenceFrame: any
    avoidanceProperties: any
    applyKinematicConstraints: bool
    applyAvoidanceSteering: bool
    enableLocalSteering: bool

    def __init__(self, infile):
        self.currentPosition = struct.unpack('>4f', infile.read(16))
        self.currentForward = struct.unpack('>4f', infile.read(16))
        self.currentUp = struct.unpack('>4f', infile.read(16))
        self.currentVelocity = struct.unpack('>4f', infile.read(16))
        self.desiredVelocity = struct.unpack('>4f', infile.read(16))
        self.localGoalPlane = struct.unpack('>4f', infile.read(16))
        self.distToLocalGoal = struct.unpack('>f', infile.read(4))
        self.character = any(infile)  # TYPE_POINTER
        self.referenceFrame = any(infile)  # TYPE_POINTER
        self.avoidanceProperties = any(infile)  # TYPE_POINTER
        self.applyKinematicConstraints = struct.unpack('>?', infile.read(1))
        self.applyAvoidanceSteering = struct.unpack('>?', infile.read(1))
        self.enableLocalSteering = struct.unpack('>?', infile.read(1))
