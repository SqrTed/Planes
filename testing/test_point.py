from unittest import TestCase

from domain.entities import Point


class TestPoint(TestCase):
    def setUp(self):
        self.p = Point("A", 2, "Default")

    def test_x_setup(self):
        self.assertEqual(self.p.x, 1)

    def test_x(self):
        self.p.x = "B"
        self.assertEqual(self.p.x, "B")

    def test_y_setup(self):
        self.assertEqual(self.p.y, 2)

    def test_y(self):
        self.p.y = 1
        self.assertEqual(self.p.y, 1)

    def test_value_setup(self):
        self.assertEqual(self.p.value, "Default")

    def test_value(self):
        self.p.value = "Yes"
        self.assertEqual(self.p.value, "Yes")

    def test_str(self):
        self.assertEqual(str(self.p), str(self.p.x) + " " + str(self.p.y) + " " + str(self.p.value))
