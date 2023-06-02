import unittest
from unittest.mock import patch
from contextlib import contextmanager
from io import StringIO
from code.car_movement_pedestrian import Car, GPS
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
        self.gps = GPS()
        self.car = Car(self.gps)

    @patch.object(GPS, 'is_pedestrian_zone', return_value=False)
    def test_move_towards_destination_when_not_in_pedestrian_zone(self, _):
        """Car should move towards destination if it's not a pedestrian zone."""
        # Arrange
        destination = "Mall"

        # Act
        with capture_stdout() as output:
            self.car.move(destination)

        # Assert
        expected_output = "Moving towards destination."
        self.assertEqual(expected_output, output.getvalue().strip())

    @patch.object(GPS, 'is_pedestrian_zone', return_value=True)
    def test_cannot_enter_pedestrian_zones(self, _):
        """Car shouldn't be able to enter pedestrian zones."""
        # Arrange
        destination = "Park"

        # Act
        with capture_stdout() as output:
            self.car.move(destination)

        # Assert
        expected_output = "Cannot enter pedestrian-only zones."
        self.assertEqual(expected_output, output.getvalue().strip())


class TestGPS(unittest.TestCase):

    def setUp(self):
        self.gps = GPS()

    def test_is_pedestrian_zone_returns_true_for_pedestrian_zone(self):
        """GPS should return True if the location is a pedestrian zone."""
        # Arrange
        location = "Park"

        # Act
        is_pedestrian = self.gps.is_pedestrian_zone(location)

        # Assert
        self.assertTrue(is_pedestrian)

    def test_is_pedestrian_zone_returns_false_for_non_pedestrian_zone(self):
        """GPS should return False if the location is not a pedestrian zone."""
        # Arrange
        location = "Mall"

        # Act
        is_pedestrian = self.gps.is_pedestrian_zone(location)

        # Assert
        self.assertFalse(is_pedestrian)


if __name__ == '__main__':
    unittest.main()

