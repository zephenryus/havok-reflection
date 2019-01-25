from .hkaiPersistentFaceKey import hkaiPersistentFaceKey
import struct


class hkaiPersistentEdgeKey(object):
    faceKey: hkaiPersistentFaceKey
    edgeOffset: int

    def __init__(self, infile):
        self.faceKey = hkaiPersistentFaceKey(infile)  # TYPE_STRUCT:TYPE_VOID
        self.edgeOffset = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} faceKey={faceKey}, edgeOffset={edgeOffset}>".format(**{
            "class_name": self.__class__.__name__,
            "faceKey": self.faceKey,
            "edgeOffset": self.edgeOffset,
        })
