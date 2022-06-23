# In[]
import os
import sys
import platform
import pandas as pd
print(platform.python_version())
print(sys.path)

# %%
sidecsv = pd.read_csv('data/COCO_Side.csv', index_col=0)
sidecsv

# %%
hard_features = pd.read_csv(
    'data/input/hard_features_With_weight_v2.csv', index_col=0)
hard_features
# %%
