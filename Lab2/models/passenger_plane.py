from models.airplane import Airplane

class PassengerPlane(Airplane):
    def __init__(self, model, flight_range, fuel_consumption, passenger_capacity):
        super().__init__(model, flight_range, fuel_consumption)
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        return f"Passenger {super().__str__()} - Capacity: {self.passenger_capacity} pax"
