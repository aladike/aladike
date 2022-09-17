from random import randint
def create_random_matrix(size):
    matrix = []
    for i in range(size):
        matrix.append([randint(1, 51) for _ in range(size)])
    return matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()
def guessing_game():
    print('Добро пожаловать в "Матрицу"\n')
    matrix = create_random_matrix(int(input('Выберите размерность матрицы: ')))
    print()
    print(f'Вами была выбрана матрица размером {len(matrix)} x {len(matrix)}:')
    print_matrix(matrix)

guessing_game()
