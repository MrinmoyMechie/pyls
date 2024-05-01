import sys
def filterHandler(data_array, args):
    filter_type = []
    available_types = {"file": 0, "dir": 0}
    count = 0
    for arg in args:
        if '--filter=' in arg:
            count += 1
            cur_filter_type = arg[arg.find("=")+1:]
            if cur_filter_type in available_types:
                available_types[cur_filter_type] = 1
            else:
                print("error: '{}' is not a valid filter criteria. Available \
filters are 'dir' and 'file'".format(cur_filter_type))
                sys.exit(1)
    if count > 1:
        print("error: multiple filter")
        sys.exit(1)
    
    files = []
    dirs = []
    for data in data_array:
        if 'contents' in data.keys():
            dirs.append(data)
        else:
            files.append(data)

    if available_types['file'] == 1 and available_types['dir'] == 1:
        return data_array
    elif available_types['file'] == 1:
        return files
    elif available_types['dir'] == 1:
        return dirs
    else:
        return data_array
    
        