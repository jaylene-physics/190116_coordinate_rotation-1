'''

'''

import numpy as np
import pandas as pd
import csv

# Camera -> Global Coords Conversion

''' Translation Matrix to center Camera Coords on Global Coords axis '''
def T(cam_pose):
    T = np.matrix([[1, 0, 0, -cam_pose[0]],
                   [0, 1, 0, -cam_pose[1]],
                   [0, 0, 1, -cam_pose[2]]])
    return T

''' Rotation Matrix which rotates the Camera Coords about the z-axis (yaw) by theta degrees '''
def R_yaw(theta):
    R_yaw = np.matrix([[np.cos(theta), -np.sin(theta),  0, 0],
                       [np.sin(theta),  np.cos(theta),  0, 0],
                       [            0,              0,  1, 0]])
    return R_yaw

''' Rotation Matrix which rotates the Camera Coords about the x-axis (pitch) by theta degrees '''
def R_pitch(theta):
    R_pitch = np.matrix([[1,              0,             0],
                         [0,  np.cos(theta), np.sin(theta)],
                         [0, -np.sin(theta), np.cos(theta)]])
    return R_pitch

''' Rotation Matrix which rotates the Camera Coords about the y-axis (roll) by theta degrees '''
def R_roll(theta):
    R_roll = np.matrix([[np.cos(theta), 0, -np.sin(theta)],
                        [            0, 1,              0],
                        [np.sin(theta), 0,  np.cos(theta)]])
    return R_roll

''' Rotation Matrix which rotates z-axis to correspond to the elevation axis '''
def R_axis():
    R_axis = np.matrix([[1, 0,  0],
                        [0, 0, -1],
                        [0, 1,  0]])
    return R_axis

''' Complete transformation matrix from camera coords to generalized Easting/Northing/Elevation (x,y,z) coords based on camera pose'''
def C(cam_pose):
    # cam_pose = [cam_x, cam_y, cam_z, yaw, pitch, roll]
    T = T(cam_pose)
    R_yaw = R_yaw(cam_pose[3])
    R_pitch = R_pitch(cam_pose[4])
    R_roll = R_roll(cam_pose[5])
    R_axis = R_roll()
    C = R_axis.dot(R_roll).dot(R_pitch).dot(R_yaw).dot(T)
    return C

''' Transform camera coords to generalized Easting/Northing/Elevation (x,y,z) coords based on camera pose'''
def transform_rotation(coords_cam, cam_pose):
    C = C(cam_pose)
    coords_ene = coords_cam.dot(C)


##########################################################################################
###############################        MAIN       ########################################
##########################################################################################

easting = 10000 
northing = 5000
elevation = 1000
