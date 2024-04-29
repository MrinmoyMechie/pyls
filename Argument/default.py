from Utilities import simpleDisplay

def defaultFunction(data, args):
    json_top_level = data['contents']
    if '-A' not in args:
        simpleDisplay([content['name'] for content in json_top_level if content['name'].strip()[0] != '.'])
    else:
        simpleDisplay([content['name'] for content in json_top_level])
