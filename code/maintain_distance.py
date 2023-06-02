class Car:
    def __init__(self, distance_sensor):
        self.distance_sensor = distance_sensor

    def move(self):
        if self.distance_sensor.get_distance() < 2:
            print("Maintaining safe distance from surrounding objects.")
        else:
            print("Moving forward.")

class DistanceSensor:
    def get_distance(self):
        # Simulating distance measurement
        return 2.5  # Replace with actual distance measurement logic


def main():
    distance_sensor = DistanceSensor()
    car = Car(distance_sensor)
    car.move()


if __name__ == '__main__':
    main()
