# -*- coding: utf-8 -*-
"""Work with message from file"""


ADMIN_TEXT = 'admintext.py'


def dict_by_file(file):
    """ Create python dict from file
    :param file: file with data in structure
    :return: python dict
    """
    dic = dict()
    dao = open(file, 'r', encoding='utf-8')
    for item in dao:
        key, *value = item.split(' = ')
        value = ''.join(value).replace("'", "").capitalize().strip() + ' '
        dic[key] = value
    return dic


def usr_com(key):
    """ Get user message
    :param key: key from file with message
    :return: value of message
    """
    try:
        dic = dict_by_file(ADMIN_TEXT)
        return dic[key]
    except KeyError:
        return None


def discover_separator(file_separator):
    """ Compare possible separator from ADMIN_TEXT with reference
    :param file_separator: references value of separators
    :return: separator
    """
    open_file = open(ADMIN_TEXT, 'r', encoding='utf-8')
    try:
        for item in open_file:
            item = open_file.readline().split()
            item = item[1]
            if item in file_separator:
                break
            else:
                continue
    except IndexError:
        print("Something bad")
        exit()
    return item


def correct_exist_value(key):
    """Check existing values of key in dict
    :param key: key of dict
    :return: key or none
    """
    dic = dict_by_file(ADMIN_TEXT)
    if key in set(dic.keys()):
        return key
    else:
        return None


def add_com_to_file(key, value):
    """ Add command and text to file (admin data)
    :param key: key - command
    :param value: value
    :return: alert
    """
    dao = open(ADMIN_TEXT, 'a', encoding='utf-8')
    dao.write(key + ' = ' + "'" + (value) + "'" + '\n')
    dao.close()
    print('You command was added to file')


def usr_com_with_variants(key):
    """ Transform usually command to command with variants
    :param key: key of command
    :return: complex answer with y/n
    """
    answer = usr_com(key) + usr_com('Var')
    return answer


def add_new_message_by_key(key):
    """ Add new message in file by key
    :param key:
    :return: nothing
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


if __name__ == '__main__':
    """Let's go test it"""
    print('Have a nice journey')
