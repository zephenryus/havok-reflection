from .hkReferencedObject import hkReferencedObject
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
        self.from = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.focus = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.fov = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.far = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.near = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.leftHanded = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} from={from}, focus={focus}, up={up}, fov={fov}, far={far}, near={near}, leftHanded={leftHanded}>".format(**{
            "class_name": self.__class__.__name__,
            "from": self.from,
            "focus": self.focus,
            "up": self.up,
            "fov": self.fov,
            "far": self.far,
            "near": self.near,
            "leftHanded": self.leftHanded,
        })
