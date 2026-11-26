class DriverAccount:
    def __init__(self, name, vehicle_plate, rating=5, total_trips=0):
        self.name = name
        self.vehicle_plate = vehicle_plate
        self.__rating = rating
        self.__total_trips = total_trips


    def add_rating(self, new_rating):
        if new_rating < 1 or new_rating > 5:
            print("Invalid rating. Please provide a rating between 1 and 5.")
            return

        self.__rating = (
            float(self.__rating) * self.__total_trips + new_rating
        ) / (self.__total_trips + 1)
        self.__total_trips += 1

    def get_rating(self):
        print(f"Trips made: {self.__total_trips}, Rating: {self.__rating}")