#from .default import defaultFunction
from .DashAHandler import dashAHandler
from .DashRHandler import dashRHandler
from .DashTHandler import dashTHandler
from .FilterHandler import filterHandler

class ArgumentService:
    def __init__(self, data, args):

        object_array = [content for content in data['contents']]
        object_array = dashAHandler(object_array, args)
        object_array = dashTHandler(object_array, args)
        object_array = dashRHandler(object_array, args)
        object_array = filterHandler(object_array, args)
        #print(args)

        print([obj['name'] for obj in object_array])


        
    

