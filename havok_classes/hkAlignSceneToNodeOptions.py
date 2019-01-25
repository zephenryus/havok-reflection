from .hkReferencedObject import hkReferencedObject
import struct


class hkAlignSceneToNodeOptions(hkReferencedObject):
    invert: bool
    transformPositionX: bool
    transformPositionY: bool
    transformPositionZ: bool
    transformRotation: bool
    transformScale: bool
    transformSkew: bool
    keyframe: int
    nodeName: str

    def __init__(self, infile):
        self.invert = struct.unpack('>?', infile.read(1))
        self.transformPositionX = struct.unpack('>?', infile.read(1))
        self.transformPositionY = struct.unpack('>?', infile.read(1))
        self.transformPositionZ = struct.unpack('>?', infile.read(1))
        self.transformRotation = struct.unpack('>?', infile.read(1))
        self.transformScale = struct.unpack('>?', infile.read(1))
        self.transformSkew = struct.unpack('>?', infile.read(1))
        self.keyframe = struct.unpack('>i', infile.read(4))
        self.nodeName = struct.unpack('>s', infile.read(0))
