import json
file_name = 'test.json'
with open(file_name, "r+") as jsonFile:
    data = json.load(jsonFile)
    # print(data)
    for items in data['images']:
        items["license"] = 1
        # print(type(items))
        # print(items)
        # break

    # data["location"] = "NewPath"

    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile)
    jsonFile.truncate() 