import struct


class hclSimClothDataTransferMotionData(object):
    transformSetIndex: int
    transformIndex: int
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
        self.transformSetIndex = struct.unpack('>I', infile.read(4))
        self.transformIndex = struct.unpack('>I', infile.read(4))
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
