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
        self.invert = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transformPositionX = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transformPositionY = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transformPositionZ = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transformRotation = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transformScale = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transformSkew = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.keyframe = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.nodeName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} invert={invert}, transformPositionX={transformPositionX}, transformPositionY={transformPositionY}, transformPositionZ={transformPositionZ}, transformRotation={transformRotation}, transformScale={transformScale}, transformSkew={transformSkew}, keyframe={keyframe}, nodeName=\"{nodeName}\">".format(**{
            "class_name": self.__class__.__name__,
            "invert": self.invert,
            "transformPositionX": self.transformPositionX,
            "transformPositionY": self.transformPositionY,
            "transformPositionZ": self.transformPositionZ,
            "transformRotation": self.transformRotation,
            "transformScale": self.transformScale,
            "transformSkew": self.transformSkew,
            "keyframe": self.keyframe,
            "nodeName": self.nodeName,
        })
