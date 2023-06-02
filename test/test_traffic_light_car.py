import unittest
from unittest.mock import MagicMock
from code.traffic_light_car import Car, TrafficLight


class CarTests(unittest.TestCase):
    def setUp(self):
        self.traffic_light = TrafficLight()
        self.car = Car(self.traffic_light)

    def test_wait_at_red_light_when_traffic_light_is_red(self):
        # Set up traffic light to return True for is_red
        self.traffic_light.is_red = MagicMock(return_value=True)

        # Capture the output of the move method
        with captured_output() as (out, err):
            self.car.move()

        # Assert that the car waits at the red light
        output = out.getvalue().strip()
        self.assertEqual("Waiting at the red light.", output)

    def test_cross_intersection_when_traffic_light_is_green(self):
        # Set up traffic light to return False for is_red
        self.traffic_light.is_red = MagicMock(return_value=False)

        # Capture the output of the move method
        with captured_output() as (out, err):
            self.car.move()

        # Assert that the car crosses the intersection
        output = out.getvalue().strip()
        self.assertEqual("Crossing the intersection.", output)


class TrafficLightTests(unittest.TestCase):
    def setUp(self):
        self.traffic_light = TrafficLight()

    def test_is_red_returns_boolean(self):
        # Call the is_red method
        result = self.traffic_light.is_red()

        # Assert that the result is a boolean
        self.assertIsInstance(result, bool)


# Helper class for capturing stdout
from io import StringIO
import sys

class captured_output:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = self._captured_stdout = StringIO()
        return self._captured_stdout

    def __exit__(self, *args):
        sys.stdout = self._original_stdout


if __name__ == '__main__':
    unittest.main()
