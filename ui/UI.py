from domain.entities import PlaneException, Point
from validation.validator import Validator


class UI(object):
    def __init__(self, controller):
        self.__controller = controller

    def __player_planes(self):
        player_planes = 0
        while player_planes != 2:
            try:
                point = self.__read_point()
                if point.value not in ["N", "S", "W", "E"]:
                    print("Error !!! Please insert a valid orientation!!!\n")
                else:
                    self.__controller.add_plane(point)
                    player_planes += 1
            except PlaneException as ve:
                print(ve)
            except ValueError:
                print("Invalid types!!! Coordinates must be of the form : A->H 1->8 [N, S, E, W]\n")

    def run(self):
        self.__player_planes()
        while self.__controller.win() is None:
            try:
                print(self.__controller)
                self.__controller.player_turn(self.__read_point())
                self.__controller.computer_turn()
            except PlaneException as ve:
                print(ve)
        print(self.__controller.win())

    def __read_point(self):
        read = input("Insert coordinates: ").split()
        if len(read) == 3:
            Validator.validate_types(read)
            if read[2] not in ["N", "S", "W", "E"]:
                raise PlaneException("Error!!! Invalid orientation!!!\n")
            return Point(read[0], read[1], read[2])
        elif len(read) == 2:
            Validator.validate_types(read)
            return Point(read[0], int(read[1]), "Default")
        else:
            raise PlaneException("Error!!! Please insert a valid point!!!\n")
