import random
# num = random.randint(1, 100)

def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100

def input_num():
    while True:
        guess = input()
        if is_valid(guess):
            return int(guess)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def compare_num():
    print('Добро пожаловать в числовую угадайку!\nВыберите диапазон загадывания при условии от 1 до ??? > 100:\n')
    count_guess = 0
    choose_right = input_num()
    num = random.randint(1, choose_right)
    print(f'Число загадано!\n\nДиапазон: 1 - {choose_right}\n\nВведите число:')
    while True:
        n = input_num()
        count_guess += 1
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n == 'quit':
            break
        else:
            print('Вы угадали, поздравляем!')
            print(f'Вы совершили {count_guess} попыток!')
            return another_game()

def another_game():
    while True:
        print('Сыграем снова? Введите YES или NO:')
        play_again = input()
        if play_again.lower() == 'yes':
            compare_num()
        else:
            break

compare_num()