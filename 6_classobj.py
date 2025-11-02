class Student:
    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
    
    def percentage(self):
        return ((self.s1 + self.s2 + self.s3 + self.s4) * 100) / 400

s1 = Student(98, 88, 76, 87)
s2 = Student(96, 78, 56, 77)

studList = [s1, s2]

def calpercentage(stdList):
    percentages = []
    for eachStudent in stdList:
        m = eachStudent.percentage()
        percentages.append(m)
    return percentages

print(calpercentage(studList))
