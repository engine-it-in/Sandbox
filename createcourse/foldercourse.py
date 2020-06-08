import docx
from docx import Document
"""Create structure of folder with files"""

FILE = 0 # it's file with structure of folder

structura = 0 # it's dictionary with name of folder

def create_folder_courses(FILE):
    """ Create folder of courses
    """
    structura = open_file(FILE)
    create_folders(structura)
    print('Success')


def open_file(FILE):
    """ Open file structure and modify it in dict """
    return structura


def create_folders(structura):
    """ Create folders by dict  """
    print('Success or Fail')


if __name__ == '__main__':
    print("You are win. I'm compile :-) ")
