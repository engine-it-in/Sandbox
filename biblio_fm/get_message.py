# -*- coding: utf-8 -*-
import admin_data as ad

"""Work with user message"""


def dict_by_file(file):
    """ Create python dict from file
    :param file: file with data in structure
    :return: python dict
    """
    dic = dict()
    dao = open(file, 'r', encoding='utf-8')
    for i in dao:
        k, *v = i.split(' = ')
        v = ''.join(v).replace("'", "").capitalize().strip() + ' '
        dic[k] = v
    return(dic)


def usr_com(key):
    """ Get user message from file
    :param key: key from file with message
    :return: value of message
    """
    try:
        d = dict_by_file('admin_text.py')
        return (d[key])
    except KeyError:
        return None
        exit()
    except:
        print('Something bad')


def discover_separator(file):
    open_file = open(file, 'r', encoding='utf-8')
    bag = []
    try:
        for item in open_file:
            item = open_file.readline().split()
            item = item[1] #crutch
            if item in ad.separator: break
            else: continue
    except IndexError:
        print("Something bad") #crutchs
        exit()
    return item


def correct_exist_value(key):
    """Correct existing values"""
    dic = dict_by_file('admin_text.py')
    if key in set(dic.keys()): return key
    else: return None


def add_com_to_file(key, value):
    """ Add command and text to file (admin data)
    :param key: key - command
    :param value: value
    """
    dao = open(r'admin_text.py', 'a', encoding='utf-8')
    dao.write(key+' = '+"'"+(value)+"'"+'\n')
    dao.close()
    print('You command was added to file')


def usr_com_with_variants(key):
    """ Transform usually command to command with variants
    :param key: key
    """
    answer = usr_com(key) + usr_com('Var')
    return answer


def add_new_message_by_key(key):
    """ Add new message in file by key
    :param key:
    """
    if correct_exist_value(key) is None:
        value = 'y'
        while value != 'n':
            answer = input(usr_com_with_variants('WarnK'))
            if answer is 'y':
                value = input(usr_com('InpKV'))
                add_com_to_file(key, value)
                exit()
            elif answer is 'n':
                print(usr_com('BB'))
                break
            else:
                print(usr_com('Non'))
                value = input(usr_com_with_variants('Ret'))
                pass


if __name__ == "__main__":
    print('Now time for your test')