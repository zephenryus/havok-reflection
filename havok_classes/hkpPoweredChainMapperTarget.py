from .hkpPoweredChainData import hkpPoweredChainData
import struct


class hkpPoweredChainMapperTarget(object):
    chain: any
    infoIndex: int

    def __init__(self, infile):
        self.chain = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.infoIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} chain={chain}, infoIndex={infoIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "chain": self.chain,
            "infoIndex": self.infoIndex,
        })
