from .hkpMeshMaterial import hkpMeshMaterial
import struct


class hkpStorageExtendedMeshShapeMaterial(hkpMeshMaterial):
    restitution: int
    friction: int
    userData: int

    def __init__(self, infile):
        self.restitution = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.friction = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} restitution={restitution}, friction={friction}, userData={userData}>".format(**{
            "class_name": self.__class__.__name__,
            "restitution": self.restitution,
            "friction": self.friction,
            "userData": self.userData,
        })
