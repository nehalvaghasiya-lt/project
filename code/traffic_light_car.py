class Car:
    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def move(self):
        if self.traffic_light.is_red():
            print("Waiting at the red light.")
        else:
            print("Crossing the intersection.")


class TrafficLight:
    def is_red(self):
        # Simulating traffic light status
        return True  # Replace with actual traffic light logic


def main():
    traffic_light = TrafficLight()
    car = Car(traffic_light)
    car.move()


if __name__ == '__main__':
    main()
