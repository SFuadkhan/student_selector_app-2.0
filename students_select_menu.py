import pygame as p

import backend
from translations import translations

dark_blue = p.Color(21, 9, 129)
light_gray = p.Color(245, 231, 230)
label1 = p.font.Font("fonts/TimesNewRoman.ttf", 15)
label2 = p.font.Font("fonts/TimesNewRoman.ttf", 20)
bigger_label = p.font.Font("fonts/TimesNewRoman.ttf", 30)


class StudentsSelector:
    def __init__(self, language):
        self.language = language
        self.main_menu_btn = label2.render(translations.get('selector_menu', {}).get("main_menu_btn", {}).get(language),
                                           True, dark_blue, light_gray)
        self.how_many_students = label2.render(translations.get("how_many_students_should_answer", {}).get(language),
                                               True, dark_blue, light_gray)
        self.last_time_answered = label2.render(translations.get("selector_menu", {}).get("last_time_answered", {})
                                                .get(language), True, dark_blue, light_gray)
        self.input_number = bigger_label.render(translations.get("selector_menu", {}).get("input_number", {})
                                                .get(language), True, dark_blue, light_gray)


def get_last_time_answered():
    students = backend.read_last_time_students()
    lines = [str(student) for student in students]
    return lines


def get_students(n):
    students = backend.main(n)
    lines = [str(student) for student in students]
    return lines
