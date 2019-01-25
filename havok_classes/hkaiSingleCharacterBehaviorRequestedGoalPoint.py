import struct


class hkaiSingleCharacterBehaviorRequestedGoalPoint(object):
    position: vector4
    sectionId: int

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.sectionId = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} position={position}, sectionId={sectionId}>".format(**{
            "class_name": self.__class__.__name__,
            "position": self.position,
            "sectionId": self.sectionId,
        })
