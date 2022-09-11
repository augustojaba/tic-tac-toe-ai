"""
Tic Tac Toe Player
"""

import math
import copy
from collections import Counter


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

    count = dict(sum(map(Counter, board), Counter()))

    if not count.__contains__(EMPTY):
        return None

    return X if count[EMPTY] % 2 == 1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)

    if action not in possible_actions:
        raise Exception("Invalid action")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    bestAction = None

    if player(board) == X:
        value = math.inf * -1

        for action in actions(board):
            action_value = __min_value(result(board, action))
            if action_value > value:
                value = action_value
                bestAction = action
    
    else:
        value = math.inf

        for action in actions(board):
            action_value = __max_value(result(board, action))
            if action_value < value:
                value = action_value
                bestAction = action
    
    return bestAction

def __max_value(board):
    if terminal(board):
        return utility(board)

    value = math.inf * -1
    
    for action in actions(board):
        value = max(value, __min_value(result(board, action)))

    return value

def __min_value(board):
    if terminal(board):
        return utility(board)

    value = math.inf
    
    for action in actions(board):
        value = min(value, __max_value(result(board, action)))

    return value
