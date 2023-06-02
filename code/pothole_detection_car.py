class Car:
    def __init__(self, pothole_detector):
        self.pothole_detector = pothole_detector

    def move(self):
        if self.pothole_detector.detect_pothole():
            self.avoid_pothole()
        else:
            self.drive()

    def drive(self):
        print("Driving forward.")

    def avoid_pothole(self):
        print("Avoiding pothole.")


class PotholeDetector:
    def detect_pothole(self):
        # Simulating pothole detection
        return True  # Replace with actual pothole detection logic


def main():
    pothole_detector = PotholeDetector()
    car = Car(pothole_detector)

    car.move()


if __name__ == '__main__':
    main()
