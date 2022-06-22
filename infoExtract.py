# In[]:

import json
from lib2to3.pytree import type_repr
from matplotlib.font_manager import _Weight
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


# In[]:
# f_B3_rear = open('data/input/Rear/COCO_B3_rear.json')
# # f_B3_rear = open('data/input/COCO_B3_rear.json')

# COCO_B3_rear = json.load(f_B3_rear)

f_COCO_Side = open('data/input/Side/COCO_Side.json')
# f_COCO_Side = open('data/input/COCO_Side.json')

COCO_Side = json.load(f_COCO_Side)


# # In[]:

# COCO_B3_rear.keys()

# # %%
# COCO_Side.keys()

# # %%
# COCO_Side['images']

# %%
COCO_Side['annotations']
# # %%
# COCO_Side['annotations'][0]['keypoints']

# # %%
# COCO_Side['images'][0]

# %%
type(COCO_Side['images'])

sideImages = pd.DataFrame.from_dict(
    COCO_Side['images']).set_index('id')

# sideAnnotation = pd.DataFrame.from_dict(
#     COCO_Side['annotations']).set_index('image_id')

sideAnnotation = pd.DataFrame.from_dict(
    COCO_Side['annotations']).set_index('id')

# %%


def rescale(prevweidth, prevheight, xloc, yloc):
    return 1900*yloc/prevweidth, 1425*xloc/prevheight


def distance(point_ax, point_ay, point_bx, point_by):
    return round(((point_by-point_ay)**2+(point_bx-point_ax)**2)**0.5)


# for entry in sideImages.index:
for entry in sideAnnotation.index:
    # df.loc[df['shield'] > 6, ['max_speed']]
    name = sideImages.loc[sideAnnotation.loc[entry, 'image_id'], 'file_name']
    # name = sideImages.loc[entry, 'file_name']
    keypoint = sideAnnotation.loc[entry, 'keypoints']
    height = sideImages.loc[sideAnnotation.loc[entry, 'image_id'], 'height']
    width = sideImages.loc[sideAnnotation.loc[entry, 'image_id'], 'width']

    rescaled_keypoint = map()
    print(len(keypoint))
    # print(type(keypoint[0]))
    # print(f"{entry}: {name} : {keypoint} :")
    # print(f"{entry}: {name} Height: {height} weidht: {width} ")

# %%
# sideImages
# sideAnnotation

# %%
