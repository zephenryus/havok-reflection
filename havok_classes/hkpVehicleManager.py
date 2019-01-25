from .hkReferencedObject import hkReferencedObject
from .hkpVehicleInstance import hkpVehicleInstance


class hkpVehicleManager(hkReferencedObject):
    registeredVehicles: hkpVehicleInstance

    def __init__(self, infile):
        self.registeredVehicles = hkpVehicleInstance(infile)  # TYPE_ARRAY
