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
        query = 'SELECT LAST_INSERT_ID() AS id'
        cur.execute(query);
        id = cur.fetchone()['id']
        return id

def close_mysql_connection():
    conn.close()


class User:
    
    def __init__(self, user_name=None, user_id=None):
        self.id = user_id
        self.name = user_name
    
    def write(self):
        query = "INSERT INTO User (User_Name) VALUES (%s)"
        self.id = write_to_db(query, (self.name))


class Game:
    
    def __init__(self, user=None, is_user_winner=False, crix_score=0, user_score=0, is_winner_not_out=False, game_id=None):
        self.id = game_id
        self.user = user
        self.is_user_winner = is_user_winner
        self.crix_score = crix_score
        self.user_score = user_score
        self.is_winner_not_out = is_winner_not_out
        self.turns = []

    def add_turn(self, turn):
        self.turns.append(turn)

    def end(self):
        for turn in turns:
            if turn.is_toss():
                continue
            if not turn.is_out():
                if turn.is_user_batting:
                    self.user_score += turn.user_move
                else:
                    self.crix_score += turn.crix_move
        if self.user_score > self.crix_score:
            self.is_user_winner = True
        if not turns[-1].is_out:
            self.is_winner_not_out = True

    def write(self):
        query = "INSERT INTO Game (user_id, is_user_winner, crix_score, user_score, is_winner_not_out) VALUES (%s, %s, %s, %s, %s)"
        self.id = write_to_db(query, (self.user.id, self.is_user_winner, self.crix_score, self.user_score, self.is_winner_not_out))
        for turn in turns:
            turn.write()


class Turn:
    
    def __init__(self, game=None, innings_no=None, crix_move=0, user_move=0, turn_id=None):
        self.id = turn_id
        self.game = game
        self.innings_no = innings_no
        self.crix_move = crix_move
        self.user_move = user_move
    
    def is_toss(self):
        if self.innings_no:
            return False
        return True
    
    def write(self):
        query = "INSERT INTO Turn (game_id, Innings_No, crix_move, user_move) VALUES (%s, %s, %s, %s)"
        self.id = write_to_db(query, (self.game.id, self.innings_no, self.crix_move, self.user_move))


class Toss (Turn):

    def __init__(self, is_user_choice_even=None, is_winner_choice_batting=None, game=None, innings_no=None, crix_move=0, user_move=0, turn_id=None):
        super().__init__(game, innings_no, crix_move, user_move, turn_id)
        self.is_user_choice_even = is_user_choice_even
        self.is_winner_choice_batting = is_winner_choice_batting

        sum = self.crix_move + self.user_move
        if self.is_user_choice_even ^ (sum % 2 == 0) :
            self.is_user_winner = True
        else:
            self.is_user_winner = False

    def write(self):
        super().write()
        query = "INSERT INTO Toss (turn_id, is_user_choice_even, is_user_winner, is_winner_choice_batting) VALUES (%s, %s, %s, %s)"
        write_to_db(query, (self.id, self.is_user_choice_even, self.is_user_winner, self.is_winner_choice_batting))


class Delivery (Turn):

    def __init__(self, is_user_batting=None, game=None, innings_no=None, crix_move=0, user_move=0, turn_id=None):
        super().__init__(game, innings_no, crix_move, user_move, turn_id)
        self.is_user_batting = is_user_batting

    def is_out(self):
        if self.crix_move == self.user_move:
            return True
        return False

    def write(self):
        super().write()
        query = "INSERT INTO Delivery (turn_id, is_user_batting)"
        write_to_db(query, (self.id, self.is_user_batting))
