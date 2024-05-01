
class Help:
    helpinfo = '''
usage: python -m pyls [option] ... [--help | --filter=file | --filter=dir | <> ] ...
Options:
-A     : prints all files and directories
-l     : prints the files/directories vertically with additional information
-r 	   : prints the list in reverse
-t     : sorts the list in ascending order of time modified
<>     : prints the list of files in the directory or the file itself when relative path is provided 
-h     : prints in human readable format of file/directory size
--help : prints the help/usage document
--filter=dir     : prints the directories only inside the directory
--filter=file    : prints the files within the directory
'''