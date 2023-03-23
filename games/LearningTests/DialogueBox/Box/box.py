base_display_coordiantes = None
base_letter_coordiantes = None
base_shader_width = 1
border_width = 10
# initial_letter_coordinate =


from settings import *


# How does PyGame handles the memory of an closed dialogue_box? Does it need to check for it EVERY TIME?
# might be. So we need an abstraction of our own or see if pygame already as an optimal one.
class DialogueBox:
    def __init__(self, screen, text: str, **kwargs):
        # List: 4: x_coord, y_coord, x_size, y_size
        self.display_coordiantes = kwargs.get(
            "base_display_coordiantes", self.get_base_display_coordinates()
        )
        self.outer_shader_width = kwargs.get("outer_shader_width", base_shader_width)
        self.border_width = kwargs.get("border_width", border_width)
        self.initial_letter_coordinate = kwargs.get(
            "base_letter_coordiantes", base_letter_coordiantes
        )
        self.text = text

    def get_base_display_coordinates(self):
        y_size = SCREEN_HEIGHT * 0.40
        x_size = SCREEN_WIDTH * 0.90
        x_coord = SCREEN_WIDTH * 0.05
        y_coord = SCREEN_HEIGHT - (SCREEN_HEIGHT * 0.05) - y_size

        rect_coords = [x_coord, y_coord, x_size, y_size]

        return rect_coords


    def get_shader_display_coordinates(self):
        pass
