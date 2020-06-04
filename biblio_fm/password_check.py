#-*- coding:utf-8 -*-
import re

""" Validation data of user"""

def check_pass(password):
    """
    Password verification
    :param password: value of password
    :return: vocabulary with result and schedule of exception
    """
    try:
        for i in password:
            length_error = len(i) < 8
            digit_error = re.search(r"\d{2}", i)
            uppercase_error = re.search(r"[A-Z]", i)
            lowercase_error = re.search(r"[a-z]", i)
            symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', i)
            password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)
        return {
            'password_ok': password_ok,
            'length_error': length_error,
            'digit_error': digit_error,
            'uppercase_error': uppercase_error,
            'lowercase_error': lowercase_error,
            'symbol_error': symbol_error,
        }
    except:
        print('Something bad with password_check')


if __name__ == '__main__':
    a = check_pass('12fff')
    print(a)