from .hkReferencedObject import hkReferencedObject


class hkpRejectChassisListener(hkReferencedObject):
    chassis: any

    def __init__(self, infile):
        self.chassis = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} chassis={chassis}>".format(**{
            "class_name": self.__class__.__name__,
            "chassis": self.chassis,
        })
