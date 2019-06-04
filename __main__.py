import sys, pygame, time
from Maze import Maze, Character

pygame.init()

size = width, height = 1010, 1010
# size = width, height = 505, 505
black = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

maze_size = 10
maze = Maze(maze_size, screen)
maze.generate_maze()

character = Character(screen, maze.maze[0][0])
muriel = pygame.image.load('images/muriel.png').convert_alpha()
muriel = pygame.transform.scale(muriel, (38, 48))

x = 0
y = 0

x_change, y_change = 0, 0
flag = False
start_time = time.time()

while True:
    key = None

    screen.fill(black)
    maze.draw()
    screen.blit(character.character, maze.maze[y][x].a)
    screen.blit(muriel, maze.maze[maze_size - 1][maze_size - 1].a)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x_change = -1
            key = 3
        elif keys[pygame.K_RIGHT]:
            x_change = 1
            key = 1
        elif keys[pygame.K_DOWN]:
            y_change = 1
            key = 2
        elif keys[pygame.K_UP]:
            y_change = -1
            key = 0

    if ((x + x_change >= 0) and (x + x_change < maze_size)) and ((y + y_change >= 0) and (y + y_change < maze_size)):
        if character.move_character(maze.maze[y + y_change][x + x_change], key):
            x += x_change
            y += y_change
            if x == maze_size - 1 and y == maze_size - 1:
                flag = True

    if flag:
        screen.blit(pygame.image.load("images/finish.jpg"), ((width // 2) - 430 // 2, (height // 2) - 370 // 2))
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("Your time %s sec" % (round(time.time() - start_time, 2)), False, (255, 0, 0))
        screen.blit(textsurface, (20, 20))
        pygame.display.update()
        time.sleep(3)
        sys.exit()

    x_change, y_change = 0, 0

    pygame.display.update()
    clock.tick(60)
