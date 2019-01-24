from .hkpConstraintAtom import hkpConstraintAtom
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
