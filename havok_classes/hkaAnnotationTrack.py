from typing import List
from .common import get_array
from .hkaAnnotationTrackAnnotation import hkaAnnotationTrackAnnotation


class hkaAnnotationTrack(object):
    trackName: str
    annotations: List[hkaAnnotationTrackAnnotation]

    def __init__(self, infile):
        self.trackName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.annotations = get_array(infile, hkaAnnotationTrackAnnotation, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} trackName=\"{trackName}\", annotations=[{annotations}]>".format(**{
            "class_name": self.__class__.__name__,
            "trackName": self.trackName,
            "annotations": self.annotations,
        })
