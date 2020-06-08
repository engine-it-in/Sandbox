import docx
from docx import Document
"""Create structure of folder with files"""

FILE = 0 # it's file with structure of folder

structura = 0 # it's dictionary with name of folder

def create_folder_courses(FILE):
    """ ! """
    structura = open_file(FILE)
    create_folders(structura)
    print('Success')


def open_file(FILE):
    """ ! """
    pass


def create_folders(structura):
    """ ! """
    pass


if __name__ == '__main__':
    print("Compile :-) ")
