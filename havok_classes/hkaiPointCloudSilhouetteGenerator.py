from .hkaiSilhouetteGenerator import hkaiSilhouetteGenerator
from .hkAabb import hkAabb


class hkaiPointCloudSilhouetteGenerator(hkaiSilhouetteGenerator):
	localAabb: hkAabb
	localPoints: any
	silhouetteSizes: any
	weldTolerance: float
	silhouetteDetailLevel: any
	flags: any
	localPointsChanged: bool
	isEnabled: bool
