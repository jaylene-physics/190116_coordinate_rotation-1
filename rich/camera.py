'''

'''

import numpy as np
import pandas as pd
import scipy.optimize as so
import matplotlib.pyplot as plt

# local imports
import * from coord_rotation
import * from projective_transform

class Camera(object):
    ''' Build camera based on camera's realworld coords, '''
    def __init__(self, x_cam, y_cam, z_cam, yaw, pitch, roll, focal):
        self.pose = np.matrix([x_cam, y_cam, z_cam, yaw pitch, roll])
        self.focal = focal
        self.c = np.array([None,None])

    """ This function performs the projective transform on generalized coordinates in the camera reference frame. """
    def projective_transform(self,x):

        pass

    """ This function performs the translation and rotation from world coordinates into generalized camera coordinates. """
    def rotational_transform(self,X):

        pass

    """ This function adjusts the pose vector such that the difference between the observed pixel coordinates u_gcp
    and the projected pixels coordinates of X_gcp is minimized. """
    def estimate_pose(self,X_gcp,u_gcp):

        pass

##########################################################################################
###############################        MAIN       ########################################
##########################################################################################
