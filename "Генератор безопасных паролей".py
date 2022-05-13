# Генератор безопасных паролей
import random
from math import ceil

def is_valid(que):
    return que.isdigit() and ('1' or '0') in que and ('3' or '4' or '5' or '6' or '7' or '8' or '9') not in que and len(que) >= 4

def password_randomizer(question, symbols_total, count_passwords):
    diggits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = []
    question = str(question)
    for i in range(count_passwords):
        if question[0] == '1':
            chars += random.sample(diggits,ceil(symbols_total/question.count('1')))
        if question[1] == '1':
            chars += random.sample(lowercase_letters,ceil(symbols_total/question.count('1')))
        if question[2] == '1':
            chars += random.sample(uppercase_letters,ceil(symbols_total/question.count('1')))
        if question[3] == '1':
            chars += random.sample(punctuation,ceil(symbols_total/question.count('1')))
        print(''.join(chars))
        chars.clear()

def request():
    print('Добро пожаловать в генератор безопасных паролей!\n')
    symbols_total = int(input('Введите общее количество символов предполагаемого пароля:\n'))
    count_passwords = int(input('Введите количество паролей для генерации:\n'))
    question = input('Какой пароль вам нужен?\n\n'
                     'Введите четыре "1" если пароль должен содержать цифры/маленькие буквы/большые буквы/символы пунктуации\n'
                     'Если же пароль не должен содержать какие либо из перечисленных символов, - введите "0"\n\n'
                     'К примеру: если нужен пароль без символов пунктуации, введите "1110".\n'
                     'Введите запрос:\n')
    if is_valid(question):
        password_randomizer(question.strip(), symbols_total, count_passwords)
    else:
        print('Запрос не отвечает требованиям, прошу повторить:')
        request()

request()
