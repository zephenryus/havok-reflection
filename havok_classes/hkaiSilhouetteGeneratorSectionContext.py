from .hkQTransform import hkQTransform
from .hkaiSilhouetteGenerator import hkaiSilhouetteGenerator
import struct


class hkaiSilhouetteGeneratorSectionContext(object):
    lastRelativeTransform: hkQTransform
    generator: hkaiSilhouetteGenerator
    generatorSize: int
    generatedLastFrame: bool
    generatingThisFrame: bool

    def __init__(self, infile):
        self.lastRelativeTransform = hkQTransform(infile)  # TYPE_STRUCT
        self.generator = hkaiSilhouetteGenerator(infile)  # TYPE_POINTER
        self.generatorSize = struct.unpack('>i', infile.read(4))
        self.generatedLastFrame = struct.unpack('>?', infile.read(1))
        self.generatingThisFrame = struct.unpack('>?', infile.read(1))
