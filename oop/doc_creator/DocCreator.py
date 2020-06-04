#-*- coding:utf - 8 -*-
"""
Purprose:
Create structure files
"""

class DocCreator(object):
    def __init__(self, LS, LSF, LSF_, LSFE, KEY):
        self.LSFE = LSFE # Конечная папка, откуда берем файл (.txt) с структурой создаваемого курса
        self.LSF = LSF   # Папка промежуточного пути, откуда берем файл с структурой создаваемого курса
        self.LSF_= LSF_  # Промежуточное хранилище
        self.LS = LS     # Диск, откуда берем файл с структурой создаваемого курса
        self.KEY = KEY   # ?


    def PrepareDialog(self):
        """
        Purprose:
            Dialog with user
        Algorithm:
            1. With key output value to user
            2. Process answer
            2.1. Answer bad -> Warnings and loop
            2.1.1. He should have ability to exit
            2.2. Answer good ->
            2.2.1. Write answer
            2.2.2. Say him thank you
            2.2.3. Loop or exit
        """
        try:
            d = {}
            a = open(r'/home/ivan/PyPy/admin_text.py', 'r', encoding="utf-8")
            for i in a:
                k, *v = i.split(' = ')
                v = ''.join(v).strip('\n')
                d[k] = v
        except IndexError:
            print('Для указанного ключа нет значения в словаре служебных слов и выражений')
        except KeyError:
            print('Для указанного ключа нет значения в словаре служебных слов и выражений')
        except:
            print('Произошла неопознанная ошибка')
        return (d[self.KEY])