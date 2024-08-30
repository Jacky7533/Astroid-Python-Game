import pygame

# Base class for game ojects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must ovveride
        pass

    def collisions(self, other):
        # Each CircleShape's position property is a pygame.Vector2. 
        # Use its distance_to method to calculate the distance between the two shapes.

        distance_between_2 = self.position.distance_to(other.position)

        # If distance is less than or equal to r1 + r2, 
        # the circles are colliding. If not, they aren't.
        
        return distance_between_2 <= (self.radius + other.radius)