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
        #중복된 영역을 제외하는 것이 아닌, 중복된 영역을 포함하여 어차피 한번만 세면 되니까
        #1보다 큰 영역에 대해서 result+=1를 해주기만 하면 된다.(생각보다 간단)
        if grid[i][j]>=1:
            result+=1
        #우리가 생각하는 문제풀이 방식과 코드로 구현하는 방식에 차이가 있다는 것을 유념하자.
    
print(result)

