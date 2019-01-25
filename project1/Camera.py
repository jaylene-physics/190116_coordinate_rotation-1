from projective_transform import *
from rotation import *
from scipy.optimize import least_squares

class Camera(object):
    def __init__(self, f_length35, image_width):
        self.p = None # Pose
        self.f = f_length35/(36*image_width) # Focal Length in Pixels
        self.c = np.array([None,None])  # 
        
    def projective_transform_project(self, X, X_cam, width, height):
        u, v = projective_transform(X,X_cam,self.f, width, height)
        """  
        This function performs the projective transform on generalized coordinates in the camera reference frame.
        """
        pass
    
    def rotational_transform(self,X_ene,X_cam):
        
        """  
        This function performs the translation and rotation from world coordinates into generalized camera coordinates.
        """
        pass
    
    def estimate_pose(self,X_gcp,u_gcp):
        """
        This function adjusts the pose vector such that the difference between the observed pixel coordinates u_gcp 
        and the projected pixels coordinates of X_gcp is minimized.
        """
        pass
f_length35  = 35
image_width = 6000
world_coords = pd.read_csv("Image_constrain.txt", delimiter="|")
world_coords_ene = world_coords.iloc[:,2:5]
print(world_coords_ene)
camera = Camera(f_length35, image_width)
#camera.projective_transform_project([0],[0])
