import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)

        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.timer = 0 # Initial timer

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Override the draw method of CircleShape
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),width=2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        #front of the ship
        front_ship = self.triangle()[0]

        # Calculate the offset vector (10 pixel away from the tip)
        offset_distance = 10
        offset = pygame.Vector2(0, offset_distance).rotate(self.rotation)

        # Apply the offset to the tip position
        spawn_position = front_ship + offset

        # draw the bullet
        bullet = Shot(spawn_position.x, spawn_position.y)

        # adding the velocity
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED
        
        # set timer to shoot 0.3
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-(dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-(dt))
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
            else:
                self.timer -= dt
            