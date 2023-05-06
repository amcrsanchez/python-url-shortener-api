import json
def get():
    with open("./data/config.json", "r") as file:
        config = json.load(file)
    file.close()
    return config