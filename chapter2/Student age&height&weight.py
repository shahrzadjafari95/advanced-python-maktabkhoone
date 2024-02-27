from statistics import mean


class Student:
    def __init__(self, age_list: list, height_list: list, weight_list: list):
        self.age_list = age_list
        self.height_list = height_list
        self.weight_list = weight_list

    def average_age(self):
        average_age = float(mean(self.age_list))
        return average_age

    def average_height(self):
        average_height = float(mean(self.height_list))
        return average_height

    def average_weight(self):
        average_weight = float(mean(self.weight_list))
        return average_weight


students_age = []
students_height = []
students_weight = []
for i in range(2):
    number1 = int(input())
    ages = list(map(int, input().split(' ')))
    students_age.append(ages)
    height = list(map(int, input().split(' ')))
    students_height.append(height)
    weights = list(map(int, input().split(' ')))
    students_weight.append(weights)

A = Student(students_age[0], students_height[0], students_weight[0])
B = Student(students_age[1], students_height[1], students_weight[1])

print(A.average_age())
print(A.average_height())
print(A.average_weight())
print(B.average_age())
print(B.average_height())
print(B.average_weight())

if A.average_height() > B.average_height():
    print('A')
elif A.average_height() < B.average_height():
    print('B')
elif A.average_height() == B.average_height():
    if A.average_weight() < B.average_weight():
        print('A')
    elif A.average_weight() > B.average_weight():
        print('B')
    else:
        print('Same')
