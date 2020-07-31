import copy

X = "X"
O = "O"
EMPTY = None

class StackQueue():
    def __init__(self):
        pass

    frontier = []
    
    def remove(self):
        removed_node = self.frontier.pop()
        return removed_node     

class Node():
    def __init__(self, parent, state, value):
        self.parent = parent
        self.state = state
        self.value = value

def explore_board(board):
    """
    returns a list of all possible board states
    """
    # return an empty list if the board is full
    num_of_empty = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                num_of_empty = num_of_empty + 1
    
    if num_of_empty == 0:
        return []
    # check whose turn it is
    num_x = 0
    num_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                num_x = num_x + 1
            if cell == O:
                num_o = num_o + 1

    if num_x == num_o:
        current_turn = X

    else:
        current_turn = O

    # check for empty cells and remember their index
    empty_index = []
    for row in enumerate(board):
        for cell in enumerate(row[1]):
            if cell[1] == EMPTY:
                empty_index.append((row[0], cell[0]))
    
    # create a list of all possible boards, with their corresponding moves
    possible_boards = []
    moves = []
    
    # choose an empty cell at random and fill it
    

    for row in enumerate(board):
        for cell in enumerate(row[1]):
            if cell[1] == EMPTY:
                # 
                board_copy = copy.deepcopy(board)
                board_copy[row[0]][cell[0]] = current_turn
                possible_boards.append(board_copy)
                moves.append((row[0], cell[0]))
                
    result = [possible_boards, moves]
    
    
    return result
