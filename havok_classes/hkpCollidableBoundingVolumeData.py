import struct


class hkpCollidableBoundingVolumeData(object):
    min: int
    expansionMin: int
    expansionShift: int
    max: int
    expansionMax: int
    padding: int
    numChildShapeAabbs: int
    capacityChildShapeAabbs: int
    childShapeAabbs: any
    childShapeKeys: any

    def __init__(self, infile):
        self.min = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.expansionMin = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.expansionShift = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.max = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.expansionMax = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.numChildShapeAabbs = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.capacityChildShapeAabbs = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.childShapeAabbs = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.childShapeKeys = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} min={min}, expansionMin={expansionMin}, expansionShift={expansionShift}, max={max}, expansionMax={expansionMax}, padding={padding}, numChildShapeAabbs={numChildShapeAabbs}, capacityChildShapeAabbs={capacityChildShapeAabbs}, childShapeAabbs={childShapeAabbs}, childShapeKeys={childShapeKeys}>".format(**{
            "class_name": self.__class__.__name__,
            "min": self.min,
            "expansionMin": self.expansionMin,
            "expansionShift": self.expansionShift,
            "max": self.max,
            "expansionMax": self.expansionMax,
            "padding": self.padding,
            "numChildShapeAabbs": self.numChildShapeAabbs,
            "capacityChildShapeAabbs": self.capacityChildShapeAabbs,
            "childShapeAabbs": self.childShapeAabbs,
            "childShapeKeys": self.childShapeKeys,
        })
