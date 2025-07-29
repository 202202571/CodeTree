class Point:
    def __init__(self,x,y,number,distance):
        self.x = x
        self.y = y
        self.number =number
        self.distance=distance
    
    def __str__(self):
        return f"{self.number}"

n = int(input())

points = []
num = 1
for _ in  range(n):
    x,y = input().split()
    x,y = int(x),int(y)
    distance = abs(x)+abs(y)
    points.append(Point(x,y,num,distance))
    num+=1

sorted_points = sorted(points,key = lambda x: (x.distance,x.number))

for i in range(n):
    print(sorted_points[i])
    



