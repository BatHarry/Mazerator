from .Cell import Cell
import pygame, random


class Maze:

    def __init__(self, size, screen):
        self.maze = []
        self.size = size
        self.screen = screen
        self.backlog = [(0, 0)]
        pos_x, pos_y = 0, 0
        for x in range(self.size ):
            self.maze.append([])
            for y in range(self.size):
                self.maze[x].append(Cell(pos_x, pos_y))
                pos_x += 50
            pos_y += 50
            pos_x = 0
        self.maze[0][0].visited = True
        pygame.draw.rect(screen, (150,120,140), pygame.Rect((2, 2), (48,48)))

    def draw(self):
        for row in self.maze:
            for cell in row:
                if cell.walls[0]:
                    pygame.draw.line(self.screen, cell.color, cell.a, cell.b)
                if cell.walls[1]:
                    pygame.draw.line(self.screen, cell.color, cell.b, cell.c)
                if cell.walls[2]:
                    pygame.draw.line(self.screen, cell.color, cell.c, cell.d)
                if cell.walls[3]:
                    pygame.draw.line(self.screen, cell.color, cell.d, cell.a)

    def generate_maze(self, x=0, y=0, count=0):
        neighbours = []
        options = []

        if x + 1 < self.size:
            neighbours.append((x + 1, y))
        if y + 1 < self.size:
            neighbours.append((x, y + 1))
        if y - 1 >= 0:
            neighbours.append((x, y - 1))
        if x - 1 >= 0:
            neighbours.append((x - 1, y))

        for neighbour in neighbours:
            if not self.maze[neighbour[0]][neighbour[1]].visited:
                options.append(neighbour)

        if len(options):
            rand_int = len(options) - 1
            # print(rand_int)
            move = options[random.randint(0, rand_int)]
            next_cell = self.maze[move[0]][move[1]]
            next_cell.visited = True

            # Remove walls to current and neighbour
            self.remove_walls((x, y), (move[0], move[1]))

            # print(move)
            color = (random.randint(0, 35), random.randint(0, 35), random.randint(0, 55))
            # color = (10, 30, 50)
            pygame.draw.rect(self.screen, color, pygame.Rect(next_cell.a, (48, 48)))

            self.backlog.append((move[0], move[1]))
            self.generate_maze(move[0], move[1], count)
        else:
            if len(self.backlog):
                move = self.backlog.pop()
                # print("BACK")
                self.generate_maze(move[0], move[1])
            else:
                return True

    def remove_walls(self, current, move):
        difference_x = current[0] - move[0]
        difference_y = current[1] - move[1]

        current_cell = self.maze[current[1]][current[0]]
        next_cell = self.maze[move[1]][move[0]]

        # DOWN
        if difference_y == -1:
            current_cell.walls[2] = 0
            next_cell.walls[0] = 0
            # print("HERE")

        # RIGHT
        if difference_x == 1:
            current_cell.walls[3] = 0
            next_cell.walls[1] = 0

        # DOWN
        if difference_y == 1:
            current_cell.walls[0] = 0
            next_cell.walls[2] = 0

        # LEFT
        if difference_x == -1:
            current_cell.walls[1] = 0
            next_cell.walls[3] = 0
