USE alpha_hand_cricket;

CREATE TABLE User (
    User_ID INT PRIMARY KEY AUTO_INCREMENT,
    User_Name VARCHAR(30) NOT NULL
);

CREATE TABLE Game (
    Game_ID INT PRIMARY KEY AUTO_INCREMENT,
    User_ID INT NOT NULL,
    Winner BOOLEAN NOT NULL,
    Run_Diff INT,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID)
);

CREATE TABLE Turn (
    Turn_ID INT PRIMARY KEY AUTO_INCREMENT,
    Game_ID INT NOT NULL,
    Innings_No TINYINT NOT NULL,
    Crix_Move TINYINT,
    User_Move TINYINT,
    is_toss BOOLEAN,
    FOREIGN KEY (Game_ID) REFERENCES Game(Game_ID)
);

CREATE TABLE Toss (
    Turn_ID INT PRIMARY KEY,
    User_Choice BOOLEAN,
    Winner BOOLEAN NOT NULL,
    FOREIGN KEY (Turn_ID) REFERENCES Turn(Turn_ID)
);

CREATE TABLE Delivery (
    Turn_ID INT PRIMARY KEY,
    is_user_batting BOOLEAN NOT NULL,
    FOREIGN KEY (Turn_ID) REFERENCES Turn(Turn_ID)
);
