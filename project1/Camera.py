import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares
from skimage import io

from project1.projective_transform import projective_transform
from project1.rotation import rotate

f_length35  = 35.0
width = 6000
length = 4000
f_length = f_length35/36*width
world_coords = pd.read_csv("Image_constrain.txt", delimiter="|")
X_world = world_coords.iloc[:,2:5] #real world coordinates
X_cam = world_coords.iloc[:,0:2] # pixel coordinates OR OBSERVED VALUES

class Camera(object):

    def __init__(self, f_length, image_width,image_height):
        self.p = pred_guess = [272600.41,5193729.88,982,0,-0.349,4.89]
        self.f = f_length
        self.c = np.array([image_width,image_height]) 

    def projective_transform_project(self, pose, X_world):
        u, v = projective_transform(self.f, self.c[0], self.c[1], pose, X_world)
        U = np.array([u,v]).T
        return U

    def rotational_transform(self, pose, X_world):
        x,y,z = rotate(pose, X_world)
        X = np.array([x,y,z]).T
        return  X

    @staticmethod
    def residual(pose, self, X_world, X_cam):

      rotated = self.rotational_transform(pose, X_world)
      transformed = self.projective_transform_project(pose, rotated)
      return (transformed - X_cam).values.flatten()

    def estimate_pose(self,p0, X_world, X_cam):
      pose_Opt = least_squares(self.residual, p0, method = 'lm',args=(self, X_world,X_cam))
      return pose_Opt

Camera = Camera(f_length,width,length)
Pose = Camera.estimate_pose(Camera.p, X_world, X_cam).x

new_rotate = Camera.rotational_transform(Pose, X_world)
new_transform = Camera.projective_transform_project(Pose, new_rotate).T
fig, ax = plt.subplots(1, figsize=(12,8))
ax.imshow(io.imread("DSCF3272.JPG"))
ax.scatter(world_coords.iloc[:, 0], world_coords.iloc[:, 1], c="red", s=100)
ax.scatter(new_transform[0], new_transform[1], c="green", s=100)
plt.show()
