import struct


class hkAabb16(object):
    min: int
    key: int
    max: int
    key1: int

    def __init__(self, infile):
        self.min = struct.unpack('>H', infile.read(2))
        self.key = struct.unpack('>H', infile.read(2))
        self.max = struct.unpack('>H', infile.read(2))
        self.key1 = struct.unpack('>H', infile.read(2))
