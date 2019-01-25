from .hkpRigidBody import hkpRigidBody
from .common import any


class hkpSerializedDisplayRbTransformsDisplayTransformPair(object):
    rb: hkpRigidBody
    localToDisplay: any

    def __init__(self, infile):
        self.rb = hkpRigidBody(infile)  # TYPE_POINTER
        self.localToDisplay = any(infile)  # TYPE_TRANSFORM
