import unittest
from unittest.mock import patch
from contextlib import contextmanager
from io import StringIO
from code.pothole_detection_car import Car, PotholeDetector
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
        self.pothole_detector = PotholeDetector()
        self.car = Car(self.pothole_detector)

    @patch.object(PotholeDetector, 'detect_pothole', return_value=False)
    def test_drive_forward_when_no_pothole_detected(self, _):
        """Car should drive forward when no pothole is detected."""
        # Act
        with capture_stdout() as output:
            self.car.move()

        # Assert
        expected_output = "Driving forward."
        self.assertEqual(expected_output, output.getvalue().strip())

    @patch.object(PotholeDetector, 'detect_pothole', return_value=True)
    def test_avoid_pothole_when_pothole_detected(self, _):
        """Car should avoid potholes when a pothole is detected."""
        # Act
        with capture_stdout() as output:
            self.car.move()

        # Assert
        expected_output = "Avoiding pothole."
        self.assertEqual(expected_output, output.getvalue().strip())


class TestPotholeDetector(unittest.TestCase):

    def setUp(self):
        self.pothole_detector = PotholeDetector()

    def test_detect_pothole_returns_boolean(self):
        """PotholeDetector's detect_pothole method should return a boolean value."""
        # Act
        result = self.pothole_detector.detect_pothole()

        # Assert
        self.assertIsInstance(result, bool)


if __name__ == '__main__':
    unittest.main()

