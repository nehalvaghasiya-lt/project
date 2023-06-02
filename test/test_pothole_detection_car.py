import unittest
from unittest.mock import MagicMock
from code.pothole_detection_car import Car, PotholeDetector


class CarTests(unittest.TestCase):
    def setUp(self):
        self.pothole_detector = PotholeDetector()
        self.car = Car(self.pothole_detector)

    def test_drive_forward_when_no_pothole_detected(self):
        # Set up pothole detector to return False for detect_pothole
        self.pothole_detector.detect_pothole = MagicMock(return_value=False)

        # Capture the output of the move method
        with captured_output() as (out, err):
            self.car.move()

        # Assert that the car drives forward
        output = out.getvalue().strip()
        self.assertEqual("Driving forward.", output)

    def test_avoid_pothole_when_pothole_detected(self):
        # Set up pothole detector to return True for detect_pothole
        self.pothole_detector.detect_pothole = MagicMock(return_value=True)

        # Capture the output of the move method
        with captured_output() as (out, err):
            self.car.move()

        # Assert that the car avoids the pothole
        output = out.getvalue().strip()
        self.assertEqual("Avoiding pothole.", output)


class PotholeDetectorTests(unittest.TestCase):
    def setUp(self):
        self.pothole_detector = PotholeDetector()

    def test_detect_pothole_returns_boolean(self):
        # Call the detect_pothole method
        result = self.pothole_detector.detect_pothole()

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
