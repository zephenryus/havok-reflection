import struct


class hkaiEdgeFollowingBehaviorCornerPredictorInitInfo(object):
    positionLocal: vector4
    forwardVectorLocal: vector4
    upLocal: vector4
    positionSectionIndex: int
    nextEdgeIndex: int
    nextIsLeft: bool
    hasInfo: bool

    def __init__(self, infile):
        self.positionLocal = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.forwardVectorLocal = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.upLocal = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.positionSectionIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.nextEdgeIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.nextIsLeft = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.hasInfo = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} positionLocal={positionLocal}, forwardVectorLocal={forwardVectorLocal}, upLocal={upLocal}, positionSectionIndex={positionSectionIndex}, nextEdgeIndex={nextEdgeIndex}, nextIsLeft={nextIsLeft}, hasInfo={hasInfo}>".format(**{
            "class_name": self.__class__.__name__,
            "positionLocal": self.positionLocal,
            "forwardVectorLocal": self.forwardVectorLocal,
            "upLocal": self.upLocal,
            "positionSectionIndex": self.positionSectionIndex,
            "nextEdgeIndex": self.nextEdgeIndex,
            "nextIsLeft": self.nextIsLeft,
            "hasInfo": self.hasInfo,
        })
