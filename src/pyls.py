import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from Utilities import JsonParser
from Argument import ArgumentService

def argfn(arguments, file_path):
    json_parser = JsonParser(file_path)
    data = json_parser.data
    argument_service = ArgumentService(data, arguments)

def inputfn():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('File Selection')
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getOpenFileName(window, "Select File", "", "All\
                                                Files (*)", options=options)
    return file_path


def main():
    #file_path = inputfn()
    file_path = "./src/structure.json"
    arguments = sys.argv
    argfn(arguments[1:], file_path)

if __name__ == "__main__":
    main()
    

