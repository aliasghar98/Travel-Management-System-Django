# from agency.business_logic.car_model import Car_Model
from .booking import Booking
from ..models import BOOKING
from django.core.exceptions import ObjectDoesNotExist

class BookingList:
    def __init__(self):
        pass

    def add_booking(self,trip,allocated_car,allocated_hotel,customer):
        new_booking = Booking(trip,allocated_car,allocated_hotel,customer)
        new_booking.save()