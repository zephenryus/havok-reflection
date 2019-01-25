from .hkaAnimation import hkaAnimation
from .hkaSkeleton import hkaSkeleton


class hkaReferencePoseAnimation(hkaAnimation):
    skeleton: hkaSkeleton

    def __init__(self, infile):
        self.skeleton = hkaSkeleton(infile)  # TYPE_POINTER
