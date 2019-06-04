import pygame


class Character:

    def __init__(self, screen, cell):
        self.screen = screen
        self.character = pygame.image.load('images/character.png').convert_alpha()
        self.character = pygame.transform.scale(self.character, (48, 48))
        self.position = cell

        self.screen.blit(self.character, self.position.a)

    def move_character(self, cell):
        self.position = cell
        self.screen.blit(self.character, self.position.a)
