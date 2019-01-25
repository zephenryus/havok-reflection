from .hkpVehicleSimulation import hkpVehicleSimulation
from .hkpVehicleInstance import hkpVehicleInstance
from .common import any
import struct
from .hkpVehiclePerWheelSimulationWheelData import hkpVehiclePerWheelSimulationWheelData


class hkpVehiclePerWheelSimulation(hkpVehicleSimulation):
    instance: hkpVehicleInstance
    world: any
    slipDamping: float
    impulseScaling: float
    maxImpulse: float
    takeDynamicVelocity: float
    curbDamping: float
    wheelData: hkpVehiclePerWheelSimulationWheelData

    def __init__(self, infile):
        self.instance = hkpVehicleInstance(infile)  # TYPE_POINTER
        self.world = any(infile)  # TYPE_POINTER
        self.slipDamping = struct.unpack('>f', infile.read(4))
        self.impulseScaling = struct.unpack('>f', infile.read(4))
        self.maxImpulse = struct.unpack('>f', infile.read(4))
        self.takeDynamicVelocity = struct.unpack('>f', infile.read(4))
        self.curbDamping = struct.unpack('>f', infile.read(4))
        self.wheelData = hkpVehiclePerWheelSimulationWheelData(infile)  # TYPE_ARRAY
