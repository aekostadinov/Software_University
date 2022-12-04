"""Create a class Class. The __init__ method should receive the name of the class. Each class should also have 2 empty
 lists - students and grades. Create a class attribute __students_count equal to 22. The class should also have 3 additional methods:

· add_student(name: str, grade: float) - adds the student and the grade in the two lists if there is free space in the class
· get_average_grade() - returns the average of all existing grades formatted to the second decimal point (as a number)
· __repr__ - returns the string (single line):

"The students in {class_name}: {students}. Average grade: {average_grade}".

The students must be separated by a comma and a space: ", "."""


class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(str(name))
            self.grades.append(float(grade))

    def get_average_grade(self):
        number = f"{(sum(self.grades) / len(self.grades)):.2f}"
        return float(number)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. " \
               f"Average grade: {Class.get_average_grade(self)}"