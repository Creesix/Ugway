import math

from Phidget22.Devices.Encoder import *

def init_encoder(hub_serial, hub_port, data_interval):
    """
    Init the encoder at the hub_port.

    @param hub_serial: the hub id
    @param hub_port: the port of the encoder
    @param data_interval: the interval at which the signal is measured (millisecond)
    @return: the Encoder()
    """
    assert data_interval >= 20

    encoder = Encoder()

    encoder.setHubPort(hub_port)
    encoder.setDeviceSerialNumber(hub_serial)
    encoder.openWaitForAttachment(500)
    encoder.setDataInterval(int(data_interval))

    return encoder

def odom_position_calculation(wheels_pos, prev_wheels_pos, theta, wheel_radius, entraxe, encoder_tics_count):
    """
    Calculate the movement in x, y, theta of the robot between two measure of the encoders.

    @param wheels_pos: the (left_pos, right_pos) of the encoders
    @param prev_wheels_pos: the previous (left_pos, right_pos) of the encoders
    @param theta: the angle of the robot
    @param wheel_radius: the radius of the wheels
    @param entraxe: the distance between the wheels
    @param encoder_tics_count: the number of tics per rotation of the encoders
    @return: dx, dy, dtheta
    """
    prev_left_pos, prev_right_pos = prev_wheels_pos
    left_pos, right_pos = wheels_pos

    ds_l = 2 * math.pi * wheel_radius / encoder_tics_count * (left_pos - prev_left_pos) # left
    ds_r = 2 * math.pi * wheel_radius / encoder_tics_count * (right_pos - prev_right_pos)

    dc = (ds_l + ds_r) / 2  # déplacement du centre
    dtheta = (ds_r - ds_l) / entraxe

    dx = dc * math.cos(theta + dtheta / 2)
    dy = dc * math.sin(theta + dtheta / 2)

    return dx, dy, dtheta
