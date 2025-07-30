
n = int(input())
directions = []
distances = []
for _ in range(n):
    direction,distance=input().split()
    distance = int(distance)
    directions.append(direction)
    distances.append(distance)

dx,dy = [1,0,-1,0], [0,1,0,-1]
x,y=0,0

dir_num =0
for i in range(n):
        
    if directions[i]=='E':
        dir_num = 0
    elif directions[i]=='N':
        dir_num=1
    elif directions[i]=='W':
        dir_num=2
    else:
        dir_num=3
    
    x=x+dx[dir_num]*distances[i]
    y=y+dy[dir_num]*distances[i]

print(f"{x} {y}")



