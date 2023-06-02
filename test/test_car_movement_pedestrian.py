import unittest
from unittest.mock import MagicMock
from code.car_movement_pedestrian import Car, GPS


class CarTests(unittest.TestCase):
    def setUp(self):
        self.gps = GPS()
        self.car = Car(self.gps)

    def test_move_towards_destination_when_not_in_pedestrian_zone(self):
        # Set up GPS to return False for is_pedestrian_zone
        self.gps.is_pedestrian_zone = MagicMock(return_value=False)

        # Capture the output of the move method
        with captured_output() as (out, err):
            self.car.move("Mall")

        # Assert that the car moves towards the destination
        output = out.getvalue().strip()
        self.assertEqual("Moving towards destination.", output)

    def test_cannot_enter_pedestrian_zones(self):
        # Set up GPS to return True for is_pedestrian_zone
        self.gps.is_pedestrian_zone = MagicMock(return_value=True)

        # Capture the output of the move method
        with captured_output() as (out, err):
            self.car.move("Park")

        # Assert that the car cannot enter pedestrian-only zones
        output = out.getvalue().strip()
        self.assertEqual("Cannot enter pedestrian-only zones.", output)


class GPSTests(unittest.TestCase):
    def setUp(self):
        self.gps = GPS()

    def test_is_pedestrian_zone_returns_true_for_pedestrian_zone(self):
        # Call the is_pedestrian_zone method with a pedestrian zone
        is_pedestrian = self.gps.is_pedestrian_zone("Park")

        # Assert that it returns True for pedestrian zone
        self.assertTrue(is_pedestrian)

    def test_is_pedestrian_zone_returns_false_for_non_pedestrian_zone(self):
        # Call the is_pedestrian_zone method with a non-pedestrian zone
        is_pedestrian = self.gps.is_pedestrian_zone("Mall")

        # Assert that it returns False for non-pedestrian zone
        self.assertFalse(is_pedestrian)


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
