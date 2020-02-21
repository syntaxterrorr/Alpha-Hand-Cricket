USE alpha_hand_cricket;

CREATE TABLE User (
    User_ID INT PRIMARY KEY AUTO_INCREMENT,
    User_Name VARCHAR(30) NOT NULL
);

CREATE TABLE Game (
    Game_ID INT PRIMARY KEY AUTO_INCREMENT,
    User_ID INT NOT NULL,
    is_user_winner BOOLEAN NOT NULL,
    Run_Diff INT,
    Target_Required INT NOT NULL,
    Game_Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID)
);

CREATE TABLE Turn (
    Turn_ID INT PRIMARY KEY AUTO_INCREMENT,
    Game_ID INT NOT NULL,
    Innings_No TINYINT,
    Crix_Move TINYINT NOT NULL,
    User_Move TINYINT NOT NULL,
    is_toss BOOLEAN NOT NULL,
    FOREIGN KEY (Game_ID) REFERENCES Game(Game_ID),
    CHECK (Crix_Move >= 0 AND Crix_Move <=6 AND User_Move >= 0 AND User_Move <=6)
);

CREATE TABLE Toss (
    Turn_ID INT PRIMARY KEY,
    is_user_choice_even BOOLEAN NOT NULL,
    is_user_winner BOOLEAN NOT NULL,
    is_winner_choice_batting BOOLEAN NOT NULL,
    FOREIGN KEY (Turn_ID) REFERENCES Turn(Turn_ID)
);

CREATE TABLE Delivery (
    Turn_ID INT PRIMARY KEY,
    is_user_batting BOOLEAN NOT NULL,
    FOREIGN KEY (Turn_ID) REFERENCES Turn(Turn_ID)
);
