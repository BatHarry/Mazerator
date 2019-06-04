import sys, pygame
from Maze import Maze, Character

pygame.init()

# size = width, height = 1010, 1010
size = width, height = 505, 505
speed = [2, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

maze = Maze(10, screen)
maze.generate_maze()
maze.draw()
character = Character(screen, maze.maze[0][0])
clock = pygame.time.Clock()
x = 0
y = 0

x_change, y_change = 0, 0

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x_change == 0:
                    x_change = -1
            elif event.key == pygame.K_RIGHT:
                if x_change == 0:
                    x_change = 1
            elif event.key == pygame.K_DOWN:
                if x_change == 0:
                    y_change = 1
            elif event.key == pygame.K_UP:
                y_change = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change, y_change = 0, 0

    x += x_change
    y += y_change
    character.move_character(maze.maze[y][x])

    pygame.display.update()
    clock.tick(60)
