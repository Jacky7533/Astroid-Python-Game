# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import the function_hello function
# and the variable_player variable
# into the current file
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_time = pygame.time.Clock()
    dt = 0
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color=(0,0,0))
        pygame.display.flip()
        game_time.tick(60)
        dt = game_time.tick()/1000

if __name__ == "__main__":
    main()