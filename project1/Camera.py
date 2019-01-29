from projective_transform import *
from rotation import *
from scipy.optimize import least_squares
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

class Camera(object):

    def __init__(self, pose, f_length, image_width, image_height):
        self.p = pose
        self.f = f_length
        self.c = np.array([image_width, image_height])

    def projective_transform_project(self, pose, X_world):
        u,v = projective_transform(self.f, self.c[0], self.c[1], pose, X_world)
        U = np.array([u,v]).T
        return U

    def rotational_transform(self, pose, X_world):
        x,y,z = rotate(pose, X_world)
        X = np.array([x,y,z]).T
        return X

    def convert_world_to_cam_coords(self, X_world):
        pose = self.p.copy()
        X_cam = self.rotational_transform(pose, X_world)
        X_cam = self.projective_transform_project(pose, X_cam)
        return X_cam

    @staticmethod
    def residual(pose, self, X_world, X_cam_true):
      X_cam_pred = self.rotational_transform(pose, X_world)
      X_cam_pred = self.projective_transform_project(pose, X_cam_pred)
      return (X_cam_pred - X_cam_true).values.flatten()

    def estimate_pose(self, X_world, X_cam):
      pose = self.p.copy()
      pose_opt = least_squares(self.residual, pose, method = 'lm', args=(self, X_world, X_cam))
      print(pose_opt)
      self.p = pose_opt.x
      return pose_opt.x

###############################################################################
##############################       MAIN     #################################
###############################################################################

# Camera specs
f_length  = 27.0 #23.0
sensor_size = 36.0 #23.5
width = 3264 #6000
length = 2448 #4000
f_length = f_length/sensor_size*width
pose_guess = [272510.0,5193893.0,1000.0,3.14/2.0,0,0]
# pose_guess = [272470.0,5193991.0,985.0,1.97,0.214,0.01]

# Known data points
world_coords = pd.read_csv("gcp_1.txt", delimiter=",", header=None)
X_world = world_coords.iloc[:,2:5] #real world coordinates
X_cam = world_coords.iloc[:,0:2] # pixel coordinates OR OBSERVED VALUES

# Estimate Camera pose
camera = Camera(pose_guess, f_length, width, length)
est_pose = camera.estimate_pose(X_world, X_cam)

# Plot Results
X_cam_pred = camera.convert_world_to_cam_coords(X_world)
print('X_cam_true: \n', X_cam)
print('X_cam_pred: \n', X_cam_pred)
fig, ax = plt.subplots(1, figsize=(12,8))
ax.imshow(io.imread("campus_stereo_1.jpg"))
ax.scatter(X_cam.iloc[:,0],X_cam.iloc[:,1],c="red",s=100)
ax.scatter(X_cam_pred[:, 0], X_cam_pred[:, 1],c="green",s=100)
plt.show(fig)
