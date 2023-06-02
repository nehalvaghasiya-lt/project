import unittest
from unittest.mock import MagicMock
from code.one_way_street_car import Car, StreetMap


class CarTests(unittest.TestCase):
    def setUp(self):
        self.street_map = StreetMap()
        self.car = Car(self.street_map)

    def test_move_forward_on_non_one_way_street(self):
        # Set up street map to return False for is_one_way
        self.street_map.is_one_way = MagicMock(return_value=False)

        # Capture the output of the move method
        with captured_output() as (out, err):
            self.car.move("Main Street", "West")

        # Assert that the car moves forward on the street
        output = out.getvalue().strip()
        self.assertEqual("Moving forward on the street.", output)

    def test_cannot_enter_wrong_direction_on_one_way_street(self):
        # Set up street map to return True for is_one_way
        self.street_map.is_one_way = MagicMock(return_value=True)

        # Capture the output of the move method
        with captured_output() as (out, err):
            self.car.move("Main Street", "West")

        # Assert that the car cannot enter the one-way street in the wrong direction
        output = out.getvalue().strip()
        self.assertEqual("Cannot enter a one-way street in the wrong direction.", output)


class StreetMapTests(unittest.TestCase):
    def setUp(self):
        self.street_map = StreetMap()

    def test_is_one_way_returns_boolean(self):
        # Call the is_one_way method
        result = self.street_map.is_one_way("Main Street", "West")

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
