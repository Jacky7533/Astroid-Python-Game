# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import the function_hello function
# and the variable_player variable
# into the current file
import constants

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()