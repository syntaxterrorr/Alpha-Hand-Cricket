class User:
    
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name


class Game:
    
    def __init__(self, game_id):
        self.id = game_id


class Turn:
    
    def __init__(self, turn_id):
        self.id = turn_id


class Toss (Turn):
    
    def __init__(self, turn_id):
        super().__init__(turn_id) 


class Delivery (Turn):
    
    def __init__(self, turn_id):
        super().__init__(turn_id) 
