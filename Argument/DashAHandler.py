
def dashAHandler(data_array, args):
    if '-A' in args:
        return data_array
    else:
        return [data for data in data_array if data['name'].strip()[0] != '.']
