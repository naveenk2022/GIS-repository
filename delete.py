# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:57:33 2022

@author: navee
"""
#A script to delete the contents of the "Output Frames" folder if the production of video frames needs to be halted for any reason.
#This is a cumbersome process if done manually, so this script helps save time. Frames can number in the tens of thousands if the frame generation script is interrupted. 
import os
import shutil
folder = r'C:\Users\navee\Desktop\YOLOV5\Output frames'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
