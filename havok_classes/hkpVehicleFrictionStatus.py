from .hkpVehicleFrictionStatusAxisStatus import hkpVehicleFrictionStatusAxisStatus


class hkpVehicleFrictionStatus(object):
    axis: hkpVehicleFrictionStatusAxisStatus

    def __init__(self, infile):
        self.axis = hkpVehicleFrictionStatusAxisStatus(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} axis={axis}>".format(**{
            "class_name": self.__class__.__name__,
            "axis": self.axis,
        })
