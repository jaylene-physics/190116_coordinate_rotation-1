import pandas as pd
import numpy as np
import collections
from matplotlib import pyplot as plt
from matplotlib import colors
import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def Trans(cam_coords):
  return np.matrix([[1, 0, 0, -cam_coords[0]],
                    [0, 1, 0, -cam_coords[1]],
                    [0, 0, 1, -cam_coords[2]],
                    [0, 0, 0,             1]])

def R_yaw_trans(yaw):
  return np.matrix([[np.cos(yaw), -np.sin(yaw), 0, 0],
                    [np.sin(yaw),  np.cos(yaw), 0, 0],
                    [          0,            0, 1, 0]])

def R_pitch_trans(pitch):
  return np.matrix([[1,              0,             0],
                    [0,  np.cos(pitch), np.sin(pitch)],
                    [0, -np.sin(pitch), np.cos(pitch)]])

def R_roll_trans(roll):
  return np.matrix([[np.cos(roll), 0, -np.sin(roll)],
                    [0,            1,             0],
                    [np.sin(roll), 0, np.cos(roll)]])

def R_axis_trans():
  return np.matrix([[1, 0, 0],
                    [0, 0,-1],
                    [0, 1, 0]])

def rotate(pose, X_world):
  #camera coords  [easting, northing, elevation, yaw, pitch ,roll]
  easting =  pose[0]
  northing = pose[1]
  elevation = pose[2]
  cam_coords = np.array([easting, northing, elevation])

  #camera angle
  yaw = pose[3] # radians
  pitch = pose[4] # radians
  roll = pose[5] # radians


  T = Trans(cam_coords)
  R_yaw = R_yaw_trans(yaw)
  R_pitch = R_pitch_trans(pitch)
  R_roll = R_roll_trans(roll)
  R_axis = R_axis_trans()
  C = R_axis.dot(R_roll).dot(R_pitch).dot(R_yaw).dot(T)
  x = []
  y = []
  z = []
  I = []

  for index, coord in X_world.iterrows():
    np_coord = np.array(coord)
    np_coord = np.append(coord, 1)
    xyz_coords = C.dot(np_coord).T
    x.append(xyz_coords.item(0))
    y.append(xyz_coords.item(1))
    z.append(xyz_coords.item(2))

  return x, y, z

  #############################################################################
  ##############################       MAIN     ###############################
  #############################################################################
