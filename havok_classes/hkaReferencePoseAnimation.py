from .hkaAnimation import hkaAnimation
from .hkaSkeleton import hkaSkeleton


class hkaReferencePoseAnimation(hkaAnimation):
    skeleton: any

    def __init__(self, infile):
        self.skeleton = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} skeleton={skeleton}>".format(**{
            "class_name": self.__class__.__name__,
            "skeleton": self.skeleton,
        })
