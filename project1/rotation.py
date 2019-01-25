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

def rotate(X,X_cam):  
  #camera coords
  easting = 10000
  northing = 5000
  elevation = 1000
  cam_coords = np.array([easting, northing, elevation])

  #camera angle
  yaw = 0.785398 # radians
  pitch = -0.174532925 # radians
  roll = 0 # radians

  ene_coords = pd.read_csv("coordinates_ene.txt", delim_whitespace=True)

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

  for index, coord in ene_coords.iterrows():
    np_coord = np.array(coord)
    np_coord = np.append(coord, 1)
    xyz_coords = C.dot(np_coord).T 
    x.append(xyz_coords[0])
    y.append(xyz_coords[1])
    z.append(xyz_coords[2])

'''
  z = [float(s) for s in z]
  cm = plt.get_cmap('jet')
  cNorm = colors.Normalize(vmin=min(z), vmax=max(z))
  scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
  fig = plt.figure()
  ax = Axes3D(fig)
  scale = scalarMap.to_rgba(z)
  ax.scatter(x, y, z)
  scalarMap.set_array(z)
  fig.colorbar(scalarMap)
  plt.show()
  cNorm = colors.Normalize(vmin=min(z), vmax=max(z))
  scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
  fig = plt.figure()
  ax = Axes3D(fig)
  scale = scalarMap.to_rgba(z)
  ax.scatter(x, y, z)
  scalarMap.set_array(z)
  fig.colorbar(scalarMap)
  plt.show()
'''
