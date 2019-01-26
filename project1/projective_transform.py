import pandas as pd
import matplotlib.pyplot as plt

def projective_transform(self,X_world):
  focal_length = self.f # pixels
  sensor_u = self.width # pixels
  sensor_v = self.height # pixels

  list_u = []
  list_v = []
  #list_I = []

  for X_point in X_world.itterows():
    x = X_point[0]/X_point[2]
    y = X_pointl[1]/X_point[2]
     
    u = x*focal_length + sensor_u/2
    v = y*focal_length + sensor_v/2
    
    list_u.append(u)
    list_v.append(v)
    #list_I.append(pixel[3])

  return list_u, list_v
  #axes = plt.gca()
  #axes.set_xlim(0,sensor_u)
  #axes.set_ylim(0,sensor_v)
  #plt.scatter(list_u,list_v,c = list_I)
  #plt.show()
