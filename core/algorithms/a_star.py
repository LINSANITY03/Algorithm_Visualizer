import heapq
import math


class Node:
    '''
    Represents a A* Node on a position
    '''

    def __init__(self, parent, position) -> None:
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __repr__(self):
        return f'cur:{self.position}-- par:{self.parent}'

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __eq__(self, other) -> bool:
        return self.position == other.position


def heuristic(a, b):
    '''
    calculate the heuristic (Euclidean distance)

    '''
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def reconstruct_path(start_node, end_node):
    '''
    get the path once the A* algorithm is completed
    '''
    total_path = []
    end_node = end_node.parent
    while end_node != start_node:
        total_path.append(end_node.position)
        end_node = end_node.parent
    return total_path[::-1]


class AStar:
    '''
    Determines the shortest path distance between src and destination

    '''

    def __init__(self, source, destination, gs) -> None:
        '''
        Setup the initial parameter for the search algorithms
        '''
        self.gs = gs
        self.open = []
        self.closed = []
        self.start = Node(None, source)
        self.end = Node(None, destination)

    def search(self):
        '''
        Create the logic for a* search returning shortest path if found
        '''
        heapq.heappush(self.open, (self.start.f, self.start))
        while self.open:
            current_node = heapq.heappop(self.open)[1]
            self.closed.append(current_node)

            if current_node == self.end:
                '''

                # add the all previous point with the current i.e end point to form
                # a line indicating the shortest path taken
                '''
                return reconstruct_path(self.start, current_node)

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                          [1, 1], [1, -1], [-1, -1], [-1, 1]]

            children = []

            for x, y in directions:
                '''
                    Iterate the neighbour of current position and check the availability
                '''
                new_position = (
                    current_node.position[0] + x, current_node.position[1] + y)
                new_node = Node(current_node, new_position)

                if (new_position[0] < 0 or new_position[0] > 10
                    or new_position[1] < 0 or new_position[1] > 10
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

                child.g = current_node.g + \
                    heuristic(current_node.position, child.position)
                child.h = heuristic(new_position, self.end.position)
                child.f = child.g + child.h

                for each_node in self.open:
                    if each_node[1].position == child.position:
                        if each_node[0] < child.g:
                            continue

                heapq.heappush(self.open, (child.f, child))

        return None
