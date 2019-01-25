from .hclAction import hclAction
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
        self.windDirection = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.windMinSpeed = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.windMaxSpeed = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.windFrequency = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maximumDrag = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.airVelocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.currentTime = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} windDirection={windDirection}, windMinSpeed={windMinSpeed}, windMaxSpeed={windMaxSpeed}, windFrequency={windFrequency}, maximumDrag={maximumDrag}, airVelocity={airVelocity}, currentTime={currentTime}>".format(**{
            "class_name": self.__class__.__name__,
            "windDirection": self.windDirection,
            "windMinSpeed": self.windMinSpeed,
            "windMaxSpeed": self.windMaxSpeed,
            "windFrequency": self.windFrequency,
            "maximumDrag": self.maximumDrag,
            "airVelocity": self.airVelocity,
            "currentTime": self.currentTime,
        })
