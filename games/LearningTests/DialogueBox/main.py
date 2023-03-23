import pygame, sys

from settings import *
from pygame.locals import *
from Box.box import DialogueBox


# C1 = (75, 150, 150)
# C2 = (150, 150, 150)

y_size = SCREEN_HEIGHT * 0.40
x_size = SCREEN_WIDTH
x_coord = 0
y_coord = SCREEN_HEIGHT - y_size

# rect_coords = [x_coord, y_coord, x_size, y_size]
# print(rect_coords)

# rect = Rect(*rect_coords)


# percentage_size = 0.10
# rect2_coords = [
#     x_coord + (SCREEN_HEIGHT * (percentage_size)),
#     y_coord + (SCREEN_WIDTH * (percentage_size)),
#     x_size * 0.80,
#     y_size * 0.80,
# ]
# rect2 = Rect(*rect2_coords)

# print(rect2_coords)

color_text = (96, 52, 80, 255)

print(SCREEN_WIDTH / 80, SCREEN_HEIGHT / 80)
print((SCREEN_WIDTH, SCREEN_HEIGHT))


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Psycodelic Punk")
        self.clock = pygame.time.Clock()
        pygame.display.set_icon(pygame.image.load("assets/cat_pixel_icon.png"))
        self.font = pygame.font.Font("assets/Pixeltype.ttf", 48)

        # self.level = Level()

    def run(self):
        while True:
            bg = pygame.image.load("bg.jpg")
            bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # box = DialogueBox("SAMPLE TEXT")
            text = self.font.render("Hello World!", False, color_text)
            text_rect = text.get_rect()
            # rect.size = img.get_size()
            img = pygame.image.load("assets/Box2.png").convert()
            img = pygame.transform.scale(img, (x_size, y_size))
            self.screen.blit(img, (x_coord, y_coord))
            self.screen.blit(text, (x_coord + 35, y_coord + 30))

            # pygame.draw.rect(self.screen, C1, rect)
            # pygame.draw.rect(self.screen, C2, rect2)

            # self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

    # should this me somewhere else?

    def display_dialogue_box():
        pass


if __name__ == "__main__":
    game = Game()
    game.run()
