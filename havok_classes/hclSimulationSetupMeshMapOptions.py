import struct
from .hclVertexSelectionInput import hclVertexSelectionInput


class hclSimulationSetupMeshMapOptions(object):
    collapseVertices: bool
    collapseThreshold: float
    vertexSelection: hclVertexSelectionInput

    def __init__(self, infile):
        self.collapseVertices = struct.unpack('>?', infile.read(1))
        self.collapseThreshold = struct.unpack('>f', infile.read(4))
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
