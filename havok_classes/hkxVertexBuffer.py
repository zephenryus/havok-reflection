from .hkReferencedObject import hkReferencedObject
from .hkxVertexBufferVertexData import hkxVertexBufferVertexData
from .hkxVertexDescription import hkxVertexDescription


class hkxVertexBuffer(hkReferencedObject):
    data: hkxVertexBufferVertexData
    desc: hkxVertexDescription

    def __init__(self, infile):
        self.data = hkxVertexBufferVertexData(infile)  # TYPE_STRUCT:TYPE_VOID
        self.desc = hkxVertexDescription(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} data={data}, desc={desc}>".format(**{
            "class_name": self.__class__.__name__,
            "data": self.data,
            "desc": self.desc,
        })
