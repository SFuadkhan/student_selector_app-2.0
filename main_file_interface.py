import sys

import pygame as p

import about_author_menu
import about_program_menu
import main_menu
import students_select_menu
import table_menu
from translations import translations

p.init()

languages = [
    'en', 'ru', 'az'
]
language = 'en'
language_count = 0

clock = p.time.Clock()
mouse = p.mouse.get_pressed()
keys = p.key.get_pressed()
screen = p.display.set_mode((600, 500))

dark_blue = p.Color(21, 9, 129)
light_gray = p.Color(245, 231, 230)

p.display.set_caption("Student Selector app")
bdu_image = p.image.load("images/bdu1_blured.jpg").convert_alpha()
bdu_image_not_blured = p.image.load("images/bdu1.jpeg").convert_alpha()

label_newRoman = p.font.Font("fonts/TimesNewRoman.ttf", 20)
bigger_label = p.font.Font("fonts/TimesNewRoman.ttf", 30)

language_btn = bigger_label.render(language, True, dark_blue, light_gray)
arrow_to_left = bigger_label.render("|→|", False, dark_blue, light_gray)
arrow_to_right = bigger_label.render("|←|", False, dark_blue, light_gray)

running = True
is_main_menu = True
is_students_selector_menu = False
is_table_menu = False
is_about_program_menu = False
is_about_author_menu = False
is_waiting_students = False
is_blured_once = True

blur_timer = p.USEREVENT + 1
p.time.set_timer(blur_timer, 1000)

window_properties = []
window_properties_placement = []
window_properties_rectangles = []
some_lines = []

how_many_students = 0
table = table_menu.get_table()
reset_table = label_newRoman.render(translations.get("table_menu", {}).get("reset_table", {}).get(language),
                                    True, dark_blue, light_gray)
dividable = False
page = 1
pages = 0

last_time_answered_students = None


def blit_all_properties(properties, properties_placement):
    i = 0
    for unit in properties:
        screen.blit(unit, properties_placement[i])
        i += 1


def blit_text(text, n, x, y):
    space = 0
    if is_table_menu and dividable:
        for i in text[page - 1]:
            screen.blit(i, (x, y + space))
            space += n
    else:
        for i in text:
            screen.blit(i, (x, y + space))
            space += n


def format_line_surfaces(lines):
    global dividable, pages
    line_surfaces = []
    pages = len(lines) // 20
    if len(lines) > 20:
        for i in range(0, len(lines), 20):
            section_lines = lines[i:i + 20]
            section_surfaces = [label_newRoman.render(line, True, dark_blue, light_gray) for line in section_lines]
            line_surfaces.append(section_surfaces)
        dividable = True
    else:
        line_surfaces = [label_newRoman.render(line, True, dark_blue, light_gray) for line in lines]

    return line_surfaces


while running:
    if is_main_menu and is_blured_once:
        screen.blit(bdu_image_not_blured, ((screen.get_width() - bdu_image.get_width()) / 2,
                                           (screen.get_height() - bdu_image.get_height()) / 2))

    else:
        screen.blit(bdu_image, ((screen.get_width() - bdu_image.get_width()) / 2,
                                (screen.get_height() - bdu_image.get_height()) / 2))

        if is_main_menu:
            main_class = main_menu.MainMenu(language)
            window_properties = main_class.list_of_properties
            window_properties_placement = main_class.list_of_properties_placement
            window_properties_rectangles = main_class.list_of_rectangles
            blit_all_properties(window_properties, window_properties_placement)
            screen.blit(language_btn, (500, 400))

        elif is_table_menu:
            blit_text(format_line_surfaces(table), 23, 100, 23)
            screen.blit(about_author_menu.AboutAuthor(language).main_menu_btn, (400, 400))
            screen.blit(arrow_to_right, (250, 400))
            screen.blit(arrow_to_left, (300, 400))
            screen.blit(reset_table, (400, 250))

        elif is_about_author_menu:
            screen.blit(about_author_menu.lines, ((600 - about_author_menu.lines.get_width()) / 2, 200))
            screen.blit(about_author_menu.AboutAuthor(language).main_menu_btn, (400, 400))

        elif is_about_program_menu:
            blit_text(about_program_menu.line_surfaces, 50, 100, 30)
            screen.blit(about_program_menu.AboutProq(language).main_menu_btn, (400, 400))

        elif is_students_selector_menu:
            students_select = students_select_menu.StudentsSelector(language)
            if is_waiting_students:
                screen.blit(students_select.how_many_students, ((screen.get_width() - students_select.
                                                                 how_many_students.get_width()) / 2, 50))
                screen.blit(students_select.input_number,
                            ((screen.get_width() - students_select.input_number.get_width()) / 2, 150))
                screen.blit(students_select.last_time_answered, (70, 220))
                blit_text(format_line_surfaces(last_time_answered_students), 20, 100, 250)
            else:
                blit_text(format_line_surfaces(some_lines), 20, 100, 30)
            screen.blit(students_select.main_menu_btn, (400, 400))

    for event in p.event.get():
        if event.type == blur_timer:
            is_blured_once = False
            blur_timer = None
        if is_table_menu or is_students_selector_menu or is_about_author_menu or is_about_program_menu:
            if is_students_selector_menu and is_waiting_students:
                if event.type == p.KEYDOWN:
                    if event.key == p.K_1:
                        how_many_students = 1
                        some_lines = students_select_menu.get_students(1)
                        is_waiting_students = False
                    elif event.key == p.K_2:
                        how_many_students = 2
                        some_lines = students_select_menu.get_students(2)
                        is_waiting_students = False
                    elif event.key == p.K_3:
                        how_many_students = 3
                        some_lines = students_select_menu.get_students(3)
                        is_waiting_students = False
                    elif event.key == p.K_4:
                        how_many_students = 4
                        some_lines = students_select_menu.get_students(4)
                        is_waiting_students = False
                    elif event.key == p.K_5:
                        how_many_students = 5
                        some_lines = students_select_menu.get_students(5)
                        is_waiting_students = False
                    elif event.key == p.K_6:
                        how_many_students = 6
                        some_lines = students_select_menu.get_students(6)
                        is_waiting_students = False
                    elif event.key == p.K_7:
                        how_many_students = 7
                        some_lines = students_select_menu.get_students(7)
                        is_waiting_students = False
                    elif event.key == p.K_8:
                        how_many_students = 8
                        some_lines = students_select_menu.get_students(8)
                        is_waiting_students = False
                    elif event.key == p.K_9:
                        how_many_students = 9
                        some_lines = students_select_menu.get_students(9)
                        is_waiting_students = False

            if event.type == p.MOUSEBUTTONDOWN and any(p.mouse.get_pressed()):
                if reset_table.get_rect(topleft=(400, 250)).collidepoint(p.mouse.get_pos()):
                    table_menu.reset_table()
                    table = table_menu.get_table()
                if arrow_to_right.get_rect(topleft=(250, 400)).collidepoint(p.mouse.get_pos()) and dividable:
                    page = (page - 1) % pages
                if arrow_to_left.get_rect(topleft=(300, 400)).collidepoint(p.mouse.get_pos()) and dividable:
                    page = (page + 1) % pages

                if about_author_menu.AboutAuthor(language).main_menu_btn.get_rect(topleft=(400, 400)).collidepoint(
                        p.mouse.get_pos()):
                    print("Button clicked!")
                    is_main_menu = True
                    is_students_selector_menu = False
                    is_about_program_menu = False
                    is_about_author_menu = False
                    is_table_menu = False

        if is_main_menu:
            if event.type == p.MOUSEBUTTONDOWN and any(p.mouse.get_pressed()):
                for index, item in enumerate(window_properties_rectangles):
                    if item.collidepoint(p.mouse.get_pos()):
                        print("Button clicked:", index)
                        window_properties = []
                        window_properties_rectangles = []
                        window_properties_placement = []
                        is_main_menu = False
                        if index == 0:
                            is_students_selector_menu = True
                            is_waiting_students = True
                            last_time_answered_students = students_select_menu.get_last_time_answered()
                        elif index == 1:
                            table = table_menu.get_table()
                            reset_table = label_newRoman.render(
                                translations.get("table_menu", {}).get("reset_table", {})
                                .get(language), True, dark_blue, light_gray)
                            is_table_menu = True
                        elif index == 2:
                            is_about_program_menu = True
                        elif index == 3:
                            is_about_author_menu = True
                        elif index == 4:
                            running = False
                            p.quit()
                            sys.exit(0)
                    if language_btn.get_rect(topleft=(500, 400)).collidepoint(p.mouse.get_pos()):
                        language_count += 1
                        language = languages[language_count % len(languages)]
                        language_btn = bigger_label.render(language, True, dark_blue, light_gray)

        if event.type == p.QUIT or (event.type == p.KEYUP and event.key == p.K_ESCAPE):
            running = False
            p.quit()
            sys.exit(0)
    clock.tick(30)
    p.display.update()
