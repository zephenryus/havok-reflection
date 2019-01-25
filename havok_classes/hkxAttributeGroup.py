from typing import List
from .common import get_array
from .hkxAttribute import hkxAttribute


class hkxAttributeGroup(object):
    name: str
    attributes: List[hkxAttribute]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.attributes = get_array(infile, hkxAttribute, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} name=\"{name}\", attributes=[{attributes}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "attributes": self.attributes,
        })
