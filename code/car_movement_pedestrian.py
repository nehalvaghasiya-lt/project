class Car:
    def __init__(self, gps):
        self.gps = gps

    def move(self, destination):
        if not self.gps.is_pedestrian_zone(destination):
            print("Moving towards destination.")
        else:
            print("Cannot enter pedestrian-only zones.")


class GPS:
    def is_pedestrian_zone(self, location):
        # Simulating GPS check for pedestrian zones
        pedestrian_zones = ["Park", "Plaza", "Sidewalk"]
        return location in pedestrian_zones


def main():
    gps = GPS()
    car = Car(gps)
    destination = "Mall"  # Example destination

    car.move(destination)


if __name__ == '__main__':
    main()
