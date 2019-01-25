from .hclShape import hclShape
from .hkSphere import hkSphere


class hclSphereShape(hclShape):
    sphere: hkSphere

    def __init__(self, infile):
        self.sphere = hkSphere(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} sphere={sphere}>".format(**{
            "class_name": self.__class__.__name__,
            "sphere": self.sphere,
        })
