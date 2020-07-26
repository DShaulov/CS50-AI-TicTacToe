class StackFrontier():
    def __init__(self):
        pass

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
