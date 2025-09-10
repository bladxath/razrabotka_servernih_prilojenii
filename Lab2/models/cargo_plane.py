from models.airplane import Airplane

class CargoPlane(Airplane):
    def __init__(self, model, flight_range, fuel_consumption, cargo_capacity):
        super().__init__(model, flight_range, fuel_consumption)
        self.cargo_capacity = cargo_capacity  # tons

    def __str__(self):
        return f"Cargo {super().__str__()} - Capacity: {self.cargo_capacity} tons"
