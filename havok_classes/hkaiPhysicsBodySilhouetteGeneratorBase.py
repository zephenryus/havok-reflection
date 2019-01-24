from .hkaiPointCloudSilhouetteGenerator import hkaiPointCloudSilhouetteGenerator
from .common import vector4


class hkaiPhysicsBodySilhouetteGeneratorBase(hkaiPointCloudSilhouetteGenerator):
    linearVelocityAndThreshold: vector4
