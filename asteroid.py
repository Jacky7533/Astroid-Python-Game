import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # destroy itself
        self.kill()
        # spawn new asteroids, if the radius is less than min radius
        # it means it's the smallest asteroid, therefore it'll just return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate random angle between 20 - 50 degrees
        random_angle = random.uniform(20,50)

        # Rotate the velocity vector to get two new vector
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        # Calculate the new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new astroids at the current possition with new velocity and raidus
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_velocity2 * 1.2