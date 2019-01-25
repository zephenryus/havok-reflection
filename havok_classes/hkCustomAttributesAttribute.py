from .common import any


class hkCustomAttributesAttribute(object):
    name: str
    value: any

    def __init__(self, infile):
        self.name = str(infile)  # TYPE_CSTRING
        self.value = any(infile)  # TYPE_VARIANT
