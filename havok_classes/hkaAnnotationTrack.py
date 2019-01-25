from .hkaAnnotationTrackAnnotation import hkaAnnotationTrackAnnotation


class hkaAnnotationTrack(object):
    trackName: str
    annotations: hkaAnnotationTrackAnnotation

    def __init__(self, infile):
        self.trackName = struct.unpack('>s', infile.read(0))
        self.annotations = hkaAnnotationTrackAnnotation(infile)  # TYPE_ARRAY
