from math import sqrt
from pprint import pprint
import numpy as np

from Student import Student


def generete_grades(n):
    """
    generates random grades for n students
    :param n: integer representing number of students
    :return: list of student objects
    """
    lst = []

    for i in range(n):
        grade = 100 * np.random.random((4, 5))
        grade = grade.astype(int)
        lst.append(Student(f"student-{i}", grade))

    return lst


def calculate_strength(lst):
    """
    calculates strength for every student from dictionary
    :param lst:  list of student objects and returns stronges
    :return:  best student
    """
    return max([(stud.strength, stud.name) for stud in lst])

ls = generete_grades(5)
for x in ls:
    print(x.strength, x.name)
print(calculate_strength(ls))




