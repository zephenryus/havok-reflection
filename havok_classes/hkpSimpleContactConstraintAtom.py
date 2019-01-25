from .hkpConstraintAtom import hkpConstraintAtom
import struct
from .hkpSimpleContactConstraintDataInfo import hkpSimpleContactConstraintDataInfo


class hkpSimpleContactConstraintAtom(hkpConstraintAtom):
    sizeOfAllAtoms: int
    numContactPoints: int
    numReservedContactPoints: int
    numUserDatasForBodyA: int
    numUserDatasForBodyB: int
    contactPointPropertiesStriding: int
    maxNumContactPoints: int
    info: hkpSimpleContactConstraintDataInfo

    def __init__(self, infile):
        self.sizeOfAllAtoms = struct.unpack('>H', infile.read(2))
        self.numContactPoints = struct.unpack('>H', infile.read(2))
        self.numReservedContactPoints = struct.unpack('>H', infile.read(2))
        self.numUserDatasForBodyA = struct.unpack('>B', infile.read(1))
        self.numUserDatasForBodyB = struct.unpack('>B', infile.read(1))
        self.contactPointPropertiesStriding = struct.unpack('>B', infile.read(1))
        self.maxNumContactPoints = struct.unpack('>H', infile.read(2))
        self.info = hkpSimpleContactConstraintDataInfo(infile)  # TYPE_STRUCT
