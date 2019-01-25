import struct


class hkpCompressedMeshShapeBigTriangle(object):
    a: int
    b: int
    c: int
    material: int
    weldingInfo: int
    transformIndex: int

    def __init__(self, infile):
        self.a = struct.unpack('>H', infile.read(2))
        self.b = struct.unpack('>H', infile.read(2))
        self.c = struct.unpack('>H', infile.read(2))
        self.material = struct.unpack('>I', infile.read(4))
        self.weldingInfo = struct.unpack('>H', infile.read(2))
        self.transformIndex = struct.unpack('>H', infile.read(2))
