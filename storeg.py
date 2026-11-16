import json
class DataManager:
    def __init__(self, rooms_file ="rooms.json", bookings_file = "booking.json"):
        self.rooms_file = rooms_file
        self.bookings_file = bookings_file

    def load_rooms(self):
        with open (self.rooms_file, "r") as file:
            data = json.load(file)
            return data

    def load_bookings(self):
        with open (self.bookings_file, "r") as file:
            data = json.load(file)
            return data

    def save_rooms(self, rooms):
        with open (self.rooms_file, "w", encoding="utf-8") as file:
            json.dump(rooms, file, indent=2, ensure_ascii=False)

    def save_booking(self, booking):
        with open (self.bookings_file, "w", encoding="utf-8") as file:
            json.dump(booking, file, indent=2, ensure_ascii=False)



