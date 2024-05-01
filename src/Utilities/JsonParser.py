import json
class JsonParser:
    def __init__(self, loc):
        with open(loc) as json_file:
            data = json.load(json_file)
        self.data = data