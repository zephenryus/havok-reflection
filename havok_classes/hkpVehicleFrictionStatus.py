from .hkpVehicleFrictionStatusAxisStatus import hkpVehicleFrictionStatusAxisStatus


class hkpVehicleFrictionStatus(object):
    axis: hkpVehicleFrictionStatusAxisStatus

    def __init__(self, infile):
        self.axis = hkpVehicleFrictionStatusAxisStatus(infile)  # TYPE_STRUCT
