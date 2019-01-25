from .hkpShapeCollection import hkpShapeCollection
from .hkpSampledHeightFieldShape import hkpSampledHeightFieldShape
import struct
from typing import List
from .common import get_array


class hkpTriSampledHeightFieldCollection(hkpShapeCollection):
    heightfield: any
    childSize: int
    radius: float
    weldingInfo: List[int]
    triangleExtrusion: vector4

    def __init__(self, infile):
        self.heightfield = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.childSize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.weldingInfo = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.triangleExtrusion = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} heightfield={heightfield}, childSize={childSize}, radius={radius}, weldingInfo=[{weldingInfo}], triangleExtrusion={triangleExtrusion}>".format(**{
            "class_name": self.__class__.__name__,
            "heightfield": self.heightfield,
            "childSize": self.childSize,
            "radius": self.radius,
            "weldingInfo": self.weldingInfo,
            "triangleExtrusion": self.triangleExtrusion,
        })
