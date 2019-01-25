import struct


class hkpGenericConstraintDataSchemeConstraintInfo(object):
    maxSizeOfSchema: int
    sizeOfSchemas: int
    numSolverResults: int
    numSolverElemTemps: int

    def __init__(self, infile):
        self.maxSizeOfSchema = struct.unpack('>i', infile.read(4))
        self.sizeOfSchemas = struct.unpack('>i', infile.read(4))
        self.numSolverResults = struct.unpack('>i', infile.read(4))
        self.numSolverElemTemps = struct.unpack('>i', infile.read(4))
