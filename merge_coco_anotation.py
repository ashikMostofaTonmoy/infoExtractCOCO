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
# original_coco_path = 'data/annotations_trainval2014/annotations/person_keypoints_val2014.json'

# %%
# load json files
file_1 = json.load(open(file_1_path))
file_2 = json.load(open(file_2_path))
# coco_original = json.load(open(original_coco_path))
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
df1_images = pd.DataFrame(file_1['images'])
df1_images.head()

# %%
df1_annotation = pd.DataFrame(file_1['annotations'])
df1_annotation

# %%
df1_categories = pd.DataFrame(file_1['categories'])
df1_categories

# %%
max_image_id = df1_images['id'].max()
max_annotation_id = df1_annotation['id'].max()
max_categories_id = df1_categories['id'].max()

# %%
df1_images.keys()

# %%
for key in file_2:
    print(key)
    for item in file_2[key]:
        print(item)
        # print()

# %%
df2_annotation = pd.DataFrame(file_2['annotations'])
df2_annotation
# %%
df2_images = pd.DataFrame(file_2['images'])
df2_images

# %%
df2_categories = pd.DataFrame(file_2['categories'])
df2_categories


# %%
# cell for changing image id in image section and annotaion section
if file_2["annotations"][1]['image_id'] == file_2["images"][1]['id']:
    print('matched')
# %%
temp_file2 = file_2
# temp_list = []
for item in temp_file2['images']:
    print(f"id: {item['id']}")
    anno_index = df2_annotation.index[df2_annotation['image_id'] == item['id']].tolist(
    )
    print(anno_index)
    item['id'] += max_image_id
    print(f"id_after change: {item['id']}")
    for ids in anno_index:
        anid = temp_file2["annotations"][ids]['image_id']
        print(f"annoId: {anid}")
        temp_file2["annotations"][ids]['image_id'] = item['id']
        anid = temp_file2["annotations"][ids]['image_id']
        print(f"annoId after change: {anid}")
    # print(anno_index)
    # for item in file_2[key]:
    #     print(item)
# info = pd.DataFrame(temp_list, columns=['id_image', 'anoo_index'])


# %%
# anno_index = df2_annotation.index[df2_annotation['image_id'] == 5].tolist()
# %%
# # test on original coco
# temp_file2 = coco_original
# df2_annotation_coco = pd.DataFrame(temp_file2['annotations'])
# df2_annotation_coco

# temp_list = []
# for item in temp_file2['images']:
#     # print(item['id'])
#     anno_index = df2_annotation_coco.index[df2_annotation_coco['image_id'] == item['id']].tolist(
#     )
#     temp_list.append([item['id'], anno_index])
#     # print(anno_index)

#     # for item in file_2[key]:
#     #     print(item)
# info = pd.DataFrame(temp_list, columns=['id', 'anoo'])


# %%
# info
# info.to_csv('data/'+'testself_check.csv')
# %%
df_temp2_annotation = pd.DataFrame(temp_file2['annotations'])
df_temp2_annotation
# %%
max_annotation_id
# %%
# cell for changing categories id in categories section and annotaion section
for item in temp_file2['categories']:
    print(f"cat_id: {item['id']}")
    cat_index = df2_annotation.index[df2_annotation['category_id'] == item['id']].tolist(
    )
    print(cat_index)
    item['id'] += max_categories_id
    print(f"id_after change: {item['id']}")
    for ids in cat_index:
        cat_id = temp_file2["annotations"][ids]['category_id']
        print(f"cat_Id: {cat_id}")
        temp_file2["annotations"][ids]['category_id'] = item['id']
        cat_id = temp_file2["annotations"][ids]['category_id']
        print(f"cat_Id after change: {cat_id}")

# %%
df_temp2_categories = pd.DataFrame(temp_file2['categories'])
df_temp2_categories

# %%
for item in temp_file2['annotations']:
    print(f"annota_id: {item['id']}")
    item['id'] += max_annotation_id
    print(f"id_after change: {item['id']}")
# %%
