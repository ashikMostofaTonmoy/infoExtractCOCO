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
f_COCO_Side = open('data/input/COCO_Side.json')

COCO_Side = json.load(f_COCO_Side)

# %%
COCO_Side['annotations'][0]['keypoints']
# %%
# Create a black image
img = np.zeros((3120, 4160, 3), np.uint8)
c1 = [1637.53, 764.34]
# int(enumerate(c1))
# map(int,(c1))
font = cv.FONT_HERSHEY_SIMPLEX
cv.circle(img, (1637, 764), 23, (245, 221, 66), -1)
cv.putText(img, '1', (1637, 764), font, 8, (245, 221, 66), 2, cv.LINE_AA)

cv.circle(img, (3716, 963), 33, (245, 105, 66), -1)
cv.putText(img, '2', (3716, 963), font, 8, (245, 221, 66), 2, cv.LINE_AA)

cv.circle(img, (1552, 1409), 23, (129, 245, 66), -1)
cv.putText(img, '3', (1552, 1409), font, 8, (245, 221, 66), 2, cv.LINE_AA)

cv.circle(img, (2136, 1798), 13, (66, 203, 245), -1)
cv.putText(img, '4', (2136, 1798), font, 8, (245, 221, 66), 2, cv.LINE_AA)

cv.circle(img, (2100, 755), 33, (66, 84, 245), -1)
cv.putText(img, '5', (2100, 755), font, 8, (245, 221, 66), 2, cv.LINE_AA)

cv.circle(img, (3262, 2604), 33, (182, 66, 245), -1)
cv.putText(img, '6', (3262, 2604), font, 8, (245, 221, 66), 2, cv.LINE_AA)

cv.circle(img, (3206, 586), 33, (245, 66, 221), -1)
cv.putText(img, '7', (3206, 586), font, 8, (245, 221, 66), 2, cv.LINE_AA)

cv.circle(img, (3254, 1633), 33, (245, 66, 132), -1)
cv.putText(img, '8', (3254, 1633), font, 8, (245, 221, 66), 2, cv.LINE_AA)

cv.circle(img, (3015, 659), 33, (245, 66, 66), -1)
cv.putText(img, '9', (3015, 659), font, 8, (245, 221, 66), 2, cv.LINE_AA)


# im = cv.circle(img, (647, 63), 63, (0, 0, 255), -1)
# cv.imshow("img", im)
plt.imshow(img)
plt.show()
# plt(cv.circle(img,(447,63), 63, (0,0,255), -1))
# %%
