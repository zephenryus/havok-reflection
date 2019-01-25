import struct


class hkTraceStreamTitle(object):
    value: str

    def __init__(self, infile):
        self.value = struct.unpack('>c', infile.read(1))
