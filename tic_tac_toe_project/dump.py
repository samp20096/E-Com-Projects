# game data:
def game_data() -> dict:
    """
    board structer:
        first in tuple is the row
        second in tuple is the column
    """
    return {
        "board": {
            (1, 1): "_", (1, 2): "_", (1, 3): "_",
            (2, 1): "_", (2, 2): "_", (2, 3): "_",
            (3, 1): "_", (3, 2): "_", (3, 3): "_"
        },
        "player": ["x", "o"],
        "counter": 1
    }


def print_board(game: dict) -> dict:
    """
    will print the board each time that: game start, turn start, game finish
    can use for checking condition of the game - win? tie?
    """
    for (x, y), value in game["board"].items():
        if y == 3:
            print(value, "\n", end="")
        else:
            print(value, end=" ")

def pick_square():
    square = input("What square you want to place[Row, Column]? ")
    return square

def check_quare(game: dict, player_move):
    for (x, y) in game["board"].keys():
        if player_move == (x, y) and game["board"][(x, y)] == "_":
            game["board"][player_move] = "X"
            print("placed")



def play_x_o():
    """
    1. print the current status of board with print_board()
    2. asking the player where to put X/O (turn of X/O will decide)
    3. checking if player input is BLANK on board
        * if BLANK - add to game board
            * go to the next turn
        * if NOT BLANK - ask for another input from the player
        * if all NOT BLANK for X turn - False, that can't be
        * if all NOT BLANK for O turn - is draw
            * end the game and tell the players that it's draw an print the board
    """
    game_new = game_data()

    # player X turn
    while True:
        print_board(game_new)
        square_picked = pick_square()
        check_quare(game_new, square_picked)





def check_win(game, player):
    player_x = ("x", "x", "x")
    player_o = ("o", "o", "o")
    condition_check = {
        "row": [
            ((1, 1), (1, 2), (1, 3)),
            ((2, 1), (2, 2), (2, 3)),
            ((3, 1), (3, 2), (3, 3))
        ],
        "col": [
            ((1, 1), (2, 1), (3, 1)),
            ((1, 2), (2, 2), (3, 2)),
            ((1, 3), (2, 3), (3, 3))
        ],
        "diag": [
            ((1, 1), (2, 2), (3, 3)),
            ((1, 3), (2, 2), (3, 1))
        ]
    }
    for i in player:
        # row
        condition_check_list = []
        for row in range(len(condition_check["row"])):
            print(row)
            for row1, col in enumerate(condition_check["row"][row]):
                if i == game[col]:
                    print(f"{row1} - {col} Good")
                    condition_check_list.append(col)
                else:
                    print(f"{row1} - {col} BLANK")
            if len(condition_check_list) == 3:
                print(f"Row - {i}")
            else:
                print(f"Not Row - {i}")
        condition_check_list.clear()

    for i in player:        # column
        for col in range(len(condition_check["col"])):
            print(col)
            condition_check_list = []
            for row1, col1 in enumerate(condition_check["col"][row]):
                if i == game[col1]:
                    print(f"{row1} - {col1} Good")
                    condition_check_list.append(col1)
                else:
                    print(f"{row1} - {col} BLANK")
            if len(condition_check_list) == 3:
                print(f"Row - {i}")
            else:
                print(f"Not Row - {i}")

            # for i in game[col]:
            #     print(i)
            # print(condition_check["row"][row][row1])
            # print(row1, col)
            #    index, value
            # if loc == game[loc] and :

        # print(f"{row}", condition_check["row"][row])




def check_draw(game):
    if game["counter"] >= 9:
        print("Game ended by Tie")


(board["board"][(1, 1)], board["board"][(1, 2)], board["board"][(1, 3)]),
(board["board"][(2, 1)], board["board"][(2, 2)], board["board"][(2, 3)]),
(board["board"][(3, 1)], board["board"][(3, 2)], board["board"][(3, 3)])
