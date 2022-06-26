# In[]:
import json
import matplotlib.pyplot as plt
import os
import sys
import platform
import pandas as pd
print(platform.python_version())
print(sys.path)
# %%

file_dir = 'data/input/Rear/COCO_B3_rear.json'
f_B3_rear = open(file_dir)
COCO_B3_rear = json.load(f_B3_rear)
COCO_B3_rear
# %%
COCO_B3_rear.keys()
# %%
COCO_B3_rear['annotations']
# %%
type(COCO_B3_rear['images'])
# %%
COCO_B3_rear['images']
# %%
rearImage = pd.DataFrame(
    COCO_B3_rear['images']).set_index('id')
rearImage
# %%
rearAnnotation = pd.DataFrame(
    COCO_B3_rear['annotations']).set_index('id')
rearAnnotation
# %%


desired_width = 1900


def imgHeight(heightOrigine, widthOrigine, img_width=int(desired_width)):
    return int(img_width * heightOrigine / widthOrigine)


def Xrescale(xloc, prevweidth, img_width=desired_width):
    return img_width*xloc/prevweidth


def Yrescale(yloc, prevheight, postHeight):
    return postHeight*yloc/prevheight


def distance(point_ax, point_ay, point_bx, point_by):
    return round(((point_by-point_ay)**2+(point_bx-point_ax)**2)**0.5)


# %%
df_final = pd.DataFrame()
for entry in rearAnnotation.index:
    name = rearImage.loc[rearAnnotation.loc[entry, 'image_id'], 'file_name']
    # name = rearImage.loc[entry, 'file_name']
    keypoint = rearAnnotation.loc[entry, 'keypoints']
    height = rearImage.loc[rearAnnotation.loc[entry, 'image_id'], 'height']
    width = rearImage.loc[rearAnnotation.loc[entry, 'image_id'], 'width']

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

    infos = {
        'id': [rearAnnotation.loc[entry, 'image_id']],  # image id
        'name': [name],
        'weight': [str(name).split('_')[2]],  # iamge name
        'rescaled_rear_height': [distance(rescaled_keypoint[6], rescaled_keypoint[7], rescaled_keypoint[9], rescaled_keypoint[10])],
        'original_rear_height': [distance(keypoint[6], keypoint[7], keypoint[9], keypoint[10])],
        'rescaled_rear_width': [distance(rescaled_keypoint[3], rescaled_keypoint[4], rescaled_keypoint[0], rescaled_keypoint[1])],
        'original_rear_width': [distance(keypoint[3], keypoint[4], keypoint[0], keypoint[1])],
        'keypoints': [keypoint],
        'rescaled_keypoints': [rescaled_keypoint],
        'original_image_height': [height],
        'original_image_width': [width],
        'rescaled_image_height': [currtnt_hight],
        'rescaled_image_width': [desired_width]
        # 'rear_width': distance(rescaled_keypoint[], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4]),
        # 'rear_height': distance(rescaled_keypoint[0], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4]),
        # 'actual_width': distance(rescaled_keypoint[0], rescaled_keypoint[1], rescaled_keypoint[3], rescaled_keypoint[4])
    }
    df_temp = pd.DataFrame(infos)

    df_final = pd.concat([df_final, df_temp], ignore_index=True, axis=0)

# %%
df_final
# %%
print(scaleCompare)
# %%
saved_file_name = os.path.splitext(os.path.split(file_dir)[1])[0]
df_final.to_csv('data/'+saved_file_name+'.csv')
