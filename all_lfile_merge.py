# In[]
import os
import sys
import platform
import pandas as pd
print(platform.python_version())
print(sys.path)

# %%
# sideKPcsv = pd.read_csv('data/COCO_Side.csv', index_col='name')
sideKPcsv = pd.read_csv('data/COCO_Side.csv', index_col=0)
sideKPcsv

# %%
side_SEGCSV = pd.read_csv(
    'data/reorganized/segmentation_extracted.csv', index_col=0)
side_SEGCSV['name'] = side_SEGCSV.name.map(str)+'.jpg'
side_SEGCSV.keys()
side_SEGCSV
# %%

rearKPcsv = pd.read_csv('data/COCO_B3_rear.csv', index_col=0)
print(rearKPcsv.keys())
rearKPcsv['only_name'] = rearKPcsv['name'].str.split(
    '_').str[0]+'_'+rearKPcsv['name'].str.split('_').str[2]+'_'+rearKPcsv['name'].str.split('_').str[3]
# rearKPcsv

# print(rearKPcsv)

# %%
rearKPcsv

# %%
for entry in side_SEGCSV.index:
    try:
        name = side_SEGCSV.loc[entry, 'name']
        # side_height =
        # scaleCompare = pd.DataFrame(list(zip(name, side_height)),
        #                     columns=['name', 'side_height'])
        # scaleCompare = pd.DataFrame(list(name, side_height),
        #             columns=['name', 'side_height'])
        info = {
            'id': [entry],
            'name': [name],
            'side_height': [sideKPcsv.loc[name, 'side_height']]

        }
        # print(f"{name} {side_height}")
        print(info)
    except:
        pass
# %%
# side_seg_kp = pd.merge(sideKPcsv, side_SEGCSV, how='outer', on=['name'])
# print(side_seg_kp.keys())
# print(rearKPcsv.keys())
# %%

# %%
side_seg_kp = pd.merge(sideKPcsv, side_SEGCSV, how='inner', on=['name'])
side_seg_kp['only_name'] = side_seg_kp['name'].str.split(
    '_').str[0]+'_'+side_seg_kp['name'].str.split('_').str[2]+'_'+side_seg_kp['name'].str.split('_').str[3]
print(side_seg_kp.keys())
print(rearKPcsv.keys())
# %%
# rearKPcsv.rename(index=str, columns={'Reader_ID1': 'Reader_ID1_x',
#            'SITE_ID1': 'SITE_ID1_x', 'EVENT_TS1': 'EVENT_TS1_x'}, inplace=True)
renamed_rearKPCSV = rearKPcsv.rename(columns={
    'id': 'id_rear',
    'name': 'name_rear',
    'weight': 'weight__from_rear_image',
    'keypoints': 'keypoints_rear',
    'rescaled_keypoints': 'rescaled_keypoints_rear',
    'original_image_height': 'original_image_height_rear',
    'original_image_width': 'original_image_width_rear',
    'rescaled_image_height': 'rescaled_image_height_rear',
    'rescaled_image_width': 'rescaled_image_width_rear'
})

# all_merrged = pd.merge(side_seg_kp, side_SEGCSV, how='outer', on=['name'])


# %%
all_merrged = pd.merge(side_seg_kp, renamed_rearKPCSV,
                       how='inner', on=['only_name'])
all_merrged
# %%
all_merrged.keys()

# %%
all_merrged.to_csv(os.path.join('data', 'all_merrged.csv'))
# %%
