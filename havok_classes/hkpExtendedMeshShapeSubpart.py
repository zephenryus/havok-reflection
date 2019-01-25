import struct


class hkpExtendedMeshShapeSubpart(object):
    typeAndFlags: int
    shapeInfo: int
    materialStriding: int
    materialIndexStriding: int
    materialIndexBase: any
    materialBase: any
    userData: int

    def __init__(self, infile):
        self.typeAndFlags = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.shapeInfo = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.materialStriding = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.materialIndexStriding = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.materialIndexBase = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.materialBase = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} typeAndFlags={typeAndFlags}, shapeInfo={shapeInfo}, materialStriding={materialStriding}, materialIndexStriding={materialIndexStriding}, materialIndexBase={materialIndexBase}, materialBase={materialBase}, userData={userData}>".format(**{
            "class_name": self.__class__.__name__,
            "typeAndFlags": self.typeAndFlags,
            "shapeInfo": self.shapeInfo,
            "materialStriding": self.materialStriding,
            "materialIndexStriding": self.materialIndexStriding,
            "materialIndexBase": self.materialIndexBase,
            "materialBase": self.materialBase,
            "userData": self.userData,
        })
