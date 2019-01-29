import pandas as pd
import matplotlib.pyplot as plt

def projective_transform(focal_length, sensor_u, sensor_v, pose, X_world):

  list_u = []
  list_v = []
  #list_I = []

  for X_point in X_world:
    x = X_point[0]/X_point[2]
    y = X_point[1]/X_point[2]

    u = x*focal_length + sensor_u/2.0
    v = y*focal_length + sensor_v/2.0

    list_u.append(u)
    list_v.append(v)
    #list_I.append(pixel[3])
  return list_u, list_v

###############################################################################
##############################       MAIN     #################################
###############################################################################

# axes = plt.gca()
# axes.set_xlim(0,sensor_u)
# axes.set_ylim(0,sensor_v)
# plt.scatter(list_u,list_v,c = list_I)
# plt.show()
