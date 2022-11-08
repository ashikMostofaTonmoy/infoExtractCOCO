import json
file_name = 'data/test.json'


def bbox(arr: list):
    xmin = min(arr[0])
    xmax = max(arr[0])
    ymin = min(arr[1])
    ymax = max(arr[1])
    width = xmax - xmin
    height = ymax - ymin
    # print(f" xmin : {xmin}, xmax : {xmax}, ymin : {ymin}, xmax : {ymax}")

    return [xmin, ymin, width, height]


def area(box: list):
    return int(box[2]*box[3])


with open(file_name, "r+") as jsonFile:
    data = json.load(jsonFile)
    # print(data)
    for items in data['annotations']:
        # print(f'kp: {items["keypoints"]}')
        # print(f'bbox prev: {items["bbox"]}')
        # print(f'area prev: {items["area"]}')
        # print(bbox(seperated))
        # print(area(bbox(seperated)))

        seperated = [[], []]

        # seperated = [items["keypoints"][x], items["keypoints"][x+1]
        #              for x in range(0, len(items["keypoints"]), 3)]
        for x in range(0, len(items["keypoints"]), 3):
            seperated[0].append(items["keypoints"][x])
            seperated[1].append(items["keypoints"][x+1])

        # seperated = [items["keypoints"][x], items["keypoints"][x+1]for x in range(0, len(items["keypoints"]), 3)]
        items["bbox"] = bbox(seperated)
        # print(seperated)

        items["area"] = area(items["bbox"])

        # print(f'bbox : {items["bbox"]}')
        # print(f'area : {items["area"]}')
        # items["license"] = 1
        # print(type(items))
        # print(items)
        # break

    # data["location"] = "NewPath"

    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile)
    jsonFile.truncate()
