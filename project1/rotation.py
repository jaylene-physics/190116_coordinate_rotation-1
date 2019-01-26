import pandas as pd
import numpy as np
import collections
from matplotlib import pyplot as plt
from matplotlib import colors
import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D

def T(cam_coords):
  return np.matrix([[1,0,0,-cam_coords[0]],[0,1,0,-cam_coords[1]],[0,0,1,-cam_coords[2]],[0,0,0,1]])

def R_yaw(yaw):
  return np.matrix([[np.cos(yaw),-np.sin(yaw),0,0],[np.sin(yaw),np.cos(yaw),0,0],[0,0,1,0]])

def R_pitch(pitch):
  return np.matrix([[1,0,0],[0,np.cos(pitch),np.sin(pitch)],[0,-np.sin(pitch),np.cos(pitch)]])

def R_roll(roll):
  return np.matrix([[np.cos(roll),0,-np.sin(roll)],[0,1,0],[np.sin(roll),0,np.cos(roll)]])

def R_axis():
  return np.matrix([[1,0,0],[0,0,-1],[0,1,0]])

def rotate(self,X_world):
  #camera coords  [easting, northing , elecation, yaw, pitch ,roll]
  easting =  self.p[:,0]
  northing = self.p[:,1]
  elevation = self.p[:,2]
  cam_coords = np.array([easting, northing, elevation])

  #camera angle
  yaw = self.p[:,3] # radians
  pitch = self.p[:,4] # radians
  roll = self.p[:,5] # radians


  T = T(cam_coords)
  R_yaw = R_yaw(yaw)
  R_pitch = R_pitch(pitch)
  R_roll = R_roll(roll)
  R_axis = R_axis()
  C = R_axis.dot(R_roll).dot(R_pitch).dot(R_yaw).dot(T)
  x = []
  y = []
  z = []
  I = []

  for index, coord in X_world.iterrows():
    np_coord = np.array(coord)
    np_coord = np.append(coord, 1)
    xyz_coords = C.dot(np_coord).T
    x.append(xyz_coords[0])
    y.append(xyz_coords[1])
    z.append(xyz_coords[2])
