import unittest
from unittest.mock import MagicMock
from code.maintain_distance import Car, DistanceSensor


class CarTests(unittest.TestCase):
    def setUp(self):
        self.distance_sensor = DistanceSensor()
        self.car = Car(self.distance_sensor)

    def test_maintain_safe_distance(self):
        # Set up distance sensor to return a distance less than 2
        self.distance_sensor.get_distance = MagicMock(return_value=1.5)

        # Capture the output of the move method
        with captured_output() as (out, err):
            self.car.move()

        # Assert that the car maintains a safe distance from surrounding objects
        output = out.getvalue().strip()
        self.assertEqual("Maintaining safe distance from surrounding objects.", output)

    def test_move_forward(self):
        # Set up distance sensor to return a distance greater than or equal to 2
        self.distance_sensor.get_distance = MagicMock(return_value=2.5)

        # Capture the output of the move method
        with captured_output() as (out, err):
            self.car.move()

        # Assert that the car moves forward
        output = out.getvalue().strip()
        self.assertEqual("Moving forward.", output)


class DistanceSensorTests(unittest.TestCase):
    def setUp(self):
        self.distance_sensor = DistanceSensor()

    def test_get_distance_returns_float(self):
        # Call the get_distance method
        result = self.distance_sensor.get_distance()

        # Assert that the result is a float
        self.assertIsInstance(result, float)


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
