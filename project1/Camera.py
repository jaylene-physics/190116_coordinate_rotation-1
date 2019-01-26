from projective_transform import *
from rotation import *
from scipy.optimize import least_squares
import numpy as np

f_length35  = 35
width = 6000
length = 4000
f_length = f_length35/(36*width)
world_coords = pd.read_csv("Image_constrain.txt", delimiter="|")
X_world = world_coords.iloc[:,2:5] #real world coordinates
X_cam = world_coords.iloc[:,0:1] # pixel coordinates OR OBSERVED VALUES

class Camera(object):

    def __init__(self, f_length35, image_width,image_length):
        self.p = pred_guess = [272634.41,5193729.88,982,0,-0.349,4.89]
        self.f = f_length
        self.c = np.array([image_width,image_length])  

    def projective_transform_project(self,X_world):
        u, v = projective_transform(X_world)
        U = np.array([[u],[v]]).Transpose()
        return U

    def rotational_transform(self,X_world):
        x,y,z = rotate(self,X_world)
        X = np.array([[x],[y],[z]]).Transpose()
        return X

    def residual(self,X_world,X_true):
	    return projective_transform_project(self,rotational_transform(self,X_world)) - X_cam


    def estimate_pose(self,X_world,X_cam):
    	X_true = X_cam
    	pose_Opt = least_squares(residual, self.p, method = 'lm',args=(X_world,X_true))
    	return pose_Opt

Camera = Camera(35,width,length)
Pose = Camera.estimate_pose(X_world,X_cam)
print(Pose)