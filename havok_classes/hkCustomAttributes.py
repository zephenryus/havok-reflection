from .hkCustomAttributesAttribute import hkCustomAttributesAttribute


class hkCustomAttributes(object):
    attributes: hkCustomAttributesAttribute

    def __init__(self, infile):
        self.attributes = hkCustomAttributesAttribute(infile)  # TYPE_SIMPLEARRAY
