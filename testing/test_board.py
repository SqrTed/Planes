from unittest import TestCase

from domain.entities import Board, Point


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board()

    def test_add(self):
        p = Point("A", 1, "#")
        self.board.add([p])
        self.assertEqual(self.board[1][1], "#")

    def test_setitem(self):
        self.board[1][1] = "!"
        self.assertEqual(self.board[1][1], "!")

    def test_all(self):
        self.assertEqual(self.board.all(), [[" " for c in range(0, 9)] for l in range(0, 9)])

    def test_str(self):
        string = "0|1|2|3|4|5|6|7|8|\nA| | | | | | | | |\nB| | | | | | | | |\nC| | | | | | | | |\nD| | | | | | | | |\nE| | | | | | | | |\nF| | | | | | | | |\nG| | | | | | | | |\nH| | | | | | | | |\n"
        self.assertEqual(str(self.board), string)
