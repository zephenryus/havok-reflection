from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from typing import List
from .common import get_array
from .hclBonePlanesSetupObjectPerParticlePlane import hclBonePlanesSetupObjectPerParticlePlane
from .hclBonePlanesSetupObjectGlobalPlane import hclBonePlanesSetupObjectGlobalPlane
from .hclBonePlanesSetupObjectPerParticleAngle import hclBonePlanesSetupObjectPerParticleAngle
import struct


class hclBonePlanesSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: any
    transformSetSetup: any
    perParticlePlanes: List[hclBonePlanesSetupObjectPerParticlePlane]
    globalPlanes: List[hclBonePlanesSetupObjectGlobalPlane]
    perParticleAngle: List[hclBonePlanesSetupObjectPerParticleAngle]
    angleSpecifiedInDegrees: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simulationMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.transformSetSetup = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.perParticlePlanes = get_array(infile, hclBonePlanesSetupObjectPerParticlePlane, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.globalPlanes = get_array(infile, hclBonePlanesSetupObjectGlobalPlane, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.perParticleAngle = get_array(infile, hclBonePlanesSetupObjectPerParticleAngle, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.angleSpecifiedInDegrees = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simulationMesh={simulationMesh}, transformSetSetup={transformSetSetup}, perParticlePlanes=[{perParticlePlanes}], globalPlanes=[{globalPlanes}], perParticleAngle=[{perParticleAngle}], angleSpecifiedInDegrees={angleSpecifiedInDegrees}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simulationMesh": self.simulationMesh,
            "transformSetSetup": self.transformSetSetup,
            "perParticlePlanes": self.perParticlePlanes,
            "globalPlanes": self.globalPlanes,
            "perParticleAngle": self.perParticleAngle,
            "angleSpecifiedInDegrees": self.angleSpecifiedInDegrees,
        })
