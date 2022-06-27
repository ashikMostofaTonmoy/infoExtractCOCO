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
rearKPcsv.keys()
# rearKPcsv

# print(rearKPcsv)

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
side_seg_kp = pd.merge(sideKPcsv, side_SEGCSV, how='outer', on=['name'])
side_seg_kp.keys()

# %%

# rearKPcsv.rename(index=str, columns={'Reader_ID1': 'Reader_ID1_x',
#            'SITE_ID1': 'SITE_ID1_x', 'EVENT_TS1': 'EVENT_TS1_x'}, inplace=True)
# all_merrged = pd.merge(side_seg_kp, side_SEGCSV, how='outer', on=['name'])

# %%
# rearKPcsv['name'].str.split('_').str[3]
rearKPcsv['only_name'] = rearKPcsv['name'].str.split(
    '_').str[0]+'_'+rearKPcsv['name'].str.split('_').str[2]+'_'+rearKPcsv['name'].str.split('_').str[3]

# %%
# +rearKPcsv['name'].str.split('_')[2]+'_'+rearKPcsv['name'].str.split('_')[3]
rearKPcsv['only_name']
# %%
