import docx
from docx import Document


def create_biblio(structura):
    struct = load_struct(structura)
    create_files(struct)
    pass


def load_struct(structura):
    pass


def create_files(struct):
    pass


if __name__ == '__main__':
    structura = None
    create_biblio(structura)

# document = Document()
# document.save('demo.docx')