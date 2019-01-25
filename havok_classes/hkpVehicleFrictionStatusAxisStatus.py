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
        self.forward_slip_velocity = struct.unpack('>f', infile.read(4))
        self.side_slip_velocity = struct.unpack('>f', infile.read(4))
        self.skid_energy_density = struct.unpack('>f', infile.read(4))
        self.side_force = struct.unpack('>f', infile.read(4))
        self.delayed_forward_impulse = struct.unpack('>f', infile.read(4))
        self.sideRhs = struct.unpack('>f', infile.read(4))
        self.forwardRhs = struct.unpack('>f', infile.read(4))
        self.relativeSideForce = struct.unpack('>f', infile.read(4))
        self.relativeForwardForce = struct.unpack('>f', infile.read(4))
