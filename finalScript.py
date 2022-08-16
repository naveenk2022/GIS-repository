# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:31:45 2022

@author: navee
"""
#Importing the necessary libraries
import cv2
import pandas as pd
import detect_modified
import os
import shutil
import pathlib
#Going through individual geospatial videos to create image files for each frame
files = pathlib.Path(r"C:\Users\navee\Desktop\YOLOV5\Input videos")
for f in files.iterdir():
    currentFrame = 1
    vid = cv2.VideoCapture(str(f))
    while(True):
        ret,frame = vid.read()
        if ret:
            try:
                name=r"C:\Users\navee\Desktop\YOLOV5\Output frames\frame" + str(currentFrame) + '.jpg'
                cv2.imwrite(name, frame)
                currentFrame += 1
            except:
                pass
        else:
            break
    vid.release()
    #Creating empty lists for the index of the frames and the detections in each frame
    frameCount = 1
    frameList = []
    detections = []
    #importing the model and the weights 
    detections = detect_modified.runModel(source=r"C:\Users\navee\Desktop\YOLOV5\Output frames", weights = r"C:\Users\navee\Desktop\YOLOV5\trained_weights\weights_small_nav.pt",conf_thres = 0.2)
    #Indexing the frames and making a list of the number of detections in each individual frame
    for img in detections:
        frameList.append(frameCount)
        frameCount = frameCount + 1
    #creating a dataframe with the frame index and the detection count
    dict = {'Frames': frameList, "Detections":detections}
    df = pd.DataFrame(dict)
    #Writing the dataframe as a comma seperated value file
    file_name = os.path.basename(str(f))
    df.to_csv(r"C:\Users\navee\Desktop\YOLOV5\Output CSV\output" + str(file_name) + ".csv", index = False)
    #deleting the already processed frame images in order to prevent unnecessary usage of storage space
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
