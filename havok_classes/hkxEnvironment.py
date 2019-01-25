from .hkReferencedObject import hkReferencedObject
from .hkxEnvironmentVariable import hkxEnvironmentVariable


class hkxEnvironment(hkReferencedObject):
    variables: hkxEnvironmentVariable

    def __init__(self, infile):
        self.variables = hkxEnvironmentVariable(infile)  # TYPE_ARRAY
