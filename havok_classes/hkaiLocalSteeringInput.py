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
        self.currentPosition = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.currentForward = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.currentUp = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.currentVelocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.desiredVelocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.localGoalPlane = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.distToLocalGoal = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.character = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.referenceFrame = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.avoidanceProperties = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.applyKinematicConstraints = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.applyAvoidanceSteering = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.enableLocalSteering = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} currentPosition={currentPosition}, currentForward={currentForward}, currentUp={currentUp}, currentVelocity={currentVelocity}, desiredVelocity={desiredVelocity}, localGoalPlane={localGoalPlane}, distToLocalGoal={distToLocalGoal}, character={character}, referenceFrame={referenceFrame}, avoidanceProperties={avoidanceProperties}, applyKinematicConstraints={applyKinematicConstraints}, applyAvoidanceSteering={applyAvoidanceSteering}, enableLocalSteering={enableLocalSteering}>".format(**{
            "class_name": self.__class__.__name__,
            "currentPosition": self.currentPosition,
            "currentForward": self.currentForward,
            "currentUp": self.currentUp,
            "currentVelocity": self.currentVelocity,
            "desiredVelocity": self.desiredVelocity,
            "localGoalPlane": self.localGoalPlane,
            "distToLocalGoal": self.distToLocalGoal,
            "character": self.character,
            "referenceFrame": self.referenceFrame,
            "avoidanceProperties": self.avoidanceProperties,
            "applyKinematicConstraints": self.applyKinematicConstraints,
            "applyAvoidanceSteering": self.applyAvoidanceSteering,
            "enableLocalSteering": self.enableLocalSteering,
        })
