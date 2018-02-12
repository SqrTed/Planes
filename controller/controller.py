from domain.entities import Plane, Point
from validation.validator import Validator
from domain.entities import Utils


class PlayerController(Utils):
    def __init__(self, player_planes_board, player_hits_board):
        self.__planes = player_planes_board
        self.__hits = player_hits_board
        self.__validator = Validator()
        self.__planes_alive = 0

    @property
    def get_planes(self):
        return self.__planes

    def new_plane(self, head):
        self.__validator.validate_plane(head)
        plane = Plane(head)
        self.__validator.overlap_plane(self.__planes, plane.coordinates())
        self.__planes.add(plane.coordinates())
        self.__planes_alive += 1

    def get_point(self, point):
        return self.__planes[point.x][point.y]

    def attacked(self, point):
        self.__validator.validate_plane(point)
        if self.__planes[point.x][point.y] == "#":
            self.__planes[point.x][point.y] = "!"
            return "X"
        elif self.__planes[point.x][point.y] in ["S", "N", "E", "W"]:
            self.__planes = self.__fill(point, "!", self.__planes)
            self.__planes_alive -= 1
            return "K"
        return "O"

    def hit(self, point, result):
        if result == "K":
            self.__hits = self.__fill(point, "X", self.__hits)
        else:
            self.__hits[point.x][point.y] = result

    def check_hit(self, point):
        if self.__hits[point.x][point.y] != " ":
            return True
        return False

    @property
    def planes_alive(self):
        return self.__planes_alive

    def __str__(self):
        return "Alive Planes: " + str(self.__planes_alive) + "\nPlanes:\n" + str(self.__planes) + "\nMoves:\n" + str(
            self.__hits)

    def __fill(self, param, value, board):
        if param.value == "N":
            return super().fill_N(param.x, param.y, value, board)
        if param.value == "S":
            return super().fill_S(param.x, param.y, value, board)
        if param.value == "W":
            return super().fill_W(param.x, param.y, value, board)
        if param.value == "E":
            return super().fill_E(param.x, param.y, value, board)


class ComputerController(PlayerController):
    pass
