
from Utilities import listDisplay, simpleDisplay

def displayHandler(data_array, args):
    if '-l' in args:
        listDisplay(data_array, args)
    else:
        simpleDisplay(data_array)
