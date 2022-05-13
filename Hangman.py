# Hangman

import random
word_list = ['мир', 'весна', 'украина', 'человек', 'собака', 'огород', 'красный', 'треугольник', 'апельсин', 'медведь', 'грейпфрут', 'ниндзя', 'коктель', 'вертушка',
             'гиббон', 'артель', 'силикон', 'штанга', 'шифер', 'принадлежность', 'параболоид', 'длиномер',
             'контроллер']

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = list('_' * len(word)) # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(6))
    print(f'Длина загаданого слова {len(word)} символов: {word_completion}')

    while tries > 0:
        print(f'Использованные буквы: {guessed_letters}')
        guess = input('Введите букву: ').upper()
        if (guess.isalpha() and len(guess) == 1):
            guessed_letters += guess
            if guess in word:
                print(f"Верный ответ. Осталось {word_completion.count('_')}\nЗагаданное слово: {word_completion}")
                for i in range(len(word)):
                    if word[i] == guess:
                        word_completion[i] = guess
                print(*word_completion, sep='')
                if ''.join(word_completion) == word:
                    print(f'Поздравляем, вы угадали слово: {word}')
                    if input('Хотите ли вы сыграть снова?\n') in ['yes', 'y', 'да', 'ок']:
                        play(get_word())
                    else:
                        print('До скорой встречи!')
                        break

            elif guess not in word:
                tries -= 1
                print(display_hangman(tries))
                if input('Хотите ли вы подсказку?').lower() in ['yes', 'y', 'да', 'ок']:
                    word_completion = list(word[0] + ('_' * (len(word) - 2)) + word[-1])
                    print(*word_completion)
                if tries == 0:
                    print(f'Попытки закончились. Вы не справились.\nПрограммой было загадано слово {word}')
                    if input('Хотите ли вы сыграть снова?\n').lower() in ['yes', 'y', 'да', 'ок']:
                        play(get_word())
                    else:
                        print('До скорой встречи!')
                        break
                else:
                    print(f'Осталось {tries} попыток. Попробуйте еще раз.')

        else:
            print('Введен некорректный символ.\nПожалуйста, введите одну букву из русского алфавита.')
            continue

play(get_word())