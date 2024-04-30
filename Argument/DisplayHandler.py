
from Utilities import listDisplay, simpleDisplay

def displayHandler(data_array, args):
    if '-l' in args:
        listDisplay(data_array)
    else:
        simpleDisplay(data_array)
