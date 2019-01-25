import struct


class hclBonePlanesConstraintSetBonePlane(object):
    planeEquationBone: vector4
    particleIndex: int
    transformIndex: int
    stiffness: float

    def __init__(self, infile):
        self.planeEquationBone = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.particleIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.transformIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.stiffness = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} planeEquationBone={planeEquationBone}, particleIndex={particleIndex}, transformIndex={transformIndex}, stiffness={stiffness}>".format(**{
            "class_name": self.__class__.__name__,
            "planeEquationBone": self.planeEquationBone,
            "particleIndex": self.particleIndex,
            "transformIndex": self.transformIndex,
            "stiffness": self.stiffness,
        })
