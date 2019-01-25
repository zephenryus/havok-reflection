from .hkReferencedObject import hkReferencedObject
import struct


class hkpAction(hkReferencedObject):
    world: any
    island: any
    userData: int
    name: str

    def __init__(self, infile):
        self.world = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.island = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} world={world}, island={island}, userData={userData}, name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "world": self.world,
            "island": self.island,
            "userData": self.userData,
            "name": self.name,
        })
