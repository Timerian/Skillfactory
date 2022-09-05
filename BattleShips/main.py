# Адыев Тимур FPW-85 Skillfactory
# решение задачи Морской бой


from random import randint


# creating user classes of exceptions
class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Мимо доски!"


class BoardUsedException(BoardException):
    def __str__(self):
        return "Сектор занят!"


class BoardWrongShipException(BoardException):
    pass


# creating class of dots, which give us more useful format of coordinates
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


#  class Ships which include all information about ships and methods of creating ships on the board
class Ship:
    def __init__(self, head, l, orient):
        self.l = l
        self.head = head
        self.orient = orient
        self.lives = l

    @property
    def dots(self):
        ship_coord = []
        for i in range(self.l):
            coord_x = self.head.x
            coord_y = self.head.y
            if self.orient == 0:
                coord_x += i
            elif self.orient == 1:
                coord_y += i

            ship_coord.append(Dot(coord_x, coord_y))

        return ship_coord


# class Board contains methods that adding ships on the board, checking coordinates of ships, contours,..
# ... making shot and etc.
class Board:
    def __init__(self, hide=False, size=6):
        self.hide = hide
        self.size = size

        self.field = [['0'] * size for _ in range(self.size)]
        self.buzy = []

        self.ships = []
        self.moves = 0

        self.count = 0

    def __str__(self):
        board = ''
        first_str = [f'{i}' for i in range(1, self.size + 1)]
        board += '  | ' + ' | '.join(first_str) + ' |'
        for i, row in enumerate(self.field):
            board += f'\n{i + 1} | ' + ' | '.join(row) + ' |'

        if self.hide:
            board = board.replace('■', '0')

        return board

    def is_out(self, dot):
        return not (0 <= dot.x < self.size and 0 <= dot.y < self.size)

    def contour(self, ship, verb=False):
        near = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
        for dot in ship.dots:
            for dx, dy in near:
                cont_dots = Dot(dot.x + dx, dot.y + dy)
                if not (self.is_out(cont_dots)) and cont_dots not in self.buzy:
                    if verb:
                        self.field[cont_dots.x][cont_dots.y] = '.'
                    self.buzy.append(cont_dots)

    def add_ship(self, ship):
        for dots in ship.dots:
            if self.is_out(dots) or dots in self.buzy:
                raise BoardWrongShipException()
        for dots in ship.dots:
            self.field[dots.x][dots.y] = '■'
            self.buzy.append(dots)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, target):
        if self.is_out(target):
            raise BoardOutException

        if target in self.buzy:
            raise BoardUsedException

        self.buzy.append(target)

        for ship in self.ships:
            if target in ship.dots:
                ship.lives -= 1
                self.field[target.x][target.y] = 'X'
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print('Вы уничтожили корабль противника!')
                    return False
                else:
                    print('Вы попали по кораблю противника!')
                    return True

        self.field[target.x][target.y] = '.'
        print('Вы промахнулись!')
        return False

    def begin(self):
        self.buzy = []


# class Player contains boards of both players(User, Computer), request coordinates of shots (move)
class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, self.board.size), randint(0, self.board.size))
        print(f'Компьютер сделал ход: {d.x+1} {d.y+1}')
        return d


class User(Player):
    def ask(self):
        while True:
            cords = input('Ваш ход: ').split()

            if len(cords) != 2:
                print("Должно быть две координаты!")
                continue

            x, y = cords

            if not(x.isdigit()) or not(y.isdigit()):
                print('Введите два числа!')
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


# class Game combines all methods of previous classes for working process
class Game:
    def __init__(self, size = 6):
        self.size = size
        plr = self.random_board()
        cmp = self.random_board()
        cmp.hide = True

        self.ai = AI(cmp, plr)
        self.plr = User(plr, cmp)

    def greet(self):
        print('-----------------------')
        print('Добро пожаловать в игру')
        print('      Морской бой      ')
        print('-----------------------')
        print('   Формат ввода: x y   ')
        print('   x - номер строки    ')
        print('   y - номер столбца   ')

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for i in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), i, randint(0,1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def start(self):
        self.greet()
        self.loop()

    def loop(self):
        num = 0
        while True:
            print('-' * 20)
            print('Доска пользователя:')
            print(self.plr.board)
            print('-' * 20)
            print('Доска компьютера:')
            print(self.ai.board)
            print('-' * 20)
            if num % 2 == 0:
                print('Ходит пользователь...')
                repeat = self.plr.move()
            else:
                print('Ходит компьютер...')
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print('-' * 20)
                print('Выйграл пользователь!')
                break

            if self.plr.board.count == 7:
                print('-' * 20)
                print('Выйграл компьютер!')
                break

            num += 1


g = Game()
g.start()








