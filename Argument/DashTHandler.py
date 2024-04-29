
def dashTHandler(data_array, args):

    def argsort(seq):
        return sorted(range(len(seq)), key=seq.__getitem__)
    
    time = [data['time_modified'] for data in data_array]
    indices = argsort(time)

    if '-t' in args:
        return [data_array[indices[i]] for i in range(len(indices))]
    else:
        return data_array