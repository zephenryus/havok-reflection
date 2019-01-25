from .hkpBinaryAction import hkpBinaryAction
import struct


class hkpSpringAction(hkpBinaryAction):
    lastForce: vector4
    positionAinA: vector4
    positionBinB: vector4
    restLength: float
    strength: float
    damping: float
    onCompression: bool
    onExtension: bool

    def __init__(self, infile):
        self.lastForce = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.positionAinA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.positionBinB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.restLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.strength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.damping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.onCompression = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.onExtension = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} lastForce={lastForce}, positionAinA={positionAinA}, positionBinB={positionBinB}, restLength={restLength}, strength={strength}, damping={damping}, onCompression={onCompression}, onExtension={onExtension}>".format(**{
            "class_name": self.__class__.__name__,
            "lastForce": self.lastForce,
            "positionAinA": self.positionAinA,
            "positionBinB": self.positionBinB,
            "restLength": self.restLength,
            "strength": self.strength,
            "damping": self.damping,
            "onCompression": self.onCompression,
            "onExtension": self.onExtension,
        })
