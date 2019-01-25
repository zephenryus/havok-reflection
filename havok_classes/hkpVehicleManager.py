from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpVehicleInstance import hkpVehicleInstance


class hkpVehicleManager(hkReferencedObject):
    registeredVehicles: List[hkpVehicleInstance]

    def __init__(self, infile):
        self.registeredVehicles = get_array(infile, hkpVehicleInstance, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} registeredVehicles=[{registeredVehicles}]>".format(**{
            "class_name": self.__class__.__name__,
            "registeredVehicles": self.registeredVehicles,
        })
