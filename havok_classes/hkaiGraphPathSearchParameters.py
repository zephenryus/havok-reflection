import struct
from .hkaiSearchParametersBufferSizes import hkaiSearchParametersBufferSizes


class hkaiGraphPathSearchParameters(object):
    heuristicWeight: float
    useHierarchicalHeuristic: bool
    costModifier: any
    edgeFilter: any
    bufferSizes: hkaiSearchParametersBufferSizes
    hierarchyBufferSizes: hkaiSearchParametersBufferSizes

    def __init__(self, infile):
        self.heuristicWeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.useHierarchicalHeuristic = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.costModifier = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.edgeFilter = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.bufferSizes = hkaiSearchParametersBufferSizes(infile)  # TYPE_STRUCT:TYPE_VOID
        self.hierarchyBufferSizes = hkaiSearchParametersBufferSizes(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} heuristicWeight={heuristicWeight}, useHierarchicalHeuristic={useHierarchicalHeuristic}, costModifier={costModifier}, edgeFilter={edgeFilter}, bufferSizes={bufferSizes}, hierarchyBufferSizes={hierarchyBufferSizes}>".format(**{
            "class_name": self.__class__.__name__,
            "heuristicWeight": self.heuristicWeight,
            "useHierarchicalHeuristic": self.useHierarchicalHeuristic,
            "costModifier": self.costModifier,
            "edgeFilter": self.edgeFilter,
            "bufferSizes": self.bufferSizes,
            "hierarchyBufferSizes": self.hierarchyBufferSizes,
        })
