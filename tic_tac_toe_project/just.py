# counter = 1
# prepare board:   # _ _ _
                   # _ _ _
                   # _ _ _
import functions as t


# x player - play - first
#   counter += 1
#   input location - valid: 1. 1-3/1-3 2. free
#   put x in the board
#   draw the board
#   check if won:
    #   check each row of x
    #   check each column of x
    #   check 2 diagonal of x
#   check if board is full --> tie (counter == 9)

# o player - play - second
#   counter += 1
#   input location - valid: 1. 1-3/1-3 2. free
#   put x in the board
#   draw the board
#   check if won
    #   check each row of o
    #   check each column of o
    #   check 2 diagonal of 0
#   - check if board is full --> tie ### DONT NEED TO USE IT BECAUSE ON ODD BOARD THE FIRST WALLEYES WILL BE THE FIRST TO END



# X O X
# O X O
# X O X


# board2 = [
# ['_', '_', '_'],
# ['_', '_', '_'],
# ['_', '_', '_']
# ]
# for i in board2:
#     print(" ".join(i))




board = {
    (1, 1): "x", (1, 2): "x", (1, 3): "x",
    (2, 1): "_", (2, 2): "_", (2, 3): "_",
    (3, 1): "_", (3, 2): "_", (3, 3): "_"
}

# t.game(t.game_data())

t.game(t.game_data())



#
# board[1, 1] = "o"
# print(board)
# row1 = (board[(1, 1)], board[(1, 2)], board[(1, 3)])
# if row1 == ('x', 'x', 'x'):
#     print(True)

#
#
#
# for (x, y), value in board.items():
#     if y == 3:
#         print((x, y), value, "\n", end="")
#     else:
#         print((x, y), value, end=" ")
#
# def check_win_test(board1: dict):
#     if all(board1[(1, 1), (1, 2), (1, 3)]) == "x":
#         return True
#     else:
#         return False
#
# print(check_win_test(board))
# player = ["x", "o"]

# board[(1, 1)] = "X" # making the change
# board[(1, 2)] = "X" # making the change
# board[(1, 3)] = "X" # making the change


# if game["board"][(1, 1)] == player and game["board"][(1, 2)] == player and game["board"][(1, 3)] == player:
#     print(player, "win")
# if game["board"][(2, 1)] == player and game["board"][(2, 2)] == player and game["board"][(2, 3)] == player:
#     print(player, "win")
# if game["board"][(3, 1)] == player and game["board"][(3, 2)] == player and game["board"][(3, 3)] == player:
#     print(player, "win")
# if game["board"][(1, 1)] == player and game["board"][(2, 1)] == player and game["board"][(3, 1)] == player:
#     print(player, "win")
# if game["board"][(1, 2)] == player and game["board"][(2, 2)] == player and game["board"][(3, 2)] == player:
#     print(player, "win")
# if game["board"][(1, 3)] == player and game["board"][(2, 3)] == player and game["board"][(3, 3)] == player:
#     print(player, "win")
# if game["board"][(1, 1)] == player and game["board"][(2, 2)] == player and game["board"][(3, 3)] == player:
#     print(player, "win")
# if game["board"][(1, 3)] == player and game["board"][(2, 2)] == player and game["board"][(3, 1)] == player:
#     print(player, "win")

# print(board)
# print(x_win)

# print(x, value, end=" ")
# if y == 3:
#     print(x, value)

"""
by the tuple (x, y) can indicate placement
x == row
y == column
"""
# print(" ".join(i))


# functions.check_win(board, player)

# for i in player:
#     print(i)



# board = functions.game_data()
# for key, value in board["board"].items():
#     print(key, value)
# functions.print_board(board)

# t.check_win(t.print_board(t.game_data()))
