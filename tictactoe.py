"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    num_of_x = 0
    num_of_o = 0
    for row in board:
        num_of_x+= row.count(X)
        num_of_o += row.count(O)

    if num_of_x == num_of_o:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_moves= set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_moves.add((i, j))
    return available_moves


def result(board,action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = deepcopy(board)
    if result_board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid Move")
    result_board[action[0]][action[1]] = player(board)

    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    columns = []

    for row in board:
        num_of_x = row.count(X)
        num_of_o = row.count(O)
        if num_of_x == 3:
            return X
        if num_of_o == 3:
            return O


    for j in range(len(board)):
        column = [row[j] for row in board]
        columns.append(column)

    for j in columns:
        num_of_x= j.count(X)
        num_of_o= j.count(O)
        if num_of_x == 3:
            return X
        if num_of_o == 3:
            return  0
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_spot = 0
    for row in board:
        empty_spot += row.count(EMPTY)
    if empty_spot == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if current_player == X:
        l = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))
            if k > l:
                l = k
                best_move = action
    else:
        l = math.inf
        for action in actions(board):
            k = max_value(result(board, action))
            if k < l:
                l = k
                best_move = action
    return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    l = -math.inf
    for action in actions(board):
        l = max(l, min_value(result(board, action)))
    return l

def min_value(board):
    if terminal(board):
        return utility(board)
    l = math.inf
    for action in actions(board):
        l = min(l, max_value(result(board, action)))
    return l



