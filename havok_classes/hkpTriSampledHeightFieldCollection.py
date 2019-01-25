from .hkpShapeCollection import hkpShapeCollection
from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape
import struct
from .common import any, vector4


class hkpTriSampledHeightFieldCollection(hkpShapeCollection):
    heightfield: hkpSampledHeightFieldShape
    childSize: int
    radius: float
    weldingInfo: any
    triangleExtrusion: vector4

    def __init__(self, infile):
        self.heightfield = hkpSampledHeightFieldShape(infile)  # TYPE_POINTER
        self.childSize = struct.unpack('>i', infile.read(4))
        self.radius = struct.unpack('>f', infile.read(4))
        self.weldingInfo = any(infile)  # TYPE_ARRAY
        self.triangleExtrusion = struct.unpack('>4f', infile.read(16))
