#!/usr/bin/env python 
from PIL import Image
import subprocess
import sys
import os
sys.path.append(os.getcwd())
#pic_folder = os.path.abspath("/home/dunbar/Spring2019.Courses/Computer Vision/Project1/DSCF3272.JPG")

im = Image.open('DSCF3272.JPG')
im.show()

#bashCommand = "identify -verbose DSCF3272.JPG | grep 'exif:FocalLengthIn35' "
f_length35  = 35
image_width = 6000
image_length = 4000
f_length = f_length35/(36*image_width)




