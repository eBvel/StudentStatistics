def request_menu_item():
    while True:
        try:
            menu_item = int(input("\nВведите пункт меню: "))
            if menu_item < 1 or menu_item > 5:
                print("Ошибка: указанный пункт меню отсутствует!")
            else:
                return menu_item
        except ValueError:
            print("Ошибка: введено некорректное значение!")


def request_student_name():
    while True:
        name = input("Введите имя студента: ")
        if not validate_student_name(name):
            print("Ошибка: имя заполнено некорректно!")
        else:
            return name


def validate_student_name(name):
    if len(name) < 2: return False

    allowed_characters = set("abcdefghijklmnopqrstuvwxyz"
                             "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for letter in name:
        if letter not in allowed_characters:
            return False
    return True


def request_student_grades():
    print("\nВведите оценки студента. Допустимые значения от 0 до 100.\n"
          "Чтобы завершить ввод оценок, введите значение '-1'.")
    grades = []
    while True:
        try:
            grade = int(input("Введите оценку: "))
            if grade < -1 or grade > 100:
                print("Ошибка: введено значение за пределами допустимого"
                      " диапозона!")
            elif grade == -1:
                return grades
            else:
                grades.append(grade)
        except ValueError:
            print("Ошибка: введено некорректное значение!")


# 2-ое задание, часть 1
def calculate_average(grades):
    try:
        return round(sum(grades) / len(grades), 2)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return 0


# 5-ое и 7-ое задание
def calculate_common_average(grades):
    average_grade_by_student = [calculate_average(i) for i in grades]
    return calculate_average(average_grade_by_student)


# 3-ие задние
def determine_status(average_grade):
    return "Успешный" if average_grade >= 75 else "Отстающий"


def get_worst_student():
    if not students:
        return None

    worst_student = students[0]
    for student in students[1:]:
        worst_student_average_grade = (calculate_average
                                       (worst_student['grades']))
        current_student_average_grade = calculate_average(student['grades'])
        if worst_student_average_grade > current_student_average_grade:
            worst_student = student
    return worst_student


# 2-ое задание, часть 2
def get_students_data():
    for student in students:
        yield student_information(student)


# 4-ое задание
def student_information(student):
    average_grade = calculate_average(student['grades'])
    status = determine_status(average_grade)
    return (f"\nСтудент: {student['name']}\nСредний балл: {average_grade}, "
            f"\nСтатус: {status}")


def display_list_of_student():
    if students:
        print("\n---СПИСОК СТУДЕНТОВ---")
        for student in get_students_data():
            print(student)
    else:
        print("\n---СПИСОК СТУДЕНТОВ ПУСТ!---")


def display_common_average_grade():
    grades_of_students = [student['grades'] for student in students]
    common_average_grade = calculate_common_average(grades_of_students)
    print(f"\nОБЩИЙ СРЕДНИЙ БАЛЛ: {common_average_grade}")


# 6-ое задание, часть 2
def add_student():
    print("\nДОБАВЛЕНИЕ СТУДЕНТА:")
    name = request_student_name()
    grades = request_student_grades()
    students.append({'name': name, 'grades': grades})
    print(f"Студент: {name}\nОценки: {grades}\n---Добавлен в базу!")


# 6-ое задание, часть 1
def delete_worst_student():
    worst_student = get_worst_student()
    if worst_student is None:
        print("\n---СПИСОК СТУДЕНТОВ ПУСТ!---")
    else:
        print(f"\nУДАЛЕНИЕ СТУДЕНТА С САМЫМ НИЗКИМ РЕЙТИНГОМ:"
              f"\n{student_information(worst_student)}"
              f"\n---Удален из базы---!")
        students.remove(worst_student)


def complete_program():
    global at_work
    at_work = False
    print("Программа завершена!")


def start_menu():
    print("""
    МЕНЮ:
    1. Вывести список студентов;
    2. Вывести общий средний балл;
    3. Добавить нового студента;
    4. Удалить студента с самым низким балом.
    5. Выход.""")


def main():
    menu_operations = {1: display_list_of_student,
                       2: display_common_average_grade, 3: add_student,
                       4: delete_worst_student, 5: complete_program}

    while at_work:
        menu_item = request_menu_item()
        menu_operations[menu_item]()


# 1-ое задание.
students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]
at_work = True
start_menu()
main()
