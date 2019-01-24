from .hkReferencedObject import hkReferencedObject
from .hkpVehicleFrictionDescriptionAxisDescription import hkpVehicleFrictionDescriptionAxisDescription


class hkpVehicleFrictionDescription(hkReferencedObject):
    wheelDistance: float
    chassisMassInv: float
    axleDescr: hkpVehicleFrictionDescriptionAxisDescription
