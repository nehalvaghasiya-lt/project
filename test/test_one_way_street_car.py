import unittest
from unittest.mock import patch
from contextlib import contextmanager
from io import StringIO
from code.one_way_street_car import Car, StreetMap
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
        self.street_map = StreetMap()
        self.car = Car(self.street_map)

    @patch.object(StreetMap, 'is_one_way', return_value=False)
    def test_move_forward_on_non_one_way_street(self, _):
        """Car should move forward on a non one-way street."""
        # Arrange
        street_name = "Main Street"
        direction = "West"

        # Act
        with capture_stdout() as output:
            self.car.move(street_name, direction)

        # Assert
        expected_output = "Moving forward on the street."
        self.assertEqual(expected_output, output.getvalue().strip())

    @patch.object(StreetMap, 'is_one_way', return_value=True)
    def test_cannot_enter_wrong_direction_on_one_way_street(self, _):
        """Car should not be able to move in the wrong direction on a one-way street."""
        # Arrange
        street_name = "Main Street"
        direction = "West"

        # Act
        with capture_stdout() as output:
            self.car.move(street_name, direction)

        # Assert
        expected_output = "Cannot enter a one-way street in the wrong direction."
        self.assertEqual(expected_output, output.getvalue().strip())


class TestStreetMap(unittest.TestCase):

    def setUp(self):
        self.street_map = StreetMap()

    def test_is_one_way_returns_boolean(self):
        """StreetMap's is_one_way method should return a boolean value."""
        # Arrange
        street_name = "Main Street"
        direction = "West"

        # Act
        result = self.street_map.is_one_way(street_name, direction)

        # Assert
        self.assertIsInstance(result, bool)


if __name__ == '__main__':
    unittest.main()

