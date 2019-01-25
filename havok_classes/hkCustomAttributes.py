from .hkCustomAttributesAttribute import hkCustomAttributesAttribute


class hkCustomAttributes(object):
    attributes: any

    def __init__(self, infile):
        self.attributes = any(infile)  # TYPE_SIMPLEARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} attributes={attributes}>".format(**{
            "class_name": self.__class__.__name__,
            "attributes": self.attributes,
        })
