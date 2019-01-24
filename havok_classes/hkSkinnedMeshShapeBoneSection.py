from .hkMeshShape import hkMeshShape


class hkSkinnedMeshShapeBoneSection(object):
    meshBuffer: hkMeshShape
    startBoneSetId: int
    numBoneSets: int
