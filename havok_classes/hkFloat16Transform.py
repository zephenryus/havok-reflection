from .hkFloat16 import hkFloat16


class hkFloat16Transform(object):
    elements: hkFloat16

    def __init__(self, infile):
        self.elements = hkFloat16(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} elements={elements}>".format(**{
            "class_name": self.__class__.__name__,
            "elements": self.elements,
        })
