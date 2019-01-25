import pandas as pd
import matplotlib.pyplot as plt

focal_length = 2000 # pixels
sensor_u = 2000 # pixels
sensor_v = 1000 # pixels
world_coords = pd.read_csv("coordinates.txt", delim_whitespace=True)

list_u = []
list_v = []
list_I = []

for index, pixel in world_coords.iterrows():
  x = pixel[0]/pixel[2]
  y = pixel[1]/pixel[2]
   
  u = x*focal_length + sensor_u/2
  v = y*focal_length + sensor_v/2
  
  list_u.append(u)
  list_v.append(v)
  list_I.append(pixel[3])
axes = plt.gca()
axes.set_xlim(0,sensor_u)
axes.set_ylim(0,sensor_v)
plt.scatter(list_u,list_v,c = list_I)
plt.show()
