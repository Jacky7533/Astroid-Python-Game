import pygame
from constants import *

class Life(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize sprite with containers
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.life = 3
        self.font = pygame.font.Font(None, 36)
        self.color = "white"
        self.position = (SCREEN_WIDTH - 10, 10)
        # Initialize image and rect
        self.update()

    def decrease(self, amount):
        self.life -= amount
        self.update()

    def reset(self):
        self.life = 3
        self.update()

    def update(self, dt=None):
        # Update the image and rect attributes when the score changes
        self.image = self.font.render(f"Lives: {self.life}", True, self.color)
        self.rect = self.image.get_rect(topright=self.position)

    def draw(self, screen):
        # Draw the score image onto the screen
        screen.blit(self.image, self.rect)