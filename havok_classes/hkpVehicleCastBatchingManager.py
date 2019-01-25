from .hkpVehicleManager import hkpVehicleManager
import struct


class hkpVehicleCastBatchingManager(hkpVehicleManager):
    totalNumWheels: int

    def __init__(self, infile):
        self.totalNumWheels = struct.unpack('>H', infile.read(2))
