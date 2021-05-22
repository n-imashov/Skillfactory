from random import randint
import copy


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def __int__(self, length=0, orient=0, hp=0):
        self.length = length
        self.hp = hp
        self.dots = dots

    def show_dots(self):
        print(self.dots)


class Board:
    def __init__(self, board='', ships=None, alive=7):
        self.board = board
        self.ships = ships
        self.alive = alive

    def show_board(self):  # Функция, показывающая доску
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=' ')
            print()

    def add_ship_to_list(self, x):  # Добавляет координаты корабля в список
        if self.ships is None:
            self.ships = []
        self.ships.extend(x)

    @staticmethod
    def board_fields():  # Создает пустое поле
        board = [['O'] * 6 + [' '] for _ in range(6)]
        board = [[' ', '1', '2', '3', '4', '5', '6', ' ']] + board + [[' '] * 8]
        for i in range(1, 7):
            board[i] = list(str(i)) + board[i]
        return board

    def contour(self, x, y):  # Обводит корабли контуром
        for i in x.dots:
            if self.board[i[0] - 1][i[1] + 1] == 'O':
                self.board[i[0] - 1][i[1] + 1] = '.'
                y.append((i[0] - 1, i[1] + 1))
            if self.board[i[0]][i[1] + 1] == 'O':
                self.board[i[0]][i[1] + 1] = '.'
                y.append((i[0], i[1] + 1))
            if self.board[i[0] + 1][i[1] + 1] == 'O':
                self.board[i[0] + 1][i[1] + 1] = '.'
                y.append((i[0] + 1, i[1] + 1))
            if self.board[i[0] + 1][i[1]] == 'O':
                self.board[i[0] + 1][i[1]] = '.'
                y.append((i[0] + 1, i[1]))
            if self.board[i[0] + 1][i[1] - 1] == 'O':
                self.board[i[0] + 1][i[1] - 1] = '.'
                y.append((i[0] + 1, i[1] - 1))
            if self.board[i[0]][i[1] - 1] == 'O':
                self.board[i[0]][i[1] - 1] = '.'
                y.append((i[0], i[1] - 1))
            if self.board[i[0] - 1][i[1] - 1] == 'O':
                self.board[i[0] - 1][i[1] - 1] = '.'
                y.append((i[0] - 1, i[1] - 1))
            if self.board[i[0] - 1][i[1]] == 'O':
                self.board[i[0] - 1][i[1]] = '.'
                y.append((i[0] - 1, i[1]))

    def shot(self, cord1, hidden):  # Отрисовывает результат на поле после хода
        if self.board[cord1[0]][cord1[1]] == 'S':
            self.board[cord1[0]][cord1[1]] = 'X'
            hidden.board[cord1[0]][cord1[1]] = 'X'
            return True
        elif self.board[cord1[0]][cord1[1]] == '.' or self.board[cord1[0]][cord1[1]] == 'O':
            self.board[cord1[0]][cord1[1]] = '-'
            hidden.board[cord1[0]][cord1[1]] = '-'
            return False


class Player:
    def __init__(self, ship1_1=None, ship1_2=None, ship1_3=None, ship1_4=None, ship2_1=None, ship2_2=None, ship3=None):
        self.ship1_1 = ship1_1
        self.ship1_2 = ship1_2
        self.ship1_3 = ship1_3
        self.ship1_4 = ship1_4
        self.ship2_1 = ship2_1
        self.ship2_2 = ship2_2
        self.ship3 = ship3

    @staticmethod
    def ask():  # Запршивает ввод от пользователя
        while True:
            try:
                cords = tuple(map(int, input('Делай ход!\n').split()))
                if len(cords) != 2 or cords[0] < 1 or cords[0] > 6 or cords[1] < 1 or cords[1] > 6:
                    raise ValueError
            except ValueError:
                print('Введи две координаты цифрами в диапазоне от 1 до 6')
                continue
            return cords

    @staticmethod
    def move(move, player):  # Изменение списка кораблей после хода
        for i in range(len(player.ships)):
            if move in player.ships[i]:
                player.ships[i].remove(move)
                if len(player.ships[i]) == 0:
                    player.ships.remove(player.ships[i])
                    player.alive -= 1
                    return i


class User(Player):
    def __init__(self, board=None):
        super().__init__()
        self.board = board


class AI(Player):
    def __init__(self, board=None):
        super().__init__()
        self.board = board

    def ask(self):
        return randint(1, 6), randint(1, 6)


class Game:
    def __init__(self, user=User(), ai=AI()):
        self.user = user
        self.ai = ai

    @staticmethod
    def random_board(player, b):  # Создание случаной доски
        def o_not_in(x):  # Проверяет остались ли свободные клетки для заполнения
            for i in range(len(x)):
                for j in range(len(x[i])):
                    if x[i][j] == 'O':
                        return False
            return True

        def ship1_(x, y):  # функция создающая корабль с одной клеткой
            while True:
                cords = Dot(randint(1, 6), randint(1, 6))
                if (cords.x, cords.y) not in x and y.board[cords.x][cords.y] != '.':
                    return [(cords.x, cords.y)]
                elif o_not_in(y.board):
                    return 0

        def ship2_(x, y):  # функция создающая корабль с двумя клетками
            while True:
                cords = Dot(randint(1, 5), randint(1, 5))
                if (cords.x, cords.y) not in x and y.board[cords.x][cords.y] != '.':
                    orient = randint(1, 2)  # определяет будет ли корабль вертикальный или горизонтальный
                    if orient == 1 and (cords.x + 1, cords.y) not in x:
                        return [(cords.x, cords.y), (cords.x + 1, cords.y)]
                    if orient == 2 and (cords.x, cords.y + 1) not in x:
                        return [(cords.x, cords.y), (cords.x, cords.y + 1)]
                elif o_not_in(y.board):
                    return 0

        def ship3_(x, y):  # функция создающая корабль с тремя клетками
            while True:
                cords = Dot(randint(1, 4), randint(1, 4))
                if (cords.x, cords.y) not in x and y.board[cords.x][cords.y] != '.':
                    orient = randint(1, 2)
                    if orient == 1 and (cords.x + 1, cords.y) not in x and (cords.x + 2, cords.y) not in x:
                        return [(cords.x, cords.y), (cords.x + 1, cords.y), (cords.x + 2, cords.y)]
                    if orient == 2 and (cords.x, cords.y + 1) not in x and (cords.x, cords.y + 2) not in x:
                        return [(cords.x, cords.y), (cords.x, cords.y + 1), (cords.x, cords.y + 2)]
                elif o_not_in(y.board):
                    return 0

        def draw_ship(x, y_board):  # функция рисующая корабль
            for i in x.dots:
                y_board.board[i[0]][i[1]] = 'S'
                all_dots.append(i)
            y_board.contour(x, all_dots)

        while True:  # Цикл создает корабли по одной штуке
            b.board = b.board_fields()
            all_dots = []  # Массив содержащий все точки на доске
            player.ship3 = Ship()
            player.ship3.dots = ship3_(all_dots, b)
            if player.ship3.dots == 0:
                continue
            player.ship3.hp = player.ship3.length = len(player.ship3.dots)
            draw_ship(player.ship3, b)

            player.ship2_2 = Ship()
            player.ship2_2.dots = ship2_(all_dots, b)
            if player.ship2_2.dots == 0:
                continue
            player.ship2_2.hp = player.ship2_2.length = len(player.ship2_2.dots)
            draw_ship(player.ship2_2, b)
            player.ship2_1 = Ship()
            player.ship2_1.dots = ship2_(all_dots, b)
            if player.ship2_1.dots == 0:
                continue
            player.ship2_1.hp = player.ship2_1.length = len(player.ship2_1.dots)
            draw_ship(player.ship2_1, b)

            player.ship1_1 = Ship()
            player.ship1_1.dots = ship1_(all_dots, b)
            if player.ship1_1.dots == 0:
                continue
            player.ship1_1.hp = player.ship1_1.length = len(player.ship1_1.dots)
            draw_ship(player.ship1_1, b)

            player.ship1_2 = Ship()
            player.ship1_2.dots = ship1_(all_dots, b)
            if player.ship1_2.dots == 0:
                continue
            player.ship1_2.hp = player.ship1_2.length = len(player.ship1_2.dots)
            draw_ship(player.ship1_2, b)

            player.ship1_3 = Ship()
            player.ship1_3.dots = ship1_(all_dots, b)
            if player.ship1_3.dots == 0:
                continue
            player.ship1_3.hp = player.ship1_3.length = len(player.ship1_3.dots)
            draw_ship(player.ship1_3, b)

            player.ship1_4 = Ship()
            player.ship1_4.dots = ship1_(all_dots, b)
            if player.ship1_4.dots == 0:
                continue
            player.ship1_4.hp = player.ship1_4.length = len(player.ship1_4.dots)
            draw_ship(player.ship1_4, b)

            # b.show_board()
            break
        b.add_ship_to_list(
            [player.ship3.dots, player.ship2_1.dots, player.ship2_2.dots, player.ship1_1.dots, player.ship1_2.dots,
             player.ship1_3.dots,
             player.ship1_4.dots])

    @staticmethod
    def greet():  # Выводит правила игры
        print("Это игра морской бой!\n\n"
              "Как играть?\n"
              "Перед игроком 2 поля. Одно поле ваше, другое соперника. В качестве соперника играет\n"
              "компьютер. Все корабли расставлены в случайном порядке. \n"
              "Для победы необходимо уничтожить все вражеские корабли. Всего 7 кораблей: один трёхпалубный,\n"
              "два двухпалубных, четыре однопалубных\n"
              "Для того, чтобы сделать ход, игрок вводит 2 координаты клетки. Первая цифра - слева, вторая - сверху\n"
              "'S' - обозначает корабль, '.' - обводка вашего корабля, '-' - промах, 'О' - свободное поле\n"
              "Удачи!\n")

    def loop(self):  # Основной игровой цикл
        self.greet()
        self.user.board = Board()
        self.ai.board = Board()

        print('Твоя доска: ')
        game.random_board(self.user, self.user.board)
        self.user.board.show_board()
        print('Доска компьютера: ')
        game.random_board(self.ai, self.ai.board)

        ai_hid = Board()
        ai_hid.board = self.ai.board.board.copy()
        ai_hid.board = ai_hid.board_fields()
        ai_hid.show_board()

        copy_list_of_ai = copy.deepcopy(self.ai.board.ships)
        copy_list_of_user = copy.deepcopy(self.user.board.ships)

        def contour_shot(list_, y, z):  # Обводит контуром убитые корабли
            for i in list_:
                if y[i[0] - 1][i[1] + 1] == 'O' or y[i[0] - 1][i[1] + 1] == '.':
                    y[i[0] - 1][i[1] + 1] = '-'
                    z[i[0] - 1][i[1] + 1] = '-'
                if y[i[0]][i[1] + 1] == 'O' or y[i[0]][i[1] + 1] == '.':
                    y[i[0]][i[1] + 1] = '-'
                    z[i[0]][i[1] + 1] = '-'
                if y[i[0] + 1][i[1] + 1] == 'O' or y[i[0] + 1][i[1] + 1] == '.':
                    y[i[0] + 1][i[1] + 1] = '-'
                    z[i[0] + 1][i[1] + 1] = '-'
                if y[i[0] + 1][i[1]] == 'O' or y[i[0] + 1][i[1]] == '.':
                    y[i[0] + 1][i[1]] = '-'
                    z[i[0] + 1][i[1]] = '-'
                if y[i[0] + 1][i[1] - 1] == 'O' or y[i[0] + 1][i[1] - 1] == '.':
                    y[i[0] + 1][i[1] - 1] = '-'
                    z[i[0] + 1][i[1] - 1] = '-'
                if y[i[0]][i[1] - 1] == 'O' or y[i[0]][i[1] - 1] == '.':
                    y[i[0]][i[1] - 1] = '-'
                    z[i[0]][i[1] - 1] = '-'
                if y[i[0] - 1][i[1] - 1] == 'O' or y[i[0] - 1][i[1] - 1] == '.':
                    y[i[0] - 1][i[1] - 1] = '-'
                    z[i[0] - 1][i[1] - 1] = '-'
                if y[i[0] - 1][i[1]] == 'O' or y[i[0] - 1][i[1]] == '.':
                    y[i[0] - 1][i[1]] = '-'
                    z[i[0] - 1][i[1]] = '-'

        while True:
            while True:
                cord = self.user.ask()
                if self.ai.board.board[cord[0]][cord[1]] == 'X' or self.ai.board.board[cord[0]][cord[1]] == '-':
                    print('Ты уже стрелял в эту точку')
                    continue
                if self.ai.board.shot(cord, ai_hid):
                    self.ai.board.shot(cord, ai_hid)
                    x = self.user.move(cord, self.ai.board)
                    if x is not None:
                        contour_shot(copy_list_of_ai[x], ai_hid.board, self.ai.board.board)
                        copy_list_of_ai.remove(copy_list_of_ai[x])
                    print('Твоя доска: ')
                    self.user.board.show_board()
                    print('Доска компьютера: ')
                    ai_hid.show_board()

                    if self.ai.board.alive == 0:
                        break
                    print('Ты попал, стреляй еще')
                    print('Живые корабли противника: ', self.ai.board.alive)
                    print('Твои живые корабли: ', self.user.board.alive)
                    continue
                else:
                    self.ai.board.shot(cord, ai_hid)
                    break

            if self.ai.board.alive == 0:
                input('Ты выиграл! Нажми любую клавишу, чтобы выйти')
                break

            while True:
                cord = self.ai.ask()
                if self.user.board.board[cord[0]][cord[1]] == 'X' or self.user.board.board[cord[0]][cord[1]] == '-':
                    continue
                if self.user.board.shot(cord, self.user.board):
                    self.user.board.shot(cord, self.user.board)
                    x = self.ai.move(cord, self.user.board)
                    if x is not None:
                        contour_shot(copy_list_of_user[x], self.user.board.board, self.user.board.board)
                        copy_list_of_user.remove(copy_list_of_user[x])
                    if self.user.board.alive == 0:
                        break
                    continue
                else:
                    self.user.board.shot(cord, self.user.board)
                    print('Твоя доска: ')
                    self.user.board.show_board()
                    print('Доска компьютера: ')
                    ai_hid.show_board()
                    break

            if self.user.board.alive == 0:
                print('Твоя доска: ')
                self.user.board.show_board()
                print('Доска компьютера: ')
                ai_hid.show_board()
                input('Ты Проиграл! :с Нажми любую клавишу, чтобы выйти')
                break

            print('Живые корабли противника: ', self.ai.board.alive)
            print('Твои живые корабли: ', self.user.board.alive)

    @staticmethod
    def start():  # запускает игру
        game.loop()


game = Game()

if __name__ == '__main__':
    game.start()