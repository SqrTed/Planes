from random import randint

from domain.entities import Point, Plane, PlaneException
from validation.validator import Checker, Validator


class Boss(object):
    def __init__(self, player_controller, computer_controller):
        self.__player = player_controller
        self.__computer = computer_controller
        self.__computer_planes()
        self.__first_top = Point(0, 0, "First")
        self.__first_bot = Point(0, 0, "First")
        self.__second_top = Point(0, 0, "Second")
        self.__second_bot = Point(0, 0, "Second")

    def __computer_planes(self):
        planes = 0
        directions = ["N", "S", "W", "E"]
        while planes != 2:
            head = Point(randint(1, 8), randint(1, 8), directions[randint(0, 3)])
            plane = Plane(head)
            if not Checker.validate_plane(Checker, head):
                if not Checker.overlap_plane(self.__computer.get_planes, plane.coordinates()):
                    self.__computer.new_plane(head)
                    planes += 1

    def win(self):
        if self.__player.planes_alive == 0:
            return "Computer wins!!!"
        elif self.__computer.planes_alive == 0:
            return "Player wins!!!"
        return None

    def __corners(self, head):
        if head.value == 'N':
            top_left = Point(head.x, head.y - 2, "top_left")
            bottom_right = Point(head.x + 3, head.y + 2, "bot_right")
            return [top_left, bottom_right]
        if head.value == 'S':
            top_left = Point(head.x - 3, head.y - 2, "top_left")
            bottom_right = Point(head.x, head.y + 2, "bot_right")
            return [top_left, bottom_right]
        if head.value == 'E':
            top_left = Point(head.x - 2, head.y - 3, "top_left")
            bottom_right = Point(head.x + 2, head.y, "bot_right")
            return [top_left, bottom_right]
        if head.value == 'W':
            top_left = Point(head.x - 2, head.y, "top_left")
            bottom_right = Point(head.x + 2, head.y + 3, "bot_right")
            return [top_left, bottom_right]

    def add_plane(self, head):
        self.__player.new_plane(head)
        p = self.__corners(head)
        if self.__player.planes_alive == 1:
            self.__first_top = p[0]
            self.__first_bot = p[1]
        elif self.__player.planes_alive == 2:
            self.__second_top = p[0]
            self.__second_bot = p[1]

    def player_turn(self, point):
        Validator.validate_point(Validator, point)
        if not self.__player.check_hit(point):
            point.value = self.__computer.get_point(point)
            self.__player.hit(point, self.__computer.attacked(point))
        else:
            raise PlaneException("Error!!! Unavailable move!!!")

    def computer_turn(self):
        while True:
            if self.__player.planes_alive == 2:
                x = randint(self.__first_top.x, self.__first_bot.x)
                y = randint(self.__first_top.y, self.__first_bot.y)
            else:
                x = randint(self.__second_top.x, self.__second_bot.x)
                y = randint(self.__second_top.y, self.__second_bot.y)
            point = Point(x, y, self.__player.get_point(Point(x, y, "Default")))
            if not self.__computer.check_hit(point):
                self.__computer.hit(point, self.__player.attacked(point))
                break

    def __str__(self):
        return "\n" + str(self.__player) + "\nComputer:\n" + str(self.__computer)
