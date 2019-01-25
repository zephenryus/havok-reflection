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
        self.sizeOfAllAtoms = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.numContactPoints = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.numReservedContactPoints = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.numUserDatasForBodyA = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.numUserDatasForBodyB = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.contactPointPropertiesStriding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.maxNumContactPoints = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.info = hkpSimpleContactConstraintDataInfo(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} sizeOfAllAtoms={sizeOfAllAtoms}, numContactPoints={numContactPoints}, numReservedContactPoints={numReservedContactPoints}, numUserDatasForBodyA={numUserDatasForBodyA}, numUserDatasForBodyB={numUserDatasForBodyB}, contactPointPropertiesStriding={contactPointPropertiesStriding}, maxNumContactPoints={maxNumContactPoints}, info={info}>".format(**{
            "class_name": self.__class__.__name__,
            "sizeOfAllAtoms": self.sizeOfAllAtoms,
            "numContactPoints": self.numContactPoints,
            "numReservedContactPoints": self.numReservedContactPoints,
            "numUserDatasForBodyA": self.numUserDatasForBodyA,
            "numUserDatasForBodyB": self.numUserDatasForBodyB,
            "contactPointPropertiesStriding": self.contactPointPropertiesStriding,
            "maxNumContactPoints": self.maxNumContactPoints,
            "info": self.info,
        })
