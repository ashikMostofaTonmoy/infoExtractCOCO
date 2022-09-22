# In[]:
import argparse
import pandas as pd
import json
import os
# import sys
import platform
# # import pandas as pd
print(f"using python: {platform.python_version()}")
# print(sys.path)

# %%


def merge_coco(fpath1, fpath2, outoutfilename):
    """
            fpath1 = 1stjson file
            fpath2 = 2nd json file 
            outoutfilename = outpt forlder name
    """

    # load json files
    file_1 = json.load(open(fpath1))
    file_2 = json.load(open(fpath2))
    """
    # %%
    type(file_1)
    # output: dict
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
    # 'metadata', 'creator', 'keypoint_colors', 'keypoints', 'skeleton'])"""
    # %%
    output = file_1

    # type(output)
    # %%

    # Calling DataFrame constructor on list
    df1_images = pd.DataFrame(file_1['images'])
    # df1_images.head()

    # %%
    df1_annotation = pd.DataFrame(file_1['annotations'])
    # df1_annotation

    # %%
    df1_categories = pd.DataFrame(file_1['categories'])
    # df1_categories

    # %%
    max_image_id = df1_images['id'].max()
    max_annotation_id = df1_annotation['id'].max()
    max_categories_id = df1_categories['id'].max()

    # %%
    # df1_images.keys()

    # %%
    df2_annotation = pd.DataFrame(file_2['annotations'])
    # df2_annotation
    # %%
    df2_images = pd.DataFrame(file_2['images'])
    # df2_images

    # %%
    df2_categories = pd.DataFrame(file_2['categories'])
    # df2_categories

    # %%
    # cell for changing image id in image section and annotaion section
    # if file_2["annotations"][1]['image_id'] == file_2["images"][1]['id']:
    #     print('matched')
    # %%
    temp_file2 = file_2

    for item in temp_file2['images']:
        # print(f"id: {item['id']}")
        anno_index = df2_annotation.index[df2_annotation['image_id'] == item['id']].tolist(
        )
        # print(anno_index)
        item['id'] += max_image_id
        # print(f"id_after change: {item['id']}")
        for ids in anno_index:
            anid = temp_file2["annotations"][ids]['image_id']
            # print(f"annoId: {anid}")
            temp_file2["annotations"][ids]['image_id'] = item['id']
            anid = temp_file2["annotations"][ids]['image_id']
            # print(f"annoId after change: {anid}")

    # %%
    df_temp2_annotation = pd.DataFrame(temp_file2['annotations'])
    df_temp2_annotation
    # %%
    max_annotation_id
    # %%
    # cell for changing categories id in categories section and annotaion section
    for item in temp_file2['categories']:
        # print(f"cat_id: {item['id']}")
        cat_index = df2_annotation.index[df2_annotation['category_id'] == item['id']].tolist(
        )
        # print(cat_index)
        item['id'] += max_categories_id
        # print(f"id_after change: {item['id']}")
        for ids in cat_index:
            cat_id = temp_file2["annotations"][ids]['category_id']
            # print(f"cat_Id: {cat_id}")
            temp_file2["annotations"][ids]['category_id'] = item['id']
            cat_id = temp_file2["annotations"][ids]['category_id']
            # print(f"cat_Id after change: {cat_id}")

    # %%
    df_temp2_categories = pd.DataFrame(temp_file2['categories'])
    df_temp2_categories

    # %%
    for item in temp_file2['annotations']:
        # print(f"annota_id: {item['id']}")
        item['id'] += max_annotation_id
        # print(f"id_after change: {item['id']}")
    # %%

    for key in temp_file2:
        try:
            # print(key)
            for items in temp_file2[key]:
                output[key].append(items)
            #     # list.append
            #     print(items)
        except:
            pass

    # %%
    # Serializing json
    try:
        os.makedirs(outoutfilename, exist_ok=True)
    except OSError as error:
        print(error)

    with open(os.path.join(outoutfilename, "merged_ds.json"), "w") as outfile:
        json.dump(output, outfile)


# %%
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # file paths
    file_1_path = 'data/ML/Goat_skeleton.json'
    file_2_path = 'data/ML_sojib/Goat_skeleton.json'
    merge_coco(file_1_path, file_2_path, "random")
