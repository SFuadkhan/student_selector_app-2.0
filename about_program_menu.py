import pygame as p

from translations import translations

p.init()
dark_blue = p.Color(21, 9, 129)
light_gray = p.Color(245, 231, 230)
# label1 = p.font.Font("fonts/KodeMono-Bold.ttf", 15)
label2 = p.font.Font("fonts/TimesNewRoman.ttf", 20)
label = p.font.Font("fonts/TimesNewRoman.ttf", 15)
lines = [
    "-This is smt for what i didn't sleep",
    "-Was it worth it? ",
    "-Will someone care?"
]

# Render each line onto a surface
line_surfaces = [label2.render(line, True, p.Color(dark_blue),
                               p.Color(light_gray)) for line in lines]


class AboutProq:
    def __init__(self, language):
        self.language = language
        self.main_menu_btn = label2.render(translations.get("about_program", {}).get("main_menu_btn", {})
                                           .get(language), True, dark_blue, light_gray)
