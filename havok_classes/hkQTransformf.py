from .common import any, vector4
import struct


class hkQTransformf(object):
    rotation: any
    translation: vector4

    def __init__(self, infile):
        self.rotation = any(infile)  # TYPE_QUATERNION
        self.translation = struct.unpack('>4f', infile.read(16))
