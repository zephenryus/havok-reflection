from .hkpBvTreeShape import hkpBvTreeShape
from .hkpMoppCode import hkpMoppCode
from .common import any, vector4


class hkMoppBvTreeShapeBase(hkpBvTreeShape):
    code: hkpMoppCode
    moppData: any
    moppDataSize: int
    codeInfoCopy: vector4
