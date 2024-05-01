def argsort(arr):
    indices = list(range(len(arr)))
    mergesort_indices(arr, indices)
    return indices

def mergesort_indices(arr, indices):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        left_indices = indices[:mid]
        right_half = arr[mid:]
        right_indices = indices[mid:]

        mergesort_indices(left_half, left_indices)
        mergesort_indices(right_half, right_indices)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                indices[k] = left_indices[i]
                i += 1
            else:
                arr[k] = right_half[j]
                indices[k] = right_indices[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            indices[k] = left_indices[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            indices[k] = right_indices[j]
            j += 1
            k += 1



def dashTHandler(data_array, args):

    #def argsort(seq):
    #    return sorted(range(len(seq)), key=seq.__getitem__)
    
    time = [data['time_modified'] for data in data_array]
    indices = argsort(time)

    if '-t' in args:
        return [data_array[indices[i]] for i in range(len(indices))]
    else:
        return data_array