
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

# In[]:

f_COCO_Side = open('data/input/Side/COCO_Side.json')
# f_COCO_Side = open('data/input/COCO_Side.json')

COCO_Side = json.load(f_COCO_Side)

# %%
COCO_Side['annotations']

# %%
type(COCO_Side['images'])

sideImages = pd.DataFrame.from_dict(
    COCO_Side['images']).set_index('id')

sideAnnotation = pd.DataFrame.from_dict(
    COCO_Side['annotations']).set_index('id')

# %%

desired_width = 1900


def imgHeight(heightOrigine, widthOrigine, img_width=desired_width):
    return img_width * heightOrigine / widthOrigine


def Xrescale(xloc, prevweidth, img_width=desired_width):
    return img_width*xloc/prevweidth


def Yrescale(yloc, prevheight, postHeight):
    return postHeight*yloc/prevheight


def distance(point_ax, point_ay, point_bx, point_by):
    return round(((point_by-point_ay)**2+(point_bx-point_ax)**2)**0.5)


# %%
# for entry in sideAnnotation.index:
annoid = 1
for entry in range(annoid, annoid+1):
    # df.loc[df['shield'] > 6, ['max_speed']]
    name = sideImages.loc[sideAnnotation.loc[entry, 'image_id'], 'file_name']
    # name = sideImages.loc[entry, 'file_name']
    keypoint = sideAnnotation.loc[entry, 'keypoints']
    height = sideImages.loc[sideAnnotation.loc[entry, 'image_id'], 'height']
    width = sideImages.loc[sideAnnotation.loc[entry, 'image_id'], 'width']

    currtnt_hight = imgHeight(height, width)

    rewi = round(Xrescale(width, width))
    rehi = round(Yrescale(height, height, currtnt_hight))
    img = np.zeros((height, width, 3), np.uint8)
    rescaledimg = np.zeros((rehi, rewi, 3), np.uint8)
    print(entry, name)
    print(img.shape)
    print(rescaledimg.shape)
    font = cv.FONT_HERSHEY_SIMPLEX
    rescaled_keypoint = []
    for i in range(0, len(keypoint), 3):
        rescaled_keypoint.append(
            Xrescale(keypoint[i], width))
        rescaled_keypoint.append(
            Yrescale(keypoint[i+1], height, currtnt_hight))
        rescaled_keypoint.append(keypoint[i+2])

    # both lists, with columns specified
    scaleCompare = pd.DataFrame(list(zip(keypoint, rescaled_keypoint)),
                                columns=['original', 'scaled'])

    # print(keypoint)
    # print(rescaled_keypoint)
    print(scaleCompare)
# %%
    # visualise scaled image
    for i in range(0, len(rescaled_keypoint), 3):
        print(i)
        cv.circle(rescaledimg, (round(rescaled_keypoint[i]), round(
            rescaled_keypoint[i+1])), 10, (245, 221, 66), -1)
        cv.putText(rescaledimg, f"{int((i/3)+1)}{i,i+1} ", (round(rescaled_keypoint[i]), round(
            rescaled_keypoint[i+1])), font, 4, (245, 221, 66), 2, cv.LINE_AA)
    # visualize normal image
    for i in range(0, len(keypoint), 3):
        cv.circle(img, (round(keypoint[i]), round(
            keypoint[i+1])), 10, (245, 221, 66), -1)
        cv.putText(img, f"{int((i/3)+1)} {i,i+1}", (round(keypoint[i]), round(
            keypoint[i+1])), font, 3, (245, 221, 66), 2, cv.LINE_AA)

f, axarr = plt.subplots(1, 2)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.imshow(rescaledimg)

# plt.imshow(rescaledimg)
plt.show()

# %%
