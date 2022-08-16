# -*- coding: utf-8 -*-
"""
Created on Fri May 20 07:31:54 2022

@author: navee
"""
# A script to obtain the average number of tents detected per second.
# One second of the video has 30 frames. 30 frames are condensed into a single second, and the average number of detections is taken.
import pathlib
import pandas as pd
import os
from os.path import join
files = pathlib.Path(r"C:\Users\navee\Desktop\YOLOV5\Output CSV")
for f in files.iterdir():
    secondCount = 0
    secondList = []
    data = pd.read_csv(str(f))
    detections = data.groupby(data.index // 30).mean()['Detections']
    for i in detections:
        
        secondList.append(secondCount)
        secondCount = secondCount + 1
    dict = ({"Seconds":secondList, "Mean_Detections":detections})
    df = pd.DataFrame(dict)
    file_name = os.path.basename(str(f))
    df.to_csv(r"C:\Users\navee\Desktop\YOLOV5\Mean CSV\output" + str(file_name),index = False)  
 