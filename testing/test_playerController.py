from unittest import TestCase

from controller.controller import PlayerController
from domain.entities import Board, Point


class TestPlayerController(TestCase):
    def setUp(self):
        self.player_planes = Board()
        self.player_hits = Board()
        self.player = PlayerController(self.player_planes, self.player_hits)

    def test_new_plane(self):
        self.player.new_plane(Point("E", 4, "W"))
        self.assertEqual(self.player.planes_alive, 1)

    def test_get_point(self):
        self.player.new_plane(Point("E", 4, "W"))
        self.assertEqual(self.player.get_point(Point("E", 4, "Default")), "W")

    def test_check_hit(self):
        self.player.new_plane(Point("E", 4, "W"))
        self.player.hit(Point("E", 5, "#"), self.player.attacked(Point("E", 5, "#")))
        self.assertEqual(self.player.check_hit(Point("E", 5, "#")), True)

    def test_planes_alive(self):
        self.player.new_plane(Point("E", 4, "W"))
        self.assertEqual(self.player.planes_alive, 1)
        self.player.hit(Point("E", 4, "W"), self.player.attacked(Point("E", 4, "W")))
        self.assertEqual(self.player.planes_alive, 0)
