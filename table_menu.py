import backend


def get_table():
    students = backend.read_students()
    lines = [
        student.__str__() for student in students
    ]
    return lines


def reset_table():
    backend.create_the_list()
    backend.write_last_time_students([])
    get_table()

