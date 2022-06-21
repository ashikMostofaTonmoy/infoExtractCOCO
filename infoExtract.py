# In[]:

import json
import matplotlib.image as mpimg
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import pycocotools.coco as coco
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

# f_COCO_Side = open('data/input/Side/COCO_Side.json')
f_COCO_Side = open('data/input/COCO_Side.json')

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

# for entry in sideImages.index:
for entry in sideAnnotation.index:
    # df.loc[df['shield'] > 6, ['max_speed']]
    name = sideImages.loc[sideAnnotation.loc[entry, 'image_id'], 'file_name']
    # name = sideImages.loc[entry, 'file_name']
    keypoint = sideAnnotation.loc[entry, 'keypoints']

    print(f"{entry}: {name} : {keypoint}")

# %%
# sideImages
# sideAnnotation

# %%
