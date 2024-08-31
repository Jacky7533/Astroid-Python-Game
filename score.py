import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize sprite with containers
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.color = "white"
        self.position = (10, 10)
        # Initialize image and rect
        self.update()

    def increase(self, amount):
        self.score += amount
        self.update()

    def reset(self):
        self.score = 0
        self.update()

    def update(self, dt=None):
        # Update the image and rect attributes when the score changes
        self.image = self.font.render(f"Score: {self.score}", True, self.color)
        self.rect = self.image.get_rect(topleft=self.position)

    def draw(self, screen):
        # Draw the score image onto the screen
        screen.blit(self.image, self.rect)