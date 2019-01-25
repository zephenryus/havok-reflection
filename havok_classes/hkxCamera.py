from .hkReferencedObject import hkReferencedObject
from .common import vector4
import struct


class hkxCamera(hkReferencedObject):
    from: vector4
    focus: vector4
    up: vector4
    fov: float
    far: float
    near: float
    leftHanded: bool

    def __init__(self, infile):
        self.from = struct.unpack('>4f', infile.read(16))
        self.focus = struct.unpack('>4f', infile.read(16))
        self.up = struct.unpack('>4f', infile.read(16))
        self.fov = struct.unpack('>f', infile.read(4))
        self.far = struct.unpack('>f', infile.read(4))
        self.near = struct.unpack('>f', infile.read(4))
        self.leftHanded = struct.unpack('>?', infile.read(1))
