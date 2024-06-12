import pygame as p

from translations import translations
p.init()
dark_blue = p.Color(21, 9, 129)
light_gray = p.Color(245, 231, 230)
# label1 = p.font.Font("fonts/KodeMono-Bold.ttf", 15)
label2 = p.font.Font("fonts/TimesNewRoman.ttf", 20)
lines = label2.render("SOME THE WAY TOOO IDLE MAN", True, p.Color(dark_blue),
                      p.Color(light_gray))


class AboutAuthor:
    def __init__(self, language):
        self.language = language
        self.main_menu_btn = label2.render(translations.get("about_author", {}).get("main_menu_btn", {})
                                           .get(language), True, dark_blue, light_gray)
