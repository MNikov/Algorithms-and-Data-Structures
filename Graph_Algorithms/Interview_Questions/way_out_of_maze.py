# Your task is to design an algorithm with breadth-first search that is able to find
# the shortest path from a given source to a given destination. The maze is represented by a two-dimensional list.
# [
#    [S, 1, 1, 1, 1],
#    [0, 1, 1, 1, 1],
#    [0, 0, 0, 0, 1],
#    [1, 0, 1, 1, 1],
#    [0, 0, 0, 1, D]
# ]
# The (0,0) is the source and (4,4) is the destination.
# 0 represents walls or obstacles and 1 is the valid cells we can include in the solution.
from collections import deque


class MazeSolver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        self.visited_cells = [[False for _ in range(len(self.matrix))] for _ in range(len(self.matrix))]
        self.min_distance = float('inf')

    def is_valid(self, row, col):
        if row < 0 or row >= len(self.matrix):
            return False

        if col < 0 or col >= len(self.matrix):
            return False

        if self.matrix[row][col] == 0:
            return False

        if self.visited_cells[row][col]:
            return False

        return True

    def search(self, r, c, end_r, end_c):
        self.visited_cells[r][c] = True
        queue = deque()
        queue.append((r, c, 0))

        while queue:
            curr_r, curr_c, dist = queue.popleft()

            if curr_r == end_r and curr_c == end_c:
                self.min_distance = dist
                break

            for move in range(4):
                next_x = curr_r + self.move_x[move]
                next_y = curr_c + self.move_y[move]

                if self.is_valid(next_x, next_y):
                    self.visited_cells[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):
        if self.min_distance != float('inf'):
            print(f'The shortest way out is {self.min_distance}.')
        else:
            print('There is no way out of the maze.')


m = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]
maze_solver = MazeSolver(m)
maze_solver.search(0, 0, 4, 4)
maze_solver.show_result()
