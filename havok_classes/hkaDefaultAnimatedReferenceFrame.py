from .hkaAnimatedReferenceFrame import hkaAnimatedReferenceFrame
from .common import vector4, any


class hkaDefaultAnimatedReferenceFrame(hkaAnimatedReferenceFrame):
    up: vector4
    forward: vector4
    duration: float
    referenceFrameSamples: any
