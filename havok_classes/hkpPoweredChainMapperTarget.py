from .hkpPoweredChainData import hkpPoweredChainData
import struct


class hkpPoweredChainMapperTarget(object):
    chain: hkpPoweredChainData
    infoIndex: int

    def __init__(self, infile):
        self.chain = hkpPoweredChainData(infile)  # TYPE_POINTER
        self.infoIndex = struct.unpack('>i', infile.read(4))
