import pygame, sys

from settings import *

# from level import Level
from dialogues.hello import initial_dialogue
from pygame.locals import *


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Psycodelic Punk")
        self.clock = pygame.time.Clock()
        pygame.display.set_icon(pygame.image.load("assets/cat_pixel_icon.png"))

        # self.level = Level()

    def run(self):
        font = pygame.font.SysFont(None, 48)
        img = font.render(initial_dialogue[0], True, (255, 0, 0))
        rect = img.get_rect()
        rect.topleft = (20, 20)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")

            if event.type == KEYDOWN:
                initial_dialogue.pop(0)

            img = font.render(initial_dialogue[0], True, (255, 0, 0))
            rect.size = img.get_size()

            self.screen.blit(img, rect)

            # self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
