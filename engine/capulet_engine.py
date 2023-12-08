from engine.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__() # only necessary if Engine has non-argument attributes later
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        # if we have driven 30000 miles since last service, time for another
        return self.current_mileage - self.last_service_mileage > 30000
