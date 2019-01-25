from .common import vector4
import struct


class hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection(object):
    a: vector4
    b: vector4

    def __init__(self, infile):
        self.a = struct.unpack('>4f', infile.read(16))
        self.b = struct.unpack('>4f', infile.read(16))
