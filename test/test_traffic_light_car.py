import unittest
from unittest.mock import patch
from contextlib import contextmanager
from io import StringIO
from code.traffic_light_car import Car, TrafficLight
import sys


@contextmanager
def capture_stdout():
    """Context manager to capture stdout"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_stdout


class TestCar(unittest.TestCase):

    def setUp(self):
        self.traffic_light = TrafficLight()
        self.car = Car(self.traffic_light)

    @patch.object(TrafficLight, 'is_red', return_value=True)
    def test_wait_at_red_light_when_traffic_light_is_red(self, _):
        """Car should wait at red traffic light."""
        # Act
        with capture_stdout() as output:
            self.car.move()

        # Assert
        expected_output = "Waiting at the red light."
        self.assertEqual(expected_output, output.getvalue().strip())

    @patch.object(TrafficLight, 'is_red', return_value=False)
    def test_cross_intersection_when_traffic_light_is_green(self, _):
        """Car should cross the intersection when traffic light is green."""
        # Act
        with capture_stdout() as output:
            self.car.move()

        # Assert
        expected_output = "Crossing the intersection."
        self.assertEqual(expected_output, output.getvalue().strip())


class TestTrafficLight(unittest.TestCase):

    def setUp(self):
        self.traffic_light = TrafficLight()

    def test_is_red_returns_boolean(self):
        """TrafficLight's is_red method should return a boolean value."""
        # Act
        result = self.traffic_light.is_red()

        # Assert
        self.assertIsInstance(result, bool)


if __name__ == '__main__':
    unittest.main()

