
from ride import Ride


class PremiumRide(Ride):

    def __init__(self, distance_km, snack):
        # Initialize the parent class
        super().__init__(distance_km)

        # Private attributes
        self.__complimentary_snack = snack
        self.__premium_base_rate = 15.00

    def calculate_fare(self):
        # Premium base rate + Php 3.00 per kilometer
        return self.__premium_base_rate + (self.distance_km * 3.00)

    def start_ride(self):
        print("Starting VIP Premium Ride. Enjoy your snacks!")

    def complete_ride(self):
        print("\n=== VIP RECEIPT ===")
        print(f"Fare: Php {self.calculate_fare():.2f}")
        print(f"Complimentary Snack Served: {self.__complimentary_snack}")
        print("===================")

