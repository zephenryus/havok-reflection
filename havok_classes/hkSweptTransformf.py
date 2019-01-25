import struct


class hkSweptTransformf(object):
    centerOfMass0: vector4
    centerOfMass1: vector4
    rotation0: any
    rotation1: any
    centerOfMassLocal: vector4

    def __init__(self, infile):
        self.centerOfMass0 = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.centerOfMass1 = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.rotation0 = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.rotation1 = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.centerOfMassLocal = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} centerOfMass0={centerOfMass0}, centerOfMass1={centerOfMass1}, rotation0={rotation0}, rotation1={rotation1}, centerOfMassLocal={centerOfMassLocal}>".format(**{
            "class_name": self.__class__.__name__,
            "centerOfMass0": self.centerOfMass0,
            "centerOfMass1": self.centerOfMass1,
            "rotation0": self.rotation0,
            "rotation1": self.rotation1,
            "centerOfMassLocal": self.centerOfMassLocal,
        })
