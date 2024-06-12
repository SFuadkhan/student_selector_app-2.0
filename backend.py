import os
import random
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
backup_file_path = os.path.join(current_dir, 'backup.txt')
write_file_path = os.path.join(current_dir, 'file.txt')
last_selected = os.path.join(current_dir, 'last_time_selected.txt')


class Student:
    def __init__(self, student_id, name, answers):
        self.id = student_id
        self.name = name
        self.answers = answers

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_answers(self):
        return self.answers

    def set_answers(self, answers):
        self.answers = answers

    def __str__(self):
        return f"|{str(self.id)} | {self.name} | {str(self.answers)}|"


def create_the_list():
    try:
        with open(backup_file_path, 'r') as reader:
            txt = reader.readlines()
    except FileNotFoundError:
        return "Backup file not found."
    with open(write_file_path, 'w') as writer:
        for j, line in enumerate(txt, 1):
            writer.write(f"{j} {line}")
    return "List has been rewritten."


def pick_students(students, n):
    names = set()
    students_taken = []
    min_answers = min([student.get_answers() for student in students])
    students_left = [student for student in students if student.get_answers() == min_answers]
    students_removed = [student for student in students if student.get_answers() == min_answers + 1]

    size_of_left = len(students_left)
    if size_of_left == n:
        students_taken = students_left
        names = set(student.get_name() for student in students_left)
    elif size_of_left > n:
        random.shuffle(students_left)
        names = set([student.get_name() for student in students_left[:n]])
        students_taken = students_left[:n]
    else:
        n -= size_of_left
        random.shuffle(students_removed)
        students_taken = students_removed[:n]

        for student in students_left:
            student.set_answers(student.get_answers() + 1)
            students_taken.append(student.__str__())
        # students_taken.append([student.__str__() for student in students_left])

        names = set([student.get_name() for student in students_removed[:n]])
        names.update([student.get_name() for student in students_left])

    return students_taken, names


def read_students():
    students = []
    with open(write_file_path, 'r') as file:
        # Read student data from the file and create Student objects
        for line in file:
            temp = line.split(" ")
            students.append(Student(int(temp[0]), temp[1], int(temp[2])))
    return students


def write_students(students):
    with open(write_file_path, 'w') as file:
        # Write the updated student data back to the file
        for i, student in enumerate(students, 1):
            file.write(f"{i} {student.get_name()} {student.get_answers()}\n")


def get_last_time_answered():
    return read_last_time_students()


def read_last_time_students():
    students = []
    with open(last_selected, 'r') as file:
        # Read student data from the file and create Student objects
        for line in file:
            temp = line.split(" ")
            students.append(f"{temp[0]} {temp[1]} {temp[2]}")
    return students


def write_last_time_students(students):
    with open(last_selected, 'w') as file:
        # Write the updated student data back to the file
        for i, student in enumerate(students, 1):
            file.write(f"{students[i - 1]}\n")


def main(n):
    global FILEPATH
    try:
        if len(sys.argv) > 1:
            FILEPATH = sys.argv[1]
    except IndexError:
        pass
    # create_the_list()
    students = read_students()

    students_taken, result_set = pick_students(students, n)  # Pick students randomly

    # Update the number of times each student has been selected
    for student in students:
        if student.get_name() in result_set:
            student.set_answers(student.get_answers() + 1)

    students.sort(key=lambda x: x.get_id())  # Sort the students by ID

    write_students(students)
    students_taken = [student.__str__() for student in students_taken]
    write_last_time_students(students_taken)
    return students_taken

# if __name__ == "__main__":
#     print(main(15))
