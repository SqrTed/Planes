from unittest import TestCase

from domain.entities import Point, Plane


class TestPlane(TestCase):
    def setUp(self):
        self.head = Point("E", 4, "W")

    def test_coordinates(self):
        plane = Plane(self.head)
        self.assertEqual(len(plane.coordinates()),10)
        self.head.value="N"
        self.assertEqual(len(plane.coordinates()), 10)
        self.head.value = "S"
        self.assertEqual(len(plane.coordinates()), 10)
        self.head.value = "E"
        self.assertEqual(len(plane.coordinates()), 10)


