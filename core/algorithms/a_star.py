import heapq
from core.Game_core import GameVariable as gv
import math


class Node:
    '''Represents a A* Node on a position
    '''

    def __init__(self, parent, position) -> None:
        """Initialize the variable to represent each node.

        Args:
          parent: Represents the position of previous visited node.
          position: Current position of the node.
        """
        self.parent = parent
        self.position = position

        # g represents distance from starting node
        # h cost represents distance from end node to current node
        # f = g + h

        self.g = 0
        self.h = 0
        self.f = 0

    def __repr__(self):
        return f'{self.position}'

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __eq__(self, other) -> bool:
        return self.position == other.position

    def __hash__(self) -> int:
        return hash(self.position)


def heuristic(a, b):
    '''Calculate the heuristic (Euclidean distance).

    Args:
      a, b: position of initial and final point.
    '''
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def reconstruct_path(start_node, end_node):
    '''
    Represent the shortest path.

    Args:
      start_node: Source node.
      end_node: Destination node.

    Returns:
      The path between source and destination node.
    '''
    total_path = []
    end_node = end_node.parent
    while end_node != start_node:
        total_path.append(end_node.position)
        end_node = end_node.parent
    return total_path[::-1]


class AStar:
    '''Determines the shortest path distance between source and destination using A* algorithm.
    '''

    def __init__(self, source, destination, gs) -> None:
        '''Setup the initial parameter for the search algorithms.

        Args:
          source: Represent the position (x, y) of source cell.
          destination: Represent the position (x, y) of destination cell.
          gs: Current game state.
        '''
        self.gs = gs
        self.open = []
        self.closed = set()
        self.start = Node(None, source)
        self.end = Node(None, destination)

    def search(self):
        '''Create the logic for a* search returning shortest path if found.
        '''
        heapq.heappush(self.open, self.start)
        while self.open:
            if (len(self.open) + len(self.closed) + len(self.gs.wall)) == 400:
                return None

            current_node = heapq.heappop(self.open)
            self.closed.add(current_node)

            if current_node == self.end:
                # add the all previous point with the current i.e end point to form
                # a line indicating the shortest path taken
                return reconstruct_path(self.start, current_node)

            directions = [[-1, 0], [-1, -1], [0, -1],
                          [1, 1], [1, 0], [1, -1], [0, 1], [-1, 1]]
            children = []

            for x, y in directions:
                '''
                    Iterate the neighbour of current position and check the availability
                '''
                new_position = (
                    current_node.position[0] + x, current_node.position[1] + y)
                new_node = Node(current_node, new_position)
                if (new_position[0] < 0 or new_position[0] >= gv.DIMENSIONS
                    or new_position[1] < 0 or new_position[1] >= gv.DIMENSIONS
                        or self.gs.board[new_position[0]][new_position[1]] == "wall"
                        or new_node in self.closed):
                    continue
                children.append(new_node)

            for child in children:
                '''
                    for each neighbour check if it is already visited or neighbour has less f value 
                    than the new f value.
                '''

                if child in self.closed:
                    continue

                child.g = heuristic(self.start.position, child.position)
                child.h = heuristic(child.position, self.end.position)
                child.f = child.g + child.h

                is_in_open = False
                for each_node in self.open:
                    if each_node.position == child.position:
                        is_in_open = True
                        if each_node.f < child.f:
                            break
                        elif each_node.f > child.f:
                            each_node.f = child.f
                            each_node.parent = child.parent
                        else:
                            if each_node.h > child.h:
                                each_node.h = child.h
                                each_node.parent = child.parent

                if is_in_open:
                    continue

                if self.gs.board[child.position[0]][child.position[1]] == "dest" and not is_in_open:
                    if child in self.open:
                        pass
                    else:
                        heapq.heappush(self.open, child)
                else:
                    if not is_in_open:
                        heapq.heappush(self.open, child)
                    self.gs.board[child.position[0]
                                  ][child.position[1]] = "vs"

        return None
