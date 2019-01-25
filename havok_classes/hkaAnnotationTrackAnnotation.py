import struct


class hkaAnnotationTrackAnnotation(object):
    time: float
    text: str

    def __init__(self, infile):
        self.time = struct.unpack('>f', infile.read(4))
        self.text = struct.unpack('>s', infile.read(0))
