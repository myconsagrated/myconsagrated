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

        # LEVEL
        self.in_dialogue = False
        self.dialogBox = DialogueBox(self.font)

    def run(self):
        while True:
            bg = pygame.image.load("bg.jpg")
            bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.in_dialogue = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_pos = pygame.mouse.get_pos()
                    if self.dialogBox.is_clicked(m_pos, self.in_dialogue):
                        self.in_dialogue = False

            if self.in_dialogue:
                self.dialogBox.display()

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
