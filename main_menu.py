import pygame as p

from translations import translations

p.init()
dark_blue = p.Color(21, 9, 129)
light_gray = p.Color(245, 231, 230)
# label1 = p.font.Font("fonts/TimesNewRoman.ttf", 15)
label2 = p.font.Font("fonts/TimesNewRoman.ttf", 25)


class MainMenu:

    def __init__(self, language):
        self.language = language

        self.welcome_label = label2.render(translations.get("main", {}).get("welcome", {}).get(self.language), True,
                                           "black")
        self.select_students_btn = label2.render(
            translations.get("main", {}).get("select_students", {}).get(self.language), True,
            dark_blue, light_gray)
        self.table_btn = label2.render(translations.get("main", {}).get("table", {}).get(self.language), True,
                                       dark_blue, light_gray)
        self.about_program_btn = label2.render(translations.get("main", {}).get("about_program", {}).get(self.language),
                                               True,
                                               dark_blue, light_gray)
        self.about_author_btn = label2.render(translations.get("main", {}).get("about_author", {}).get(self.language),
                                              True,
                                              dark_blue, light_gray)
        self.quit_btn = label2.render(translations.get("main", {}).get("quit", {}).get(self.language), True, dark_blue,
                                      light_gray)

        self.list_of_properties = [
            self.welcome_label,
            self.select_students_btn,
            self.table_btn,
            self.about_program_btn,
            self.about_author_btn,
            self.quit_btn
        ]
        self.list_of_properties_placement = [
            ((600 - self.welcome_label.get_width()) / 2, 0),
            ((600 - self.select_students_btn.get_width()) / 2, 200),
            ((600 - self.table_btn.get_width()) / 2, 250),
            ((600 - self.about_program_btn.get_width()) / 2, 300),
            ((600 - self.about_author_btn.get_width()) / 2, 350),
            ((600 - self.quit_btn.get_width()) / 2, 400)
        ]
        self.list_of_rectangles = [
            self.select_students_btn.get_rect(topleft=self.list_of_properties_placement[1]),
            self.table_btn.get_rect(topleft=self.list_of_properties_placement[2]),
            self.about_program_btn.get_rect(topleft=self.list_of_properties_placement[3]),
            self.about_author_btn.get_rect(topleft=self.list_of_properties_placement[4]),
            self.quit_btn.get_rect(topleft=self.list_of_properties_placement[5])
        ]
