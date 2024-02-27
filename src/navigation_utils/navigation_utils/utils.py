#!/usr/bin/env python3
import math

from Phidget22.Devices.Encoder import *

from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped

import tf_conversions
import tf2_ros

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

def broadcast_associated_tf(node, pos):
    """
    Broadcast the tf from odom to base_footprint associated with pos.

    @param pos: the position
    @return:
    """

    br = tf2_ros.TransformBroadcaster()
    t = TransformStamped()

    t.header.stamp = node.get_clock().now()
    t.header.frame_id = "odom"
    t.child_frame_id = "base_footprint"
    t.transform.translation.x = pos.position.x
    t.transform.translation.y = pos.position.y
    t.transform.translation.z = 0.0

    q = tf_conversions.transformations.quaternion_from_euler(0, 0, pos.orientation.z)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

def get_odom_msg(node, pos):
    """
    Create an Odometry() from odom to base_footprint associated with pos.

    @param pos: the position
    @return:
    """
    msg = Odometry()
    msg.header.stamp = node.get_clock().now()
    msg.header.frame_id = "odom"
    msg.child_frame_id = "base_footprint"
    msg.pose.pose.position.x = pos.position.x
    msg.pose.pose.position.y = pos.position.y
    msg.pose.pose.position.z = 0

    q = tf_conversions.transformations.quaternion_from_euler(0, 0, pos.orientation.z)
    msg.pose.pose.orientation.x = q[0]
    msg.pose.pose.orientation.y = q[1]
    msg.pose.pose.orientation.z = q[2]
    msg.pose.pose.orientation.w = q[3]

    return msg