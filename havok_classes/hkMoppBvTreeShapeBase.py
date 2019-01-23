from .hkpBvTreeShape import hkpBvTreeShape
from .hkpMoppCode import hkpMoppCode


class hkMoppBvTreeShapeBase(hkpBvTreeShape):
	code: hkpMoppCode
	moppData: any
	moppDataSize: int
	codeInfoCopy: any
