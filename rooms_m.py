class Room:
    def __init__(self, room_id ,name ,difficulty ,duration ,min_players ,max_players ,price_per_player, is_active):
        self.room_id = room_id
        self.name = name
        self.difficulty = difficulty
        self.duration = duration
        self.min_players = min_players
        self.max_players = max_players
        self.price_per_player = price_per_player
        self.is_active = is_active
    
    def activate(self):
        self.activate = True
    
    def deactivate(self):
        self.activate = False
    
    def is_valid_players(self, player):
        if player >= self.min_players and player <= self.max_players:
            return True
        else:
            return False

    def to_dict(self):
        dict_room = {
            "room_id": self.room_id,
            "name": self.name,
            "difficulty": self.difficulty,
            "duration": self.duration,
            "min_players": self.min_players,
            "max_players": self.max_players,
            "price_per_player": self.price_per_player,
            "is_active": self.is_active
        }   
        return dict_room
    @classmethod
    def from_dict(cls, dict):
        return Room(dict["room_id"], dict["name"], dict["difficolty"], 
        dict["duration"], dict["min_players"], dict["max_players"], 
        dict["price_per_player"], dict["is_active"])





