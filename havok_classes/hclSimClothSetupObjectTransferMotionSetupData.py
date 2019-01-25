from .hclTransformSetSetupObject import hclTransformSetSetupObject
import struct


class hclSimClothSetupObjectTransferMotionSetupData(object):
    transferMotionTransformSetSetup: hclTransformSetSetupObject
    transferMotionTransformName: str
    transferTranslationMotion: bool
    minTranslationSpeed: float
    maxTranslationSpeed: float
    minTranslationBlend: float
    maxTranslationBlend: float
    transferRotationMotion: bool
    minRotationSpeed: float
    maxRotationSpeed: float
    minRotationBlend: float
    maxRotationBlend: float

    def __init__(self, infile):
        self.transferMotionTransformSetSetup = hclTransformSetSetupObject(infile)  # TYPE_POINTER
        self.transferMotionTransformName = struct.unpack('>s', infile.read(0))
        self.transferTranslationMotion = struct.unpack('>?', infile.read(1))
        self.minTranslationSpeed = struct.unpack('>f', infile.read(4))
        self.maxTranslationSpeed = struct.unpack('>f', infile.read(4))
        self.minTranslationBlend = struct.unpack('>f', infile.read(4))
        self.maxTranslationBlend = struct.unpack('>f', infile.read(4))
        self.transferRotationMotion = struct.unpack('>?', infile.read(1))
        self.minRotationSpeed = struct.unpack('>f', infile.read(4))
        self.maxRotationSpeed = struct.unpack('>f', infile.read(4))
        self.minRotationBlend = struct.unpack('>f', infile.read(4))
        self.maxRotationBlend = struct.unpack('>f', infile.read(4))
