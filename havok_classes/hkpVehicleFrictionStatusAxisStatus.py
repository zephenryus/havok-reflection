import struct


class hkpVehicleFrictionStatusAxisStatus(object):
    forward_slip_velocity: float
    side_slip_velocity: float
    skid_energy_density: float
    side_force: float
    delayed_forward_impulse: float
    sideRhs: float
    forwardRhs: float
    relativeSideForce: float
    relativeForwardForce: float

    def __init__(self, infile):
        self.forward_slip_velocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.side_slip_velocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.skid_energy_density = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.side_force = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.delayed_forward_impulse = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.sideRhs = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.forwardRhs = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.relativeSideForce = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.relativeForwardForce = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} forward_slip_velocity={forward_slip_velocity}, side_slip_velocity={side_slip_velocity}, skid_energy_density={skid_energy_density}, side_force={side_force}, delayed_forward_impulse={delayed_forward_impulse}, sideRhs={sideRhs}, forwardRhs={forwardRhs}, relativeSideForce={relativeSideForce}, relativeForwardForce={relativeForwardForce}>".format(**{
            "class_name": self.__class__.__name__,
            "forward_slip_velocity": self.forward_slip_velocity,
            "side_slip_velocity": self.side_slip_velocity,
            "skid_energy_density": self.skid_energy_density,
            "side_force": self.side_force,
            "delayed_forward_impulse": self.delayed_forward_impulse,
            "sideRhs": self.sideRhs,
            "forwardRhs": self.forwardRhs,
            "relativeSideForce": self.relativeSideForce,
            "relativeForwardForce": self.relativeForwardForce,
        })
