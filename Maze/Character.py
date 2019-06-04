import pygame, sys


class Character:

    def __init__(self, screen, cell):
        self.screen = screen
        self.character = pygame.image.load('images/character.png').convert_alpha()
        self.character = pygame.transform.scale(self.character, (48, 48))
        self.position = cell

    def move_character(self, cell, key):
        if not key:
            walls = (0, 2)
        elif key == 1:
            walls = (1, 3)
        elif key == 2:
            walls = (2, 0)
        elif key == 3:
            walls = (3, 1)

        if not self.position.walls[walls[0]] and not cell.walls[walls[1]]:
            self.position = cell
            self.screen.blit(self.character, self.position.a)

            return True
        else:
            return False

    def win(self):
        sys.exit()
