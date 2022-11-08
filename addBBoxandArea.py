import json
file_name = 'data/test.json'


def bbox(arr: list):

    pass


with open(file_name, "r+") as jsonFile:
    data = json.load(jsonFile)
    # print(data)
    for items in data['annotations']:
        print(items["keypoints"])

        seperated = [[x] for x in range(len(items["keypoints"]), 3)]
        # items["license"] = 1
        # print(type(items))
        # print(items)
        break

    # data["location"] = "NewPath"

    # jsonFile.seek(0)  # rewind
    # json.dump(data, jsonFile)
    # jsonFile.truncate()
