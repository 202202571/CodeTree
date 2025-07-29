class Student:
    def __init__(self,height,weight,number):
        self.height=height
        self.weight=weight
        self.number=number
    
    def __str__(self):
        return f"{self.height} {self.weight} {self.number}"
n = int(input())

num=1
students = []
for i in range(n):
    h,w = map(int,input().split())
    students.append(Student(h,w,num))
    num+=1

students = sorted(students,key = lambda x: (-x.height,-x.weight,x.number))

for i in range(n):
    print(students[i])