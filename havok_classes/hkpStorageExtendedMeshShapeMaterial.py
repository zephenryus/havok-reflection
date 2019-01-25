from .hkpMeshMaterial import hkpMeshMaterial
import struct


class hkpStorageExtendedMeshShapeMaterial(hkpMeshMaterial):
    restitution: int
    friction: int
    userData: int

    def __init__(self, infile):
        self.restitution = struct.unpack('>h', infile.read(2))
        self.friction = struct.unpack('>h', infile.read(2))
        self.userData = struct.unpack('>L', infile.read(8))
