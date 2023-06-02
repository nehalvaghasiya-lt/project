import unittest
from unittest.mock import patch
from contextlib import contextmanager
from io import StringIO
from code.maintain_distance import Car, DistanceSensor
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
        self.distance_sensor = DistanceSensor()
        self.car = Car(self.distance_sensor)

    @patch.object(DistanceSensor, 'get_distance', return_value=1.5)
    def test_maintain_safe_distance(self, _):
        """Car should maintain a safe distance from surrounding objects if distance is less than 2."""
        # Act
        with capture_stdout() as output:
            self.car.move()

        # Assert
        expected_output = "Maintaining safe distance from surrounding objects."
        self.assertEqual(expected_output, output.getvalue().strip())

    @patch.object(DistanceSensor, 'get_distance', return_value=2.5)
    def test_move_forward(self, _):
        """Car should move forward if distance is greater than or equal to 2."""
        # Act
        with capture_stdout() as output:
            self.car.move()

        # Assert
        expected_output = "Moving forward."
        self.assertEqual(expected_output, output.getvalue().strip())


class TestDistanceSensor(unittest.TestCase):

    def setUp(self):
        self.distance_sensor = DistanceSensor()

    def test_get_distance_returns_float(self):
        """DistanceSensor's get_distance method should return a float value."""
        # Act
        result = self.distance_sensor.get_distance()

        # Assert
        self.assertIsInstance(result, float)


if __name__ == '__main__':
    unittest.main()

