from domain.entities import Point, PlaneException


class ValidatorException(PlaneException):
    pass


class Checker:
    def validate_plane(self, head):
        if head.value == 'N':
            top_left = Point(head.x, head.y - 2, "top_left")
            bottom_right = Point(head.x + 3, head.y + 2, "bot_right")
            return self.__check_corners(top_left, bottom_right)
        if head.value == 'S':
            top_left = Point(head.x - 3, head.y - 2, "top_left")
            bottom_right = Point(head.x, head.y + 2, "bot_right")
            return self.__check_corners(top_left, bottom_right)
        if head.value == 'E':
            top_left = Point(head.x - 2, head.y - 3, "top_left")
            bottom_right = Point(head.x + 2, head.y, "bot_right")
            return self.__check_corners(top_left, bottom_right)
        if head.value == 'W':
            top_left = Point(head.x - 2, head.y, "top_left")
            bottom_right = Point(head.x + 2, head.y + 3, "bot_right")
            return self.__check_corners(top_left, bottom_right)

    @staticmethod
    def overlap_plane(planes_board, params):
        for point in params:
            if planes_board[point.x][point.y] != " ":
                return True

    @staticmethod
    def __check_corners(top_left, bottom_right):
        if top_left.x <= 0 or top_left.x > 8 or top_left.y <= 0 or top_left.y > 8 or \
                bottom_right.x <= 0 or bottom_right.x > 8 or bottom_right.y <= 0 or bottom_right.y > 8:
            return True

    @staticmethod
    def validate_point(point):
        if point.x <= 0 or point.x > 8 or point.y <= 0 or point.y > 8:
            return True


class Validator(Checker):
    def validate_plane(self, head):
        if super().validate_plane(head):
            raise ValidatorException("Error!!! Plane out of board size!!!\n")

    def overlap_plane(self, planes_board, params):
        if super().overlap_plane(planes_board, params):
            raise ValidatorException("Error!!! Planes overlap!!!\n")

    def validate_point(self, point):
        if super().validate_plane(Checker, point):
            raise ValidatorException("Error!!! Point outside of board !!!\n")

    @staticmethod
    def validate_types(point):
        errors = 0
        if point[0] not in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            errors += 1
        if int(point[1]) < 1 or int(point[1]) > 8:
            errors += 1
        if errors != 0:
            raise ValidatorException(
                "Error!!! Coordinates must be of the form : A->H 1->8 [N, S, E, W]\n")
