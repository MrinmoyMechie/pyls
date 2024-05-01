import sys

def sequenceIsPresent(sequence, data):

    if 'contents' not in data.keys():
        return None
    else:
        for content in data['contents']:
            if content['name'] == sequence:
                return content
        return None
        
def pathFinder(path, data):
    sequences = path.split("/")
    parent = data

    while len(sequences) != 0:
        sequence = sequences.pop(0)
        parent = sequenceIsPresent(sequence, parent)
        if parent == None:
            print("error: cannot access '{}': No such file or directory"\
                  .format(path))
            sys.exit(1)
    return parent

def parserhandler(data_array, data, args):

    filtered_args = [element for element in args \
                     if not element.startswith("-")]
    filtered_args = [element[2:] if element.startswith("./") \
                      else element for element in filtered_args]

    if len(filtered_args) == 0:
        return data_array
    elif len(filtered_args) > 1:
        print("error: Multiple file parser arguments")
        sys.exit(1)
    for arg in filtered_args:
        parent = pathFinder(arg, data)
        if 'contents' not in parent.keys():
            return [parent]
        else:
            return [content for content in parent['contents']]
