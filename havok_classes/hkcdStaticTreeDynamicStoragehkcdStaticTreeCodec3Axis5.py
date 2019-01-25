from .hkcdStaticTreeCodec3Axis5 import hkcdStaticTreeCodec3Axis5


class hkcdStaticTreeDynamicStoragehkcdStaticTreeCodec3Axis5(object):
    nodes: hkcdStaticTreeCodec3Axis5

    def __init__(self, infile):
        self.nodes = hkcdStaticTreeCodec3Axis5(infile)  # TYPE_ARRAY
