from .common import vector4, any


class hkpCompressedMeshShapeChunk(object):
    offset: vector4
    vertices: any
    indices: any
    stripLengths: any
    weldingInfo: any
    materialInfo: int
    reference: int
    transformIndex: int
