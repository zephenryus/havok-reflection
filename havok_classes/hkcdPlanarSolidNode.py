import struct


class hkcdPlanarSolidNode(object):
    parent: int
    left: int
    right: int
    nextFreeNodeId: int
    planeId: int
    aabbId: int
    material: int
    data: int
    type: int
    flags: int

    def __init__(self, infile):
        self.parent = struct.unpack('>I', infile.read(4))
        self.left = struct.unpack('>I', infile.read(4))
        self.right = struct.unpack('>I', infile.read(4))
        self.nextFreeNodeId = struct.unpack('>I', infile.read(4))
        self.planeId = struct.unpack('>I', infile.read(4))
        self.aabbId = struct.unpack('>I', infile.read(4))
        self.material = struct.unpack('>Q', infile.read(8))
        self.data = struct.unpack('>I', infile.read(4))
        self.type = struct.unpack('>H', infile.read(2))
        self.flags = struct.unpack('>H', infile.read(2))
