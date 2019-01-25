from .hkSetUint32 import hkSetUint32


class hkaiNavMeshCutterSavedConnectivity(object):
    storage: hkSetUint32

    def __init__(self, infile):
        self.storage = hkSetUint32(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} storage={storage}>".format(**{
            "class_name": self.__class__.__name__,
            "storage": self.storage,
        })
