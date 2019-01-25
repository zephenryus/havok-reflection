from .hkxAttribute import hkxAttribute


class hkxAttributeGroup(object):
    name: str
    attributes: hkxAttribute

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.attributes = hkxAttribute(infile)  # TYPE_ARRAY
