import struct


class hkpEntitySpuCollisionCallback(object):
    util: any
    capacity: int
    eventFilter: int
    userFilter: int

    def __init__(self, infile):
        self.util = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.capacity = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.eventFilter = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.userFilter = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} util={util}, capacity={capacity}, eventFilter={eventFilter}, userFilter={userFilter}>".format(**{
            "class_name": self.__class__.__name__,
            "util": self.util,
            "capacity": self.capacity,
            "eventFilter": self.eventFilter,
            "userFilter": self.userFilter,
        })
