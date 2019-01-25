import struct


class hkAabbUint32(object):
    min: int
    expansionMin: int
    expansionShift: int
    max: int
    expansionMax: int
    shapeKeyByte: int

    def __init__(self, infile):
        self.min = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.expansionMin = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.expansionShift = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.max = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.expansionMax = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.shapeKeyByte = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} min={min}, expansionMin={expansionMin}, expansionShift={expansionShift}, max={max}, expansionMax={expansionMax}, shapeKeyByte={shapeKeyByte}>".format(**{
            "class_name": self.__class__.__name__,
            "min": self.min,
            "expansionMin": self.expansionMin,
            "expansionShift": self.expansionShift,
            "max": self.max,
            "expansionMax": self.expansionMax,
            "shapeKeyByte": self.shapeKeyByte,
        })
