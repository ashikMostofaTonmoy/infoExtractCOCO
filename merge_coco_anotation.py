# In[]:
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
df = pd.DataFrame(file_1['images'])
df.head()
# %%
df['id'].max()

# %%
df.keys()
# %%


if __name__ == "__main__":
    pass
