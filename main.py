# Адыев Тимур FPW-85 Skillfactory
# решение задачи крестики-нолики


# winning combination options
win_coord = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

# players sign
players = ('X', '0')
# count of moves
k = 0
# turn of move
turn = 0
# field of the game
board = [[' '] * 3 for i in range(3)]


def greet():
    print('-----------------------------')
    print('   Приветствуем вас в игре   ')
    print('       крестики-нолики       ')
    print('-----------------------------')
    print('      Формат ввода: x y      ')
    print('      x - номер строки       ')
    print('      y - номер столбца      ')
    print('-----------------------------')


def ready():
    answer = input('Готовы ли вы начать игру? Y - да, N - нет.     ')
    if answer == 'Y':
        print('Начнем...')
        return True
    elif answer == 'N':
        print('До встречи! ! !')
        return False
    else:
        print('Повторите ввод')
        ready()


def show(matrix):
    print('|   | 0 | 1 | 2 |')
    print('-' * 16)
    n = 0
    for row in matrix:
        print(f'| {n} | {row[0]} | {row[1]} | {row[2]} | ')
        print('-' * 16)
        n += 1


def input_coord():
    while True:
        try:
            global turn
            i, j = list(map(int, input(f"Ход игрока {players[turn]}. Введите координаты хода: ").split()))
            if i < 0 or j < 0 or i > 2 or j > 2:
                print('Координаты должны иметь значения от 0 до 2!')
                continue
        except ValueError:
            print('Введите две координаты!')
            continue
        break
    return i, j


def move(matrix):
    global k
    global turn
    while True:
        x, y = input_coord()
        if matrix[x][y] != ' ':
            print('Клетка занята!')
            continue

        matrix[x][y] = players[turn]
        k += 1
        turn = k % 2
        break


def win_check():
    global win_coord
    for coord in win_coord:
        a, b, c = coord[0], coord[1], coord[2]
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] != ' ':
            print('')
            print(f'Игрок {board[c[0]][c[1]]} выйграл!')
            print('')
            return True
    return False


greet()
if ready():
    while True:
        show(board)
        move(board)
        if win_check():
            print('')
            print('До встречи! ! !')
            print('                                ')
            break
        if k == 9:
            print('')
            print('Ничья!!!')
            print('')
            print('До встречи! ! !')
            print('')
            break



