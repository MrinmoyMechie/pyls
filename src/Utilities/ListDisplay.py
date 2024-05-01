from datetime import datetime

def getDate(secs):
    return datetime.fromtimestamp(secs).strftime("%b %d %I:%M")

def getSize(bytes):
    val = float(bytes)/1024.0/1024.0
    if val >= 1:
        return str(round(val, 1)) + "G"
    val = float(bytes)/1023.0
    if val >= 1:
        return str(round(val, 1)) + "K"
    return str(bytes)
    
        
def listDisplay(data_array, args):
    if "-h" in args:
        for data in data_array:
            print("{}\t{}\t{}\t{}".format(data['permissions'], getSize(data['size']), getDate(data['time_modified']), data['name']))
    else:
        for data in data_array:
            print("{}\t{}\t{}\t{}".format(data['permissions'], data['size'], getDate(data['time_modified']), data['name']))