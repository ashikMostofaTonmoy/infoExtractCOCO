# In[]:
from email.mime import image
from multiprocessing.sharedctypes import Value
import pandas as pd
import json
# import matplotlib.pyplot as plt
import os
import sys
import platform
# import pandas as pd
print(platform.python_version())
print(sys.path)

# %%
# file paths
file_1_path = 'data/ML/Goat_skeleton.json'
file_2_path = 'data/ML_sojib/Goat_skeleton.json'

# %%
# load json files
file_1 = json.load(open(file_1_path))
file_2 = json.load(open(file_2_path))

# %%
type(file_1)
# %%
# show keys
file_1.keys()
# output: dict_keys(['images', 'categories', 'annotations'])

# %%
type(file_1['images'])
# all output: list
# %%
len(file_1['images'])
# %%
len(file_1['annotations'])
# %%
file_1['images'][3]
# %%
type(file_1['images'][0])
# output : dict
# %%
file_1['images'][0].keys()
# output: dict_keys(['id', 'dataset_id', 'category_ids',
# 'path', 'width', 'height', 'file_name', 'annotated',
# 'annotating', 'num_annotations', 'metadata', 'milliseconds',
# 'events', 'regenerate_thumbnail', 'is_modified'])

# %%
file_1['annotations'][0].keys()
# output: dict_keys(['id', 'image_id', 'category_id',
# 'dataset_id', 'segmentation', 'area', 'bbox', 'iscrowd',
# 'isbbox', 'creator', 'width', 'height', 'color', 'keypoints',
# 'metadata', 'milliseconds', 'events', 'num_keypoints'])

# %%
file_1['annotations'][0]
# %%
file_1['categories'][0].keys()
# output: dict_keys(['id', 'name', 'supercategory', 'color',
# 'metadata', 'creator', 'keypoint_colors', 'keypoints', 'skeleton'])
# %%
output = file_1

type(output)
# %%

# Calling DataFrame constructor on list
df_images = pd.DataFrame(file_1['images'])
df_images.head()
# %%
df_images['id'].max()

# %%
df_images.keys()

# %%
for key in file_2:
    print(key)
    for item in file_2[key]:
        print(item)

# %%
df_annotation = pd.DataFrame(file_2['annotations']).set_index('id')
df_annotation
# %%
df2_images = pd.DataFrame(file_2['images']).set_index('id')
df2_images
# %%
for key in file_2:
    print(key)
    for item in file_2[key]:
        print(item)

# %%
if file_2["annotations"][1]['image_id'] == file_2["images"][1]['id']:
    print('matched')
# %%
