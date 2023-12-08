import sys
from datetime import datetime
sys.path.append("../forage-lyft-starter-repo1")
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine

from engine.car import Car
from engine.battery.nubbin_battery import NubbinBattery

from engine.battery.spindler_battery import SpindlerBattery
from datetime import datetime

class CarFactory():
    def __init__():
        pass

    """+ create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
    + create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
    + create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool): Car
    + create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
    + create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car"""

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):

        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool):

        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))
        
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))

    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))
