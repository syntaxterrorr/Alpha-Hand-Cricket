INSERT INTO User (User_ID, User_Name)
VALUES
    (1, "John Doe"),
    (2, "Jane Doe");

INSERT INTO Game (Game_ID, User_ID, is_user_winner, Crix_Score, User_Score, is_winner_not_out)
VALUES
    (1, 1, TRUE, 7, 25, FALSE),
    (2, 1, TRUE, 5, 9, TRUE),
    (3, 2, FALSE, 3, 0, FALSE);

INSERT INTO Turn (Turn_ID, Game_ID, Innings_No, Crix_Move, User_Move)
VALUES
    (1, 1, NULL, 5, 1),
    (2, 1, 1, 3, 6),
    (3, 1, 1, 4, 6),
    (4, 1, 1, 6, 5),
    (5, 1, 1, 1, 5),
    (6, 1, 1, 6, 3),
    (7, 1, 1, 3, 3),
    (8, 1, 2, 3, 1),
    (9, 1, 2, 4, 6),
    (10, 1, 2, 6, 1),
    (11, 2, NULL, 6, 3),
    (12, 2, 1, 5, 4),
    (13, 2, 1, 6, 6),
    (14, 2, 2, 5, 1),
    (15, 2, 2, 6, 2),
    (16, 2, 2, 5, 6),
    (17, 3, NULL, 1, 2),
    (18, 3, 1, 3, 4),
    (19, 3, 1, 4, 4),
    (20, 3, 1, 5, 5);

INSERT INTO Toss (Turn_ID, is_user_choice_even, is_user_winner, is_winner_choice_batting)
VALUES
    (1, TRUE, TRUE, TRUE),
    (11, TRUE, FALSE, TRUE),
    (17, FALSE, TRUE, FALSE);

INSERT INTO Delivery (Turn_ID, is_user_batting)
VALUES
    (2, TRUE),
    (3, TRUE),
    (4, TRUE),
    (5, TRUE),
    (6, TRUE),
    (7, TRUE),
    (8, FALSE),
    (9, FALSE),
    (10, FALSE),
    (12, FALSE),
    (13, FALSE)
    (14, TRUE),
    (15, TRUE),
    (16, TRUE),
    (18, FALSE),
    (19, FALSE),
    (20, TRUE);