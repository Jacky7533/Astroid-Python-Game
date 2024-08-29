import pygame

# Base class for game ojects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, raidus):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.raidus = raidus

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must ovveride
        pass