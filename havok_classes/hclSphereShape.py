from .hclShape import hclShape
from .hkSphere import hkSphere


class hclSphereShape(hclShape):
    sphere: hkSphere

    def __init__(self, infile):
        self.sphere = hkSphere(infile)  # TYPE_STRUCT
