from .hkSetUint32 import hkSetUint32


class hkaiNavMeshCutterSavedConnectivity(object):
    storage: hkSetUint32

    def __init__(self, infile):
        self.storage = hkSetUint32(infile)  # TYPE_STRUCT
