from .hkpBinaryAction import hkpBinaryAction


class hkpSpringAction(hkpBinaryAction):
	lastForce: any
	positionAinA: any
	positionBinB: any
	restLength: float
	strength: float
	damping: float
	onCompression: bool
	onExtension: bool
