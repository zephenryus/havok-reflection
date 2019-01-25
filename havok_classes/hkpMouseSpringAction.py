from .hkpUnaryAction import hkpUnaryAction
import struct
from typing import List
from .common import get_array


class hkpMouseSpringAction(hkpUnaryAction):
    positionInRbLocal: vector4
    mousePositionInWorld: vector4
    springDamping: float
    springElasticity: float
    maxRelativeForce: float
    objectDamping: float
    shapeKey: int
    applyCallbacks: List[any]

    def __init__(self, infile):
        self.positionInRbLocal = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.mousePositionInWorld = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.springDamping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.springElasticity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxRelativeForce = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.objectDamping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.shapeKey = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.applyCallbacks = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} positionInRbLocal={positionInRbLocal}, mousePositionInWorld={mousePositionInWorld}, springDamping={springDamping}, springElasticity={springElasticity}, maxRelativeForce={maxRelativeForce}, objectDamping={objectDamping}, shapeKey={shapeKey}, applyCallbacks=[{applyCallbacks}]>".format(**{
            "class_name": self.__class__.__name__,
            "positionInRbLocal": self.positionInRbLocal,
            "mousePositionInWorld": self.mousePositionInWorld,
            "springDamping": self.springDamping,
            "springElasticity": self.springElasticity,
            "maxRelativeForce": self.maxRelativeForce,
            "objectDamping": self.objectDamping,
            "shapeKey": self.shapeKey,
            "applyCallbacks": self.applyCallbacks,
        })
