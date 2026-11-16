class Booking:
    def __init__(self, booking_id ,customer_name, room_id, booking_date, start_time, players, total_price, status ,cancellation_fee):
        self.booking_id = booking_id
        self.customer_name = customer_name 
        self.room_id = room_id
        self.booking_date = booking_date
        self.start_time =start_time
        self.players = players 
        self.total_price = total_price 
        self.status = status 
        self.cancellation_fee = cancellation_fee

    def cancel(self, fee):
        self.cancellation_fee += fee
        return self.cancellation_fee

    def update_details(self, booking_date, start_time, players, total_price):
        self.booking_date = booking_date
        self.start_time = start_time
        self.players = players
        self.total_price = total_price


    def to_dict(self):
        new_order = {
        "booking_id": self.booking_id,
        "customer_name": self.customer_name,
        "room_id": self.room_id,
        "booking_date": self.booking_date,
        "start_time": self.start_time,
        "players": self.players,
        "total_price": self.total_price,
        "status": self.status,
        "cancellation_fee": self.cancellation_fee
        }


    @classmethod
    def from_dict(cls, dict):
        return Booking(dict["booking_id"] , dict["customer_name"], dict["room_id"], 
        dict["booking_date"], dict["start_time"], dict["players"], dict["total_price"], 
        dict["status"], dict["cancellation_fee"])

class PricingManager:
    @staticmethod
    def calculate_price(room, players, booking_date):
        price =  room * players
        if players > 4 and players <= 6:
            price = round(price *0.9, 2)
        if players >= 7:
            price = round(price * 0.85, 2)
        return price

    def calculate_cancellation_fee(self):
        ...
