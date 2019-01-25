import struct


class hkpGenericConstraintDataSchemeConstraintInfo(object):
    maxSizeOfSchema: int
    sizeOfSchemas: int
    numSolverResults: int
    numSolverElemTemps: int

    def __init__(self, infile):
        self.maxSizeOfSchema = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.sizeOfSchemas = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numSolverResults = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numSolverElemTemps = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} maxSizeOfSchema={maxSizeOfSchema}, sizeOfSchemas={sizeOfSchemas}, numSolverResults={numSolverResults}, numSolverElemTemps={numSolverElemTemps}>".format(**{
            "class_name": self.__class__.__name__,
            "maxSizeOfSchema": self.maxSizeOfSchema,
            "sizeOfSchemas": self.sizeOfSchemas,
            "numSolverResults": self.numSolverResults,
            "numSolverElemTemps": self.numSolverElemTemps,
        })
