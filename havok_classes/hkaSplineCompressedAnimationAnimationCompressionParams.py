import struct


class hkaSplineCompressedAnimationAnimationCompressionParams(object):
    maxFramesPerBlock: int
    enableSampleSingleTracks: bool

    def __init__(self, infile):
        self.maxFramesPerBlock = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.enableSampleSingleTracks = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} maxFramesPerBlock={maxFramesPerBlock}, enableSampleSingleTracks={enableSampleSingleTracks}>".format(**{
            "class_name": self.__class__.__name__,
            "maxFramesPerBlock": self.maxFramesPerBlock,
            "enableSampleSingleTracks": self.enableSampleSingleTracks,
        })
