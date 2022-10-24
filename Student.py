from math import sqrt



def frobeniusNorm(mat):
    row = mat.shape[0]
    col = mat.shape[1]
    sumSq = 0
    for i in range(row):
        for j in range(col):
            sumSq += pow(mat[i][j], 2)


    res = sqrt(sumSq)
    return round(res, 5)

class Student:

    def __init__(self, name,grades):
        # grades is 4X5 np array
        # representing grades
        self.name = name
        self.grades = grades
        self.strength = self.calculate_strength()

    def calculate_strength(self):
        """
        This method calculates strength of student by grades
        I use Frobenius norm for that
        :return: strength in float
        """
        return frobeniusNorm(self.grades)  # Frobenius from is second norm


