from models.passenger_plane import PassengerPlane
from models.cargo_plane import CargoPlane

class AirlineCompany:
    def __init__(self):
        self.fleet = []

    def load_from_file(self, filename):
        import json
        with open(filename, 'r') as f:
            data = json.load(f)

        for plane in data:
            plane_type = plane.pop("type")
            if plane_type == "passenger":
                self.fleet.append(PassengerPlane(**plane))
            elif plane_type == "cargo":
                self.fleet.append(CargoPlane(**plane))



    def total_passenger_capacity(self):
        return sum(p.passenger_capacity for p in self.fleet if isinstance(p, PassengerPlane))

    def total_cargo_capacity(self):
        return sum(p.cargo_capacity for p in self.fleet if isinstance(p, CargoPlane))

    def sort_by_range(self):
        return sorted(self.fleet, key=lambda p: p.flight_range)

    def find_by_fuel_consumption(self, min_val, max_val):
        return [p for p in self.fleet if min_val <= p.fuel_consumption <= max_val]
