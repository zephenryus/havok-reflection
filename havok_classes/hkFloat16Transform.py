from .hkFloat16 import hkFloat16


class hkFloat16Transform(object):
    elements: hkFloat16

    def __init__(self, infile):
        self.elements = hkFloat16(infile)  # TYPE_STRUCT
