import struct


class hkFloat16(object):
    value: int

    def __init__(self, infile):
        self.value = struct.unpack('>H', infile.read(2))
