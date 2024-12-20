def game_data() -> dict:
    return {
        "board": {
            (1, 1): "_", (1, 2): "_", (1, 3): "_",
            (2, 1): "_", (2, 2): "_", (2, 3): "_",
            (3, 1): "_", (3, 2): "_", (3, 3): "_"
        },
        "player": ["x", "o"],
        "counter": 0
    }


def print_board(board: dict) -> None:
    """
    will print the board each time that turn start
    """
    for (x, y), value in board.items():
        if y == 3:
            print(value, "\n", end="")
        else:
            print(value, end=" ")


def check_win(board) -> bool:
    player_x = ("x", "x", "x")
    player_o = ("o", "o", "o")
    condition_check = {
        "row": [
            (board[1, 1], board[1, 2], board[1, 3]),
            (board[2, 1], board[2, 2], board[2, 3]),
            (board[3, 1], board[3, 2], board[3, 3])
        ],
        "col": [
            (board[1, 1], board[2, 1], board[3, 1]),
            (board[1, 2], board[2, 2], board[3, 2]),
            (board[1, 3], board[2, 3], board[3, 3])
        ],
        "diag": [
            (board[1, 1], board[2, 2], board[3, 3]),
            (board[1, 3], board[2, 2], board[3, 1])
        ]
    }
    for condition_type in condition_check.values():
        for line in condition_type:
            if line == player_x or line == player_o:
                return True
    return False




def game(data):
    board = data["board"]
    players = data["player"] # ['x', 'o']
    counter = data["counter"] # 0


    while True:
        print_board(board)
        players_turn = players[counter % 2]
        print(f"Player {players_turn}'s turn.")
        try:
            x, y = map(int, input("Enter row and column ('1 2', '3 2' ...): ").split())
            if (x, y) not in board:
                print("Invalid position. Try again.")
                continue
            if board[(x, y)] != "_":
                print("Position already taken. Try again.")
                continue
        except ValueError:
            print("Invalid input. Enter two numbers separated by a space.")
            continue

        board[(x, y)] = players_turn
        counter += 1

        if check_win(board):
            print_board(board)
            print(f"Player {players_turn} wins!")
            break

        if counter == 9:
            print_board(board)
            print("It's a draw!")
            break


if __name__ == '__main__':
    game(game_data())