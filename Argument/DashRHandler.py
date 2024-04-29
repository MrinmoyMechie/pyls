
def dashRHandler(data_array, args):
    if '-r' in args:
        return data_array[::-1]
    else:
        return data_array