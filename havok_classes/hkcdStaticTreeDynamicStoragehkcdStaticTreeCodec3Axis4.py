from .hkcdStaticTreeCodec3Axis4 import hkcdStaticTreeCodec3Axis4


class hkcdStaticTreeDynamicStoragehkcdStaticTreeCodec3Axis4(object):
    nodes: hkcdStaticTreeCodec3Axis4

    def __init__(self, infile):
        self.nodes = hkcdStaticTreeCodec3Axis4(infile)  # TYPE_ARRAY
