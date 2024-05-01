#from .default import defaultFunction
from .DashAHandler import dashAHandler
from .DashRHandler import dashRHandler
from .DashTHandler import dashTHandler
from .FilterHandler import filterHandler
from .ParserHandler import parserhandler
from .DisplayHandler import displayHandler
from Constants import Help

class ArgumentService:
    def __init__(self, data, args):

        if '--help' in args:
            print(Help.helpinfo)
        else:
            object_array = [content for content in data['contents']]
            object_array = parserhandler(object_array, data, args)
            object_array = dashAHandler(object_array, args)
            object_array = dashTHandler(object_array, args)
            object_array = dashRHandler(object_array, args)
            object_array = filterHandler(object_array, args)
            displayHandler(object_array, args)


        
    

