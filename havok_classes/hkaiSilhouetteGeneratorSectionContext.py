from .hkQTransform import hkQTransform
from .hkaiSilhouetteGenerator import hkaiSilhouetteGenerator
import struct


class hkaiSilhouetteGeneratorSectionContext(object):
    lastRelativeTransform: hkQTransform
    generator: any
    generatorSize: int
    generatedLastFrame: bool
    generatingThisFrame: bool

    def __init__(self, infile):
        self.lastRelativeTransform = hkQTransform(infile)  # TYPE_STRUCT:TYPE_VOID
        self.generator = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.generatorSize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.generatedLastFrame = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.generatingThisFrame = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} lastRelativeTransform={lastRelativeTransform}, generator={generator}, generatorSize={generatorSize}, generatedLastFrame={generatedLastFrame}, generatingThisFrame={generatingThisFrame}>".format(**{
            "class_name": self.__class__.__name__,
            "lastRelativeTransform": self.lastRelativeTransform,
            "generator": self.generator,
            "generatorSize": self.generatorSize,
            "generatedLastFrame": self.generatedLastFrame,
            "generatingThisFrame": self.generatingThisFrame,
        })
