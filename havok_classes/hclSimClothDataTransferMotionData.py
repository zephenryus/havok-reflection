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
        self.transformSetIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.transformIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.transferTranslationMotion = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.minTranslationSpeed = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxTranslationSpeed = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minTranslationBlend = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxTranslationBlend = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.transferRotationMotion = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.minRotationSpeed = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxRotationSpeed = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minRotationBlend = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxRotationBlend = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transformSetIndex={transformSetIndex}, transformIndex={transformIndex}, transferTranslationMotion={transferTranslationMotion}, minTranslationSpeed={minTranslationSpeed}, maxTranslationSpeed={maxTranslationSpeed}, minTranslationBlend={minTranslationBlend}, maxTranslationBlend={maxTranslationBlend}, transferRotationMotion={transferRotationMotion}, minRotationSpeed={minRotationSpeed}, maxRotationSpeed={maxRotationSpeed}, minRotationBlend={minRotationBlend}, maxRotationBlend={maxRotationBlend}>".format(**{
            "class_name": self.__class__.__name__,
            "transformSetIndex": self.transformSetIndex,
            "transformIndex": self.transformIndex,
            "transferTranslationMotion": self.transferTranslationMotion,
            "minTranslationSpeed": self.minTranslationSpeed,
            "maxTranslationSpeed": self.maxTranslationSpeed,
            "minTranslationBlend": self.minTranslationBlend,
            "maxTranslationBlend": self.maxTranslationBlend,
            "transferRotationMotion": self.transferRotationMotion,
            "minRotationSpeed": self.minRotationSpeed,
            "maxRotationSpeed": self.maxRotationSpeed,
            "minRotationBlend": self.minRotationBlend,
            "maxRotationBlend": self.maxRotationBlend,
        })
