from .hkpVehicleManager import hkpVehicleManager
import struct


class hkpVehicleCastBatchingManager(hkpVehicleManager):
    totalNumWheels: int

    def __init__(self, infile):
        self.totalNumWheels = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} totalNumWheels={totalNumWheels}>".format(**{
            "class_name": self.__class__.__name__,
            "totalNumWheels": self.totalNumWheels,
        })
