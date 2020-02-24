USE alpha_hand_cricket;

CREATE TABLE User (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(30) NOT NULL
);

CREATE TABLE Game (
    game_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    is_user_winner BOOLEAN NOT NULL,
    crix_score INT NOT NULL,
    user_score INT NOT NULL,
    is_winner_not_out BOOLEAN NOT NULL,
    game_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE Turn (
    turn_id INT PRIMARY KEY AUTO_INCREMENT,
    game_id INT NOT NULL,
    innings_no TINYINT,
    crix_move TINYINT NOT NULL,
    user_move TINYINT NOT NULL,
    FOREIGN KEY (game_id) REFERENCES Game(game_id),
    CHECK (crix_move >= 0 AND crix_move <=6 AND user_move >= 0 AND user_move <=6)
);

CREATE TABLE Toss (
    turn_id INT PRIMARY KEY,
    is_user_choice_even BOOLEAN NOT NULL,
    is_user_winner BOOLEAN NOT NULL,
    is_winner_choice_batting BOOLEAN NOT NULL,
    FOREIGN KEY (turn_id) REFERENCES Turn(turn_id)
);

CREATE TABLE Delivery (
    turn_id INT PRIMARY KEY,
    is_user_batting BOOLEAN NOT NULL,
    FOREIGN KEY (turn_id) REFERENCES Turn(turn_id)
);
