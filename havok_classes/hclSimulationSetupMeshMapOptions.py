import struct
from .hclVertexSelectionInput import hclVertexSelectionInput


class hclSimulationSetupMeshMapOptions(object):
    collapseVertices: bool
    collapseThreshold: float
    vertexSelection: hclVertexSelectionInput

    def __init__(self, infile):
        self.collapseVertices = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.collapseThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} collapseVertices={collapseVertices}, collapseThreshold={collapseThreshold}, vertexSelection={vertexSelection}>".format(**{
            "class_name": self.__class__.__name__,
            "collapseVertices": self.collapseVertices,
            "collapseThreshold": self.collapseThreshold,
            "vertexSelection": self.vertexSelection,
        })
