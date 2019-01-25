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
        self.parent = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.left = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.right = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.nextFreeNodeId = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.planeId = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.aabbId = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.material = struct.unpack('>Q', infile.read(8))  # TYPE_UINT64:TYPE_VOID
        self.data = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.type = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.flags = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} parent={parent}, left={left}, right={right}, nextFreeNodeId={nextFreeNodeId}, planeId={planeId}, aabbId={aabbId}, material={material}, data={data}, type={type}, flags={flags}>".format(**{
            "class_name": self.__class__.__name__,
            "parent": self.parent,
            "left": self.left,
            "right": self.right,
            "nextFreeNodeId": self.nextFreeNodeId,
            "planeId": self.planeId,
            "aabbId": self.aabbId,
            "material": self.material,
            "data": self.data,
            "type": self.type,
            "flags": self.flags,
        })
