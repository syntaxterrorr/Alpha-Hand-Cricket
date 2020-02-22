import pymysql
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

conn = pymysql.connect(host=config['Databse Connection']['database.host'],
                            user=config['Databse Connection']['database.user'],
                            password=config['Databse Connection']['database.password'],
                            db=config['Databse Connection']['database.dbname'],
                            cursorclass=pymysql.cursors.DictCursor)

def write_to_db(query, params):
    with conn.cursor() as cur:
        cur.execute(query, params)


class User:
    
    def __init__(self, user_name=None, user_id=None):
        self.id = user_id
        self.name = user_name
    
    def write(self):
        query = "INSERT INTO User (User_Name) VALUES (%s)"
        write_to_db(query, (self.name))


class Game:
    
    def __init__(self, user=None, is_user_winner=False, crix_score=0, user_score=0, is_winner_not_out=False, game_id=None):
        self.id = game_id
        self.user = user
        self.is_user_winner = is_user_winner
        self.crix_score = crix_score
        self.user_score = user_score
        self.is_winner_not_out = is_winner_not_out


class Turn:
    
    def __init__(self, game=None, innings_no=None, crix_move=0, user_move=0, turn_id=None):
        self.id = turn_id
        self.game = game
        self.innings_no = innings_no
        self.crix_move = crix_move
        self.user_move = user_move


class Toss (Turn):
    
    def __init__(self, is_user_choice_even=None, is_user_winner=None, is_winner_choice_batting=None, game=None, innings_no=None, crix_move=0, user_move=0, turn_id=None):
        super().__init__(game, innings_no, crix_move, user_move, turn_id)
        self.is_user_choice_even = is_user_choice_even
        self.is_user_winner = is_user_winner
        self.is_winner_choice_batting = is_winner_choice_batting


class Delivery (Turn):
    
    def __init__(self, is_user_batting=None, game=None, innings_no=None, crix_move=0, user_move=0, turn_id=None):
        super().__init__(game, innings_no, crix_move, user_move, turn_id)
        self.is_user_batting = is_user_batting
