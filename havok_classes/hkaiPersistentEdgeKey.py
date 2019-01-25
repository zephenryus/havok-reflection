from .hkaiPersistentFaceKey import hkaiPersistentFaceKey
import struct


class hkaiPersistentEdgeKey(object):
    faceKey: hkaiPersistentFaceKey
    edgeOffset: int

    def __init__(self, infile):
        self.faceKey = hkaiPersistentFaceKey(infile)  # TYPE_STRUCT
        self.edgeOffset = struct.unpack('>h', infile.read(2))
