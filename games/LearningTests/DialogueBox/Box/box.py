base_display_coordiantes = None
base_letter_coordiantes = None
base_shader_width = 1
border_width = 10

from settings import *
import pygame
from pygame.locals import *

from pygame.font import Font


# initial_letter_coordinate =
color_text = (96, 52, 80, 255)
y_size = SCREEN_HEIGHT * 0.40
x_size = SCREEN_WIDTH
x_coord = 0
y_coord = SCREEN_HEIGHT - y_size


def display_lines_that_fit(
    text, font: Font, box_surface: pygame.surface.Surface, color_text, display_surface
):
    y = box_surface.top + 30
    # print(y)
    fontHeight = font.get_height()
    # print(f"fontHeight: {fontHeight}")

    text_list = []

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > box_surface.bottom - 30:
            # print("[0] - Too large", text)
            return text[i:]

        # determine maximum width of line
        while font.size(text[:i])[0] < box_surface.width - 50 and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        image = font.render(text[:i], False, color_text)
        text_list.append(text[:i])

        display_surface.blit(image, (box_surface.left + 50, y))
        y += fontHeight - 2

        # remove the text we just blitted
        text = text[i:]

    # print(text_list)


# How does PyGame handles the memory of an closed dialogue_box? Does it need to check for it EVERY TIME?
# might be. So we need an abstraction of our own or see if pygame already as an optimal one.
class DialogueBox:
    def __init__(self, font: Font, **kwargs):
        # List: 4: x_coord, y_coord, x_size, y_size
        # self.display_coordiantes = kwargs.get(
        #     "base_display_coordiantes", self.get_base_display_coordinates()
        # )
        # self.outer_shader_width = kwargs.get("outer_shader_width", base_shader_width)
        # self.border_width = kwargs.get("border_width", border_width)
        # self.initial_letter_coordinate = kwargs.get(
        #     "base_letter_coordiantes", base_letter_coordiantes
        # )
        # self.text = text

        self.display_surface = pygame.display.get_surface()

        text_input = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla a elit cursus, fringilla felis in, suscipit leo. Etiam in laoreet velit. Curabitur sed ligula maximus, suscipit eros in, posuere quam. Aenean interdum non risus quis eleifend. Morbi non felis in dui faucibus pellentesque. Vivamus vel faucibus arcu. Aenean sed mi accumsan, feugiat nisl eu, interdum erat. Maecenas augue leo, consectetur ac scelerisque non, egestas eu dui. Vestibulum eu tellus arcu. Aenean orci urna, vestibulum non tristique at, ornare a metus. Aenean porta lorem quis posuere commodo. Nunc euismod arcu at urna pellentesque, a tincidunt nisi ultricies.
            enim. Quisque egestas turpis nec libero aliquet, nec semper neque vestibulum. Nullam in volutpat ipsum. Mauris maximus, enim ut sagittis accumsan, orci lectus egestas velit, a pellentesque turpis sapien vitae est. Morbi euismod pharetra orci mattis bibendum. Phasellus et aliquam urna. Suspendisse vitae nunc turpis.
            Phasellus auctor mauris et sapien molestie tristique. Proin vehicula accumsan sapien. Nulla consequat rutrum eros, id pulvinar odio. Ut a vestibulum 
            
        """

        # enim. Quisque egestas turpis nec libero aliquet, nec semper neque vestibulum. Nullam in volutpat ipsum. Mauris maximus, enim ut sagittis accumsan, orci lectus egestas velit, a pellentesque turpis sapien vitae est. Morbi euismod pharetra orci mattis bibendum. Phasellus et aliquam urna. Suspendisse vitae nunc turpis.

        # text_input = wrap_multi_line(text_input, font, (x_coord - 70))
        # print(text_input)
        print(font.get_height())
        self.font = font

        # self.text = font.render(text_input, False, color_text)
        self.text = text_input
        self.img_surface = pygame.image.load("assets/Box2.png").convert_alpha()
        self.img_surface = pygame.transform.scale(self.img_surface, (x_size, y_size))
        self.img_rect = self.img_surface.get_rect(topleft=(x_coord, y_coord))

        self.next_close_surf = Rect(SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50, 10, 10)

        # test(text_input, font, self.img.get_rect(), color_text, self.display_surface)

    def display(self):
        self.display_surface.blit(self.img_surface, self.img_rect)
        # self.display_surface.blit(self.text, (x_coord + 35, y_coord + 30))
        # print(self.img_rect)

        self.text_not_printed = display_lines_that_fit(
            self.text, self.font, self.img_rect, color_text, self.display_surface
        )

        # draws the "next page/done button"
        pygame.draw.rect(self.display_surface, (75, 150, 150), self.next_close_surf)

    def is_clicked(self, m_pos, is_diplayed):
        if self.next_close_surf.collidepoint(m_pos) and is_diplayed:
            print("clicked")
            if self.text_not_printed is not None:
                self.text = self.text_not_printed
                return False
            return True
        # if self.next_close_surf.
        else:
            return False

    def get_new_page_or_close(self):
        pass

    def get_base_display_coordinates(self):
        y_size = SCREEN_HEIGHT * 0.40
        x_size = SCREEN_WIDTH * 0.90
        x_coord = SCREEN_WIDTH * 0.05
        y_coord = SCREEN_HEIGHT - (SCREEN_HEIGHT * 0.05) - y_size

        rect_coords = [x_coord, y_coord, x_size, y_size]

        return rect_coords

    def get_shader_display_coordinates(self):
        pass
