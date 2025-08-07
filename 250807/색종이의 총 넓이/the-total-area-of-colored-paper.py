#입력

n = int(input())

grid = [
    [0]*201 for _ in range(201)
]


#격자(좌표평면)위에서 2차원배열에서의 구간 칠하기(+1 과정)
for i in range(n):
    x,y = tuple(map(int,input().split()))
    for j in range(x,x+8):
        x_index = j+100
        for k in range(y,y+8):
            y_index = k+100
            grid[x_index][y_index]+=1

result=0
for i in range(201):
    for j in range(201):
        if grid[i][j]>=1:
            result+=1
    
print(result)

