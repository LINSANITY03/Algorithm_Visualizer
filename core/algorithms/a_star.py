import heapq
from AlgoEngine import GameState


class Node:
    '''
    Represents a A* Node on a position
    '''

    def __init__(self, position) -> None:
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0


class AStar(GameState):
    '''
    Determines the shortest path distance between src and destination

    '''

    def __init__(self, source, destination) -> None:
        '''
        Setup the initial parameter for the search algorithms
        '''

        super().__init__()

        self.open = []
        self.closed = {}
        self.start = Node(source)
        self.close = Node(destination)

    def search(self):
        '''
        Create the logic for a* search returning shortest path if found
        '''

        heapq.heappush(self.open, self.start)
        while self.open:
            current_node = heapq.heappop(self.open)
            if current_node.position == self.close.position:
                print("Reached final")
                # add the all previous point with the current i.e end point to form
                # a line indicating the shortest path taken
            children = []
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                          [1, 1], [1, -1], [-1, -1], [-1, 1]]
            for x, y in directions:
                new_position = (
                    current_node.position[0] + x, current_node.position[1] + y)

                if (new_position[0] < 0 or new_position[0] > 10
                    or new_position[1] < 0 or new_position[1] > 0
                        or self.board[new_position[0]][new_position[1]] != "wall"):
                    continue


AStar((10, 0), (0, 0)).search()
