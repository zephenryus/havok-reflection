import struct


class hkaiPathPathPoint(object):
    position: vector4
    normal: vector4
    userEdgeData: int
    sectionId: int
    flags: any

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.normal = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.userEdgeData = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.sectionId = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} position={position}, normal={normal}, userEdgeData={userEdgeData}, sectionId={sectionId}, flags={flags}>".format(**{
            "class_name": self.__class__.__name__,
            "position": self.position,
            "normal": self.normal,
            "userEdgeData": self.userEdgeData,
            "sectionId": self.sectionId,
            "flags": self.flags,
        })
