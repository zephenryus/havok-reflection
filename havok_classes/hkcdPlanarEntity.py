from .hkReferencedObject import hkReferencedObject


class hkcdPlanarEntity(hkReferencedObject):
    debugger: any

    def __init__(self, infile):
        self.debugger = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} debugger={debugger}>".format(**{
            "class_name": self.__class__.__name__,
            "debugger": self.debugger,
        })
