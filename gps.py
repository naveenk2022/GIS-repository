# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:43:46 2022

@author: navee
"""
#importing the necessary libraries
import gpxpy
import gpxpy.gpx
import pathlib
import pandas as pd
import os
files = pathlib.Path(r"C:\Users\navee\Desktop\YOLOV5\GPS data")
# input for this loop is a GPX file, which has several attributes. The GPX files were obtained from the GPS tagger, and contain GPS coordinates, and other attributes as well.
# the attributes used for this script are the track and the time attributes. 
# the time attribute was in the form of hours:minutes:seconds.
# thetrack attribute has a segment attribute, which has it's own point attribute, which has it's own latitude and longitude attribute
for f in files.iterdir():
    # creating empty lists
    timelist = []
    maintimelist = []
    node_id = []
    seconds = []
    latitudes = []
    longitudes = []
    gpx_file = open(str(f), mode='rt', encoding='utf-8')
    gpx = gpxpy.parse(gpx_file)
    for track in gpx.tracks:
        for segment in track.segments:
                for point in segment.points:
                    # creating a list for the latitude and the longitude coordinates.
                    latitudes.append(point.latitude)
                    longitudes.append(point.longitude)
                    timelist = [(point.extensions[0].text)]
                    for time in timelist:
                        # converting the hours:minutes:seconds time attribute into a list with each element being a seperate entity 
                        import re
                        temp = re.findall(r'\d+', time)
                        res = list(map(int, temp))
                        maintimelist.append(res)
    for i in maintimelist:
        # creating an index of the seconds of video that have elapsed by converting hours and minutes into seconds. 
        second = i[0]*3600 + i[1]*60 +i[2]
        seconds.append(second)
    dict = {"Seconds":seconds,"Latitudes":latitudes, "Longitudes": longitudes }
    df = pd.DataFrame(dict)
    file_name = os.path.basename(str(f))
    # writing the GPS coordinate data in the form of a CSV file. 
    # this CSV file will then be merged with the CSV file containing the average number of tents detected in each second of the video. 
    df.to_csv(r"C:\Users\navee\Desktop\YOLOV5\GPS CSV\Output" + str(file_name) + ".csv", index = False)
