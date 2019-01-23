from .hkReferencedObject import hkReferencedObject
from .hkaiGatePathPathGate import hkaiGatePathPathGate
from .hkaiGatePathUtilExponentialSchedule import hkaiGatePathUtilExponentialSchedule


class hkaiGatePath(hkReferencedObject):
	gates: hkaiGatePathPathGate
	startPoint: any
	schedule: hkaiGatePathUtilExponentialSchedule
	needsInitialSmooth: bool
