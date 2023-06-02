class Car:
    def __init__(self, street_map):
        self.street_map = street_map

    def move(self, street_name, direction):
        if not self.street_map.is_one_way(street_name, direction):
            print("Moving forward on the street.")
        else:
            print("Cannot enter a one-way street in the wrong direction.")


class StreetMap:
    def is_one_way(self, street_name, direction):
        # Simulating street map data
        one_way_streets = {
            "Main Street": "East",
            "Broadway": "North",
            "Elm Street": "South"
        }

        if street_name in one_way_streets:
            return one_way_streets[street_name] != direction
        else:
            return False


def main():
    street_map = StreetMap()
    car = Car(street_map)

    street_name = "Main Street"  # Example street name
    direction = "West"  # Example direction

    car.move(street_name, direction)


if __name__ == '__main__':
    main()
