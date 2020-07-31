"""
Tic Tac Toe Player
"""

import math
from helpers import StackQueue, Node, explore_board
from random import randint

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
        if EMPTY in row:
            return False
    # if the board is full and no one won, return true
    else:
        return True

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
    # create a node using the input board
    input_node = Node(
        parent = None,
        state = board,
        value = None
    )
    # if board is terminal, return None
    if terminal(board) == True:
        return None

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
        current_player = X
    else:
        current_player = O

    # create a stack queue
    stack_queue = StackQueue()

    # explore the current board
    possible_boards = explore_board(board)[0]
    moves = explore_board(board)[1]
    # keep track of all the possible moves
    possible_move_nodes = []
    # create a node for each possible board
    for board_state in possible_boards:
        new_node = Node(
            parent = input_node,
            state = board_state,
            value = None
        )

        # add the new node to the frontier
        stack_queue.frontier.append(new_node)
        possible_move_nodes.append(new_node)
        
    # continue exploring the frontier while it is not empty
    while stack_queue.frontier != []:
        # remove a node from the frontier
        current_node = stack_queue.remove()
        # check if current node is terminal
        if terminal(current_node.state) == True:
            # check who won the game
            utility_value = utility(current_node.state)

            # assign to each node and its parent nodes the value
            while current_node.parent != None:
                current_node.value = utility_value
                current_node = current_node.parent
        
        if terminal(current_node.state) == False:
            # if current node is not terminal, explore it
            possible_board_states = explore_board(current_node.state)[0]

            # create a node for each board state and add it to the frontier
            for board_state in possible_board_states:
                new_node = Node(
                    parent = current_node,
                    value = None,
                    state = board_state
                )

                stack_queue.frontier.append(new_node)
    # once the frontier is empty, go over all the possible moves, and choose at random the ones that match the computers goal
    if current_player == X:
        optimal_moves = []
        for node in possible_move_nodes:
            if node.value == 1:
                # get the index of the node
                node_index = possible_move_nodes.index(node)
                move = moves(node_index)
                optimal_moves.append(move)

        # return a random optimal move
        random_index = randint(0, len(optimal_moves) - 1)
        return optimal_moves[random_index]
    
    if current_player == O:
        optimal_moves = []
        for node in possible_move_nodes:
            if node.value == -1:
                # get the index of the node
                node_index = possible_move_nodes.index(node)
                move = moves(node_index)
                optimal_moves.append(move)

        # return a random optimal move
        random_index = randint(0, len(optimal_moves) - 1)
        return optimal_moves[random_index]
        
        





