from engine.battery.battery import Battery
from datetime import datetime


class SpindlerBattery(Battery):

    def __init__(self, last_service_date, current_date):
        super().__init__()
        
        if (type(last_service_date) != datetime or type(current_date) != datetime):
            print("Battery last service date must be a date")
            exit(1)
            # it's important to have the program exit if they try to create this with the
            # wrong type of date, because otherwise other funcs won't work later
            
        self.last_service_date = last_service_date
        self.current_date = current_date

        

            # I do not see why current_date shouldn't be initialized like this, but it seems they
            # want it as an argument
        #self.current_date = datetime.today().date()

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if (self.current_date < service_threshold_date):
            return False
        else:
            return True
