# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
# import the function_hello function
# and the variable_player variable
# into the current file
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2
    game_time = pygame.time.Clock()



    # creating 2 groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # creating a group that contains all asteroids
    asteroids = pygame.sprite.Group()

    # add the player to both groups into a container
    Player.containers = (updatable, drawable)
    # add the asteroid into a container
    Asteroid.containers = (asteroids, updatable, drawable)
    # adding a asteroidfield container
    AsteroidField.containers = (updatable)

    # Create the player and asteroid field instances
    player = Player(center_x,center_y)
    asteroid_field = AsteroidField()

    dt = 0

    # GameLoop Start
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #limit fps to 60 
        dt = game_time.tick(60)/1000

        # update all objects in updatable group
        for update in updatable:
            update.update(dt)

        # Checks for collision
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game Over!")
                pygame.quit()
                sys.exit()    
    
        # Clear the screen
        screen.fill("black")

        # draw all objects in the drawable group
        for draw in drawable:
            draw.draw(screen)

        # Update the display
        pygame.display.flip()
         

if __name__ == "__main__":
    main()