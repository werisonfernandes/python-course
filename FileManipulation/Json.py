import json

with open("../database/json.json", "r") as file:
    dictionary = json.load(file)
    for key, value in dictionary.items():
        print(key + ":" + value)
    #Save json in another file
    with open("../database/json-savedbyapp.json", "w") as json_file:
        json.dump(dictionary, json_file)
