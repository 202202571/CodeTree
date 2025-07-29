class Person:
    def __init__(self,name,height,weight):
        self.name =name
        self.height=height
        self.weight=weight
    
    def __str__(self):
        return f"{self.name} {self.height} {self.weight:.1f}"
    
people = []    
for _ in range(5):
    name,height,weight = input().split()
    height = int(height)
    weight= float(weight)
    people.append(Person(name,height,weight))

sorted_name = sorted(people,key = lambda x: x.name)

sorted_height = sorted(people,key = lambda x: -x.height)

print("name")
for i in range(5):
    print(sorted_name[i])

print()

print("height")
for i in range(5):
    print(sorted_height[i])

