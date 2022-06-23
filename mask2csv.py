# In[]
import cv2
import fname_ret as fnr
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# from numba import njit

# %%
# Source path of images
sourcePath = 'data/reorganized/data/input/images'

# destination path where files need to organized
destination = 'data/reorganized/'

ext = ('png', 'jpg', 'gif')    # Add image formats here

# file type that need to select
files = fnr.filname_ret(rootpath=sourcePath, file_types=ext).fileDirectory

# %%
if os.path.exists(destination) == False:
    try:
        os.makedirs(os.path.join(destination), exist_ok=True)
    except OSError as error:
        print(error)


# %%
def mask_change(file_list):
    df_final = pd.DataFrame()
    for fil in file_list:
        # print(fil)
        print(f"Processing {fil}")
        img = cv2.imread(fil, 0)

        # get unique counts from pixels
        un, cnt = np.unique(img, return_counts=True)

        # get the counnt as dictionary
        counted_pixels = dict(zip(un, cnt))

        datafilename = os.path.splitext(os.path.split(fil)[1])[0]
        # imagemap = {
        #     sticker: 2,
        #     cow: 1,
        #     background: 0
        # }
        infos = {
            'name': [str(datafilename).split('.')[0]],
            'sticker': [counted_pixels[2]],
            'cow': [counted_pixels[1]],
            'background': [counted_pixels[0]]

        }
        df_temp = pd.DataFrame(infos)

        df_final = pd.concat([df_final, df_temp], ignore_index=True, axis=0)
    # saved_file_name = os.path.splitext(os.path.split(file_dir)[1])[0]
    df_final.to_csv(os.path.join(destination, 'segmentation_extracted.csv'))


# %%
mask_change(files)
