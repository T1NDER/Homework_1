class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rating):
        if course not in lecturer.courses_attached:
            print(f'Лектор {lecturer.name} {lecturer.surname} не закреплён за курсом {course}')
            return
        if course not in self.courses_in_progress:
            print(f'Студент {self.name} {self.surname} не записан на курс {course}')
            return
        lecturer.ratings[course].append(rating)
        print(f'Студент {self.name} {self.surname} поставил оценку {rating} лектору {lecturer.name} {lecturer.surname} '
              f'за курс {course}')

    def get_average_grade(self):
        total_grades = sum(self.grades.values())
        total_assignments = len(self.grades)
        return total_grades / total_assignments if total_assignments else 0.0

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
        self.ratings = {course: [] for course in courses_attached}

    def get_average_rating(self):
        total_ratings = sum(sum(ratings) for ratings in self.ratings.values())
        total_lectures = sum(len(ratings) for ratings in self.ratings.values())
        return total_ratings / total_lectures if total_lectures else 0.0

    def __str__(self):
        average_rating = self.get_average_rating()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating}"

    def __lt__(self, other):
        return self.get_average_rating() < other.get_average_rating()

    def __le__(self, other):
        return self.get_average_rating() <= other.get_average_rating()

    def __gt__(self, other):
        return self.get_average_rating() > other.get_average_rating()

    def __ge__(self, other):
        return self.get_average_rating() >= other.get_average_rating()

    def __eq__(self, other):
        return self.get_average_rating() == other.get_average_rating()

    def __ne__(self, other):
        return self.get_average_rating() != other.get_average_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached

    def check_homework(self, student, course, grade):
        if course not in self.courses_attached:
            print(f"Эксперт {self.name} {self.surname} не закреплен за курсом {course}")
            return
        if course not in student.courses_in_progress:
            print(f"Студент {student.name} {student.surname} не записан на курс {course}")
            return
        student.grades[course].append(grade)
        print(f'Эксперт {self.name} {self.surname} проверил домашнюю работу у студента {student.name} {student.surname} '
              f'по курсу {course} с оценкой {grade}')

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
def get_average_grade_for_course(students, course):
    """
    Функция для подсчета средней оценки за курс по всем студентам.
    """
    total_grades = 0
    count_grades = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            count_grades += len(student.grades[course])
    return total_grades / count_grades if count_grades else 0.0

def get_average_rating_for_lecturer(lecturers, course):
    """
    Функция для подсчета средней оценки за курс по всем лекторам.
    """
    total_ratings = 0
    count_ratings = 0
    for lecturer in lecturers:
        if course in lecturer.ratings:
            total_ratings += sum(lecturer.ratings[course])
            count_ratings += len(lecturer.ratings[course])
    return total_ratings / count_ratings if count_ratings else 0.0

student1 = Student('Иван', 'Иванов', 'мужской')
student1.courses_in_progress = ['Python', 'Git']
student1.grades['Python'] = [10, 9, 8]
student1.grades['Git'] = [7, 8, 9]

student2 = Student('Петр', 'Петров', 'мужской')
student2.courses_in_progress = ['Python', 'Введение в программирование']
student2.grades['Python'] = [9, 10, 10]
student2.grades['Введение в программирование'] = [8, 9, 10]

lecturer1 = Lecturer('Александр', 'Алексеев', ['Python', 'Git'])
lecturer1.ratings['Python'] = [10, 9, 10]
lecturer1.ratings['Git'] = [8, 9, 10]

lecturer2 = Lecturer('Елена', 'Еленова', ['Введение в программирование', 'Python'])
lecturer2.ratings['Введение в программирование'] = [9, 10, 10]
lecturer2.ratings['Python'] = [10, 9, 8]

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка за курс 'Python' у студентов: {get_average_grade_for_course(students, 'Python')}")
print(f"Средняя оценка за курс 'Введение в программирование' у студентов: {get_average_grade_for_course(students, 'Введение в программирование')}")

print(f"Средняя оценка за курс 'Python' у лекторов: {get_average_rating_for_lecturer(lecturers, 'Python')}")
print(f"Средняя оценка за курс 'Введение в программирование' у лекторов: {get_average_rating_for_lecturer(lecturers, 'Введение в программирование')}")
