import random


class FakeHotelGenerator:

    def generate_hotel_name(self):
        return f'Hotel-{random.randint(0, 9999)}'

    def generate_address(self):
        return f'{random.randint(0, 9999)} Amphitheatre Parkway Mountain View'





