# In[]:

import json
from lib2to3.pytree import type_repr
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
# sideImages
# sideAnnotation

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


df_final = pd.DataFrame()
# for entry in sideImages.index:
for entry in sideAnnotation.index:
    # df.loc[df['shield'] > 6, ['max_speed']]
    name = sideImages.loc[sideAnnotation.loc[entry, 'image_id'], 'file_name']
    # name = sideImages.loc[entry, 'file_name']
    keypoint = sideAnnotation.loc[entry, 'keypoints']
    height = sideImages.loc[sideAnnotation.loc[entry, 'image_id'], 'height']
    width = sideImages.loc[sideAnnotation.loc[entry, 'image_id'], 'width']

    currtnt_hight = imgHeight(height, width)

    rescaled_keypoint = []
    for i in range(0, len(keypoint), 3):
        rescaled_keypoint.append(
            Xrescale(keypoint[i], width))
        rescaled_keypoint.append(
            Yrescale(keypoint[i+1], height, currtnt_hight))
        rescaled_keypoint.append(keypoint[i+2])

    scaleCompare = pd.DataFrame(list(zip(keypoint, rescaled_keypoint)),
                                columns=['original', 'scaled'])
    # infos = {
    #     'id': sideAnnotation.loc[entry, 'image_id'],  # image id
    #     'name': name,  # iamge name
    #     'side_Length_wither': distance(rescaled_keypoint[0], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4]),
    #     'side_Length_shoulderbone': distance(rescaled_keypoint[3], rescaled_keypoint[4], rescaled_keypoint[6], rescaled_keypoint[7]),
    #     'side_F_Girth': distance(rescaled_keypoint[12], rescaled_keypoint[13], rescaled_keypoint[9], rescaled_keypoint[10]),
    #     'side_R_Girth': distance(rescaled_keypoint[24], rescaled_keypoint[25], rescaled_keypoint[21], rescaled_keypoint[22]),
    #     'side_height': distance(rescaled_keypoint[18], rescaled_keypoint[19], rescaled_keypoint[15], rescaled_keypoint[16])
    #     # 'rear_width': distance(rescaled_keypoint[], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4]),
    #     # 'rear_height': distance(rescaled_keypoint[0], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4]),
    #     # 'actual_width': distance(rescaled_keypoint[0], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4])
    # }

    infos = {
        'id': [sideAnnotation.loc[entry, 'image_id']],  # image id
        'name': [name],  # iamge name
        'side_Length_wither': [distance(rescaled_keypoint[0], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4])],
        'side_Length_shoulderbone': [distance(rescaled_keypoint[3], rescaled_keypoint[4], rescaled_keypoint[6], rescaled_keypoint[7])],
        'side_F_Girth': [distance(rescaled_keypoint[12], rescaled_keypoint[13], rescaled_keypoint[9], rescaled_keypoint[10])],
        'side_R_Girth': [distance(rescaled_keypoint[24], rescaled_keypoint[25], rescaled_keypoint[21], rescaled_keypoint[22])],
        'side_height': [distance(rescaled_keypoint[18], rescaled_keypoint[19], rescaled_keypoint[15], rescaled_keypoint[16])]
        # 'rear_width': distance(rescaled_keypoint[], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4]),
        # 'rear_height': distance(rescaled_keypoint[0], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4]),
        # 'actual_width': distance(rescaled_keypoint[0], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4])
    }
    df_temp = pd.DataFrame(infos)

    df_final = pd.concat([df_final, df_temp], ignore_index=True, axis=0)

    # df_final = df_final.append(infos, ignore_index=True)
    # print(scaleCompare)
    # scled =
    # print(len(keypoint))

    # print(type(keypoint[0]))
    # print(f"{entry}: {name} : {keypoint} :")
    # print(f"{entry}: {name} Height: {height} weidht: {width} ")
    # print(f"{keypoint} \n: {rescaled_keypoint}")


# %%
df_final
# %%
