class Airplane:
    def __init__(self, model, flight_range, fuel_consumption):
        self.model = model
        self.flight_range = flight_range  # km
        self.fuel_consumption = fuel_consumption  # L/h

    def __str__(self):
        return f"{self.model} (Range: {self.flight_range} km, Fuel: {self.fuel_consumption} L/h)"
