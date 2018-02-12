class PlaneException(Exception):
    pass


class Point(object):
    def __init__(self, x, y, value):
        self.__x = int(ord(x) - ord('A') + 1) if type(x) == str else int(x)
        self.__y = int(y)
        self.__value = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.__x)+" "+str(self.__y)+" "+str(self.__value)


class Plane(object):
    def __init__(self, head):
        self.__head = head

    def coordinates(self):
        if self.__head.value == "N":
            return self.__north()
        elif self.__head.value == "S":
            return self.__south()
        elif self.__head.value == "E":
            return self.__east()
        elif self.__head.value == "W":
            return self.__west()

    def __north(self):
        x = self.__head.x
        y = self.__head.y
        return [Point(x, y, "N"), Point(x + 1, y - 2, "#"), Point(x + 1, y - 1, "#"),
                Point(x + 1, y, "#"), Point(x + 1, y + 1, "#"), Point(x + 1, y + 2, "#"),
                Point(x + 2, y, "#"), Point(x + 3, y - 1, "#"), Point(x + 3, y, "#"),
                Point(x + 3, y + 1, "#")]

    def __south(self):
        x = self.__head.x
        y = self.__head.y
        return [Point(x, y, "S"), Point(x - 1, y - 2, "#"), Point(x - 1, y - 1, "#"),
                Point(x - 1, y, "#"), Point(x - 1, y + 1, "#"), Point(x - 1, y + 2, "#"),
                Point(x - 2, y, "#"), Point(x - 3, y - 1, "#"), Point(x - 3, y, "#"),
                Point(x - 3, y + 1, "#")]

    def __east(self):
        x = self.__head.x
        y = self.__head.y
        return [Point(x, y, "E"), Point(x + 2, y - 1, "#"), Point(x + 1, y - 1, "#"), Point(x, y - 1, "#"),
                Point(x - 1, y - 1, "#"), Point(x - 2, y - 1, "#"), Point(x, y - 2, "#"), Point(x + 1, y - 3, "#"),
                Point(x, y - 3, "#"), Point(x - 1, y - 3, "#")]

    def __west(self):
        x = self.__head.x
        y = self.__head.y
        return [Point(x, y, "W"), Point(x + 2, y + 1, "#"), Point(x + 1, y + 1, "#"), Point(x, y + 1, "#"),
                Point(x - 1, y + 1, "#"), Point(x - 2, y + 1, "#"), Point(x, y + 2, "#"), Point(x + 1, y + 3, "#"),
                Point(x, y + 3, "#"), Point(x - 1, y + 3, "#")]


class Board(object):
    def __init__(self):
        self.__board = [[" " for c in range(0, 9)] for l in range(0, 9)]

    def add(self, points):
        for point in points:
            self.__board[point.x][point.y] = point.value

    def __str__(self):
        to_print = ""
        char = 'A'
        for i in range(0, 9):
            to_print += str(i) + "|"
        to_print += '\n'
        for i in range(0, 8):
            to_print += char + "|"
            char = chr(ord(char) + 1)
            for j in range(1, 9):
                if self.__board[i + 1][j] in ["S", "N", "E", "W"]:
                    to_print += "*"
                else:
                    to_print += self.__board[i + 1][j]
                to_print += "|"
            to_print += '\n'
        return to_print

    def __getitem__(self, item):
        return self.__board[item]

    def __setitem__(self, key, value):
        self.__board[key] = value

    def all(self):
        return self.__board


class Utils(object):
    def fill_N(self, x, y, value, board):
        board[x][y] = value
        board[x + 1][y - 2] = value
        board[x + 1][y - 1] = value
        board[x + 1][y] = value
        board[x + 1][y + 1] = value
        board[x + 1][y + 2] = value
        board[x + 2][y] = value
        board[x + 3][y - 1] = value
        board[x + 3][y] = value
        board[x + 3][y + 1] = value
        return board

    def fill_S(self, x, y, value, board):
        board[x][y] = value
        board[x - 1][y - 2] = value
        board[x - 1][y - 1] = value
        board[x - 1][y] = value
        board[x - 1][y + 1] = value
        board[x - 1][y + 2] = value
        board[x - 2][y] = value
        board[x - 3][y - 1] = value
        board[x - 3][y] = value
        board[x - 3][y + 1] = value
        return board

    def fill_W(self, x, y, value, board):
        board[x][y] = value
        board[x + 2][y + 1] = value
        board[x + 1][y + 1] = value
        board[x][y + 1] = value
        board[x - 1][y + 1] = value
        board[x - 2][y + 1] = value
        board[x][y + 2] = value
        board[x + 1][y + 3] = value
        board[x][y + 3] = value
        board[x - 1][y + 3] = value
        return board

    def fill_E(self, x, y, value, board):
        board[x][y] = value
        board[x + 2][y - 1] = value
        board[x + 1][y - 1] = value
        board[x][y - 1] = value
        board[x - 1][y - 1] = value
        board[x - 2][y - 1] = value
        board[x][y - 2] = value
        board[x + 1][y - 3] = value
        board[x][y - 3] = value
        board[x - 1][y - 3] = value
        return board