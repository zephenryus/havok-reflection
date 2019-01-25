from .hkpVehicleSimulation import hkpVehicleSimulation
from .hkpVehicleInstance import hkpVehicleInstance
import struct
from typing import List
from .common import get_array
from .hkpVehiclePerWheelSimulationWheelData import hkpVehiclePerWheelSimulationWheelData


class hkpVehiclePerWheelSimulation(hkpVehicleSimulation):
    instance: any
    world: any
    slipDamping: float
    impulseScaling: float
    maxImpulse: float
    takeDynamicVelocity: float
    curbDamping: float
    wheelData: List[hkpVehiclePerWheelSimulationWheelData]

    def __init__(self, infile):
        self.instance = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.world = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.slipDamping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.impulseScaling = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxImpulse = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.takeDynamicVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.curbDamping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelData = get_array(infile, hkpVehiclePerWheelSimulationWheelData, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} instance={instance}, world={world}, slipDamping={slipDamping}, impulseScaling={impulseScaling}, maxImpulse={maxImpulse}, takeDynamicVelocity={takeDynamicVelocity}, curbDamping={curbDamping}, wheelData=[{wheelData}]>".format(**{
            "class_name": self.__class__.__name__,
            "instance": self.instance,
            "world": self.world,
            "slipDamping": self.slipDamping,
            "impulseScaling": self.impulseScaling,
            "maxImpulse": self.maxImpulse,
            "takeDynamicVelocity": self.takeDynamicVelocity,
            "curbDamping": self.curbDamping,
            "wheelData": self.wheelData,
        })
