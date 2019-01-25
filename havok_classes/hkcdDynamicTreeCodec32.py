from .hkAabb import hkAabb


class hkcdDynamicTreeCodec32(object):
    aabb: hkAabb

    def __init__(self, infile):
        self.aabb = hkAabb(infile)  # TYPE_STRUCT
