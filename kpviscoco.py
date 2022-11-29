# %%
import cv2 as cv
import numpy as np
import json
import matplotlib.image as mpimg
import matplotlib.patches as patches
import matplotlib.pyplot as plt
# import pycocotools.coco as coco
import sys
import platform
import pandas as pd
print(platform.python_version())
print(sys.path)

# %%
# file_dir = 'data/input/Rear/COCO_B3_rear.json'
file_dir = 'data/train.json'
# f_COCO_Side = open('data/input/COCO_Side.json')
f_COCO = open(file_dir)
COCO_ = json.load(f_COCO)

# %%
COCO_['annotations']

# %%
type(COCO_['images'])

Images = pd.DataFrame.from_dict(
    COCO_['images']).set_index('id')

Annotation = pd.DataFrame.from_dict(
    COCO_['annotations']).set_index('id')

# %%
entry = 223
name = Images.loc[Annotation.loc[entry, 'image_id'], 'file_name']
# name = sideImages.loc[entry, 'file_name']
keypoint = Annotation.loc[entry, 'keypoints']
bbox = Annotation.loc[entry, 'bbox']
height = Images.loc[Annotation.loc[entry, 'image_id'], 'height']
width = Images.loc[Annotation.loc[entry, 'image_id'], 'width']
img = np.zeros((height, width, 3), np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
# visualize normal image
for i in range(0, len(keypoint), 3):
    cv.circle(img, (round(keypoint[i]), round(
        keypoint[i+1])), 10, (245, 221, 66), -1)
    cv.putText(img, f"{int((i/3)+1)} {i,i+1}", (round(keypoint[i]), round(
        keypoint[i+1])), font, 3, (245, 221, 66), 2, cv.LINE_AA)
# f, axarr = plt.subplots(1, 2)

# represents the top left corner of rectangle
start_point = (bbox[0], bbox[1])
# represents the bottom right corner of rectangle
end_point = (bbox[0]+bbox[2], bbox[1]+bbox[3])

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

img = cv.rectangle(img, start_point, end_point, color, thickness)
plt.imshow(img)
plt.show()

# %%


# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
