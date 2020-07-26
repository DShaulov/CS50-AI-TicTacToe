"""
Tic Tac Toe Player
"""

import math
import helpers

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

    # if its the initial state, its the turn of X player
    if board == initial_state():
        return "X"
    # otherwise, if there are less O's than X's on the board, its O's turn
    num_x = 0
    num_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                num_x = num_x + 1
            if cell == O:
                num_o = num_o + 1

    if num_x == num_o:
        return X

    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    

    # if cell already full, raise exception
    if board[action[0]][action[1]] != EMPTY:
        raise KeyError

    # check whose turn it is
    num_x = 0
    num_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                num_x = num_x + 1
            if cell == O:
                num_o = num_o + 1

    # return a deep copy of the board with the taken action
    new_board = board
    
    if num_x == num_o:
        new_board[action[0]][action[1]] = X
    else:
        new_board[action[0]][action[1]] = O
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check the board rows for a winner
    for row in board:
        if row == [X, X, X]:
            return X
        if row == [O, O, O]:
            return O

    # check the columns for a winner
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == X:
        return X
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == O:
        return O

    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == X:
        return X
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == O:
        return O

    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == X:
        return X
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == O:
        return O
    
    # check diagonally for a winner
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == X:
        return X
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == O:
        return O

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == X:
        return X
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == O:
        return O

    # if no one won, return none
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # go over the board ROWS
    for row in board:
        if row == [X, X, X] or row == [O, O, O]:
            return True 
    # go over the board COLUMNS
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return True

    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return True

    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return True
    # go over the board diagonally
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return True

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return True

    # check if the board is full
    for row in board:
        if None in row:
            return False
    # if the board is full and no one won, return true
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # check the rows for a winner
    for row in board:
        if row == [X, X, X]:
            return 1
        if row == [O, O, O]:
            return -1

    # check the columns for a winner
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == X:
        return 1
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == O:
        return -1

    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == X:
        return 1
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == O:
        return -1

    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == X:
        return 1
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == O:
        return -1
    
    # check diagonally for a winner
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == X:
        return 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == O:
        return -1

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == X:
        return 1
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == O:
        return -1

    # if no winner is found, its a tie
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # check whose turn it is
    num_x = 0
    num_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                num_x = num_x + 1
            if cell == O:
                num_o = num_o + 1
    
    if num_o == num_x:
        current_turn = X
    else:
        current_turn = O

    # create a stack frontier

    # add the current board to the frontier
    raise NotImplementedError

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def remove(self, node):
        removed_node = self.frontier[0]
        self.frontier = self.frontier[1::]
        return removed_node

class Node():
    def __init__(self):
        self.action = action
        self.parent = parent
        self.state = state
        self.value = value

def explore_board(board):
    """
    returns a list of all possible boards
    """
    raise NotImplementedError



