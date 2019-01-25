from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkxEnvironmentVariable import hkxEnvironmentVariable


class hkxEnvironment(hkReferencedObject):
    variables: List[hkxEnvironmentVariable]

    def __init__(self, infile):
        self.variables = get_array(infile, hkxEnvironmentVariable, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} variables=[{variables}]>".format(**{
            "class_name": self.__class__.__name__,
            "variables": self.variables,
        })
