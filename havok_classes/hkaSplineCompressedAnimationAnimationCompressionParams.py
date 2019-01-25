import struct


class hkaSplineCompressedAnimationAnimationCompressionParams(object):
    maxFramesPerBlock: int
    enableSampleSingleTracks: bool

    def __init__(self, infile):
        self.maxFramesPerBlock = struct.unpack('>H', infile.read(2))
        self.enableSampleSingleTracks = struct.unpack('>?', infile.read(1))
